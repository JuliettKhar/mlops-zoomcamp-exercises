#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd

def read_model():
    with open('lin_reg.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
        return (dv, model)


def read_data(year, month):
    df = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')
    return df

def prepare_data(df):
    df = df.copy()
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df['PULocationID'] = df['PULocationID'].fillna(-1).astype('int').astype('str')
    df['DOLocationID'] = df['DOLocationID'].fillna(-1).astype('int').astype('str')

    df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    return df


def predict_data(df, dv, model):
    categorical = ['PU_DO']

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    print("Mean:", y_pred.mean())
    print("Std:", y_pred.std())

    return y_pred

def build_ride_id_col(df, y_pred, year, month):
    df = df.copy()
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    df_res = pd.DataFrame()
    df_res['ride_id'] = df['ride_id']
    df_res['predicted_duration'] = y_pred
    output_file = f'yellow_tripdata_{year}-{month}_predictions.parquet'
    df_res.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )


if(__name__ == '__main__'):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)

    args = parser.parse_args()

    dv, model = read_model()
    df = read_data(args.year, args.month)
    df = prepare_data(df)
    y_pred = predict_data(df, dv, model)
    build_ride_id_col(df, y_pred, args.year, args.month)
