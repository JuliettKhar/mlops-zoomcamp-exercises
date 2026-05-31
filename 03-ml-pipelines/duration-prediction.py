#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import root_mean_squared_error
import mlflow
import xgboost as xgb
from pathlib import Path

mlflow.set_tracking_uri('http://localhost:5001')
mlflow.set_experiment('my-new-experiment-2')

models_folder = Path('models')
models_folder.mkdir(exist_ok=True)

def read_dataframe(year, month): 
    filename = f"data/green_tripdata_{year}-{month:02d}.parquet"
    df = pd.read_parquet(filename)
    print(df.sh)

    df['duration'] = df.lpep_dropoff_datetime - df.lpep_pickup_datetime
    df.duration = df.duration.apply(lambda td: td.total_seconds() / 60)

    df = df[((df.duration >= 0) & (df.duration <= 60))]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)
    df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']

    return df

def create_X(df, dv = None):
    categorical = ['PU_DO']
    numerical = ['trip_distance']
    dicts = df[categorical + numerical].to_dict(orient='records')

    if dv is None:
        dv = DictVectorizer(sparse=True)
        X = dv.fit_transform(dicts)
    else: 
        X = dv.transform(dicts)

    return X, dv


def train_model(X_train, y_train, X_val, y_val, dv):
    with mlflow.start_run() as run:
        run_id = run.info.run_id
        train = xgb.DMatrix(X_train, label=y_train)
        valid = xgb.DMatrix(X_val, label=y_val)

        best_params = {
            'learning_rate': 0.23663837413933345,
            'max_depth': 63,
            'min_child_weight': 5.145379319889727,
            'objective': 'reg:linear',
            'reg_alpha': 0.011421312210525376,
            'reg_lambda': 0.365514542783101,
            'seed': 42
        }
        mlflow.log_params(best_params)

        booster = xgb.train(
            params=best_params,
            dtrain=train,
            num_boost_round=30,
            evals=[(valid, 'validation')],
            early_stopping_rounds=50
        )  
        y_pred = booster.predict(valid) 
        rmse = root_mean_squared_error(y_val, y_pred)

        mlflow.log_metric('rmse', rmse)

        with open("models/preprocessor.b", "wb") as f_out:
            pickle.dump(dv, f_out)
            mlflow.xgboost.log_model(booster, artifact_path='models_mlflow')
            mlflow.log_artifact(local_path='models/preprocessor.b', artifact_path='models_mlflow')

    return run_id

from prefect import flow 

@flow
def main(year, month):
    df_train = read_dataframe(year, month)
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    df_val = read_dataframe(year=next_year, month=next_month)

    X_train, dv = create_X(df_train)
    X_val, _ = create_X(df_val, dv)


    target = 'duration'
    y_train = df_train[target].values
    y_val = df_val[target].values

    run_id = train_model(X_train, y_train, X_val, y_val, dv)
    return run_id


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="train model")
    parser.add_argument('--year', type=int, required=True, help="year")
    parser.add_argument('--month', type=int, required=True, help="month")
    args = parser.parse_args()

    run_id = main(year=args.year, month=args.month)
    print(f"run_id: {run_id}")

    with open("run_id.txt", "w") as file:
        file.write(run_id)

