#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd

with open('lin_reg.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)



def read_data(year, month):
    df = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df['PULocationID'] = df['PULocationID'].fillna(-1).astype('int').astype('str')
    df['DOLocationID'] = df['DOLocationID'].fillna(-1).astype('int').astype('str')

    df['PU_DO'] = df['PULocationID'] + '_' + df['DOLocationID']

    return df

def prepare_data(df):
    categorical = ['PU_DO']

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_train = df.duration.values
    y_pred = model.predict(X_val)

    print("Mean:", y_pred.mean())
    print("Std:", y_pred.std())

    return y_pred

def build_ride_id_col(df, y_pred, year, month):
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
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

    df = read_data(args.year, args.month)
    y_pred = prepare_data(df)
    build_ride_id_col(df, y_pred, args.year, args.month)
