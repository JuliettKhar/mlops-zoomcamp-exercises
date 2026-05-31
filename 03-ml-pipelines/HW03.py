#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
import sklearn
from prefect import flow, task
import mlflow

filename_yellow = 'data/yellow_tripdata_2026-01.parquet'

@task
def read_dataframe(filename):
    df = pd.read_parquet(filename)
    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.apply( lambda td: td.total_seconds() / 60)

    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    return df

@task
def prepare_features(df):
    categorical = ['PULocationID', 'DOLocationID']
    train_dict = df[categorical].to_dict(orient='records')
    dv = DictVectorizer()
    x_train = dv.fit_transform(train_dict)
    y_train = df.duration.values

    return dv, x_train, y_train

@task
def train_model(x_train, y_train):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_pred = lr.predict(x_train)
    
    return lr

@task
def register_model(lr):
    with mlflow.start_run():
        mlflow.sklearn.log_model(
            sk_model=lr,
            name="model"
        )

@flow
def taxi_pipeline(filename, year, month):
    df = read_dataframe(filename)
    _, X_train, y_train = prepare_features(df)
    lr  = train_model(X_train, y_train)
    register_model(lr)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)

    args = parser.parse_args()

    taxi_pipeline(filename_yellow, year=args.year, month=args.month)