from datetime import datetime as dt

import pandas as pd

import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).resolve().parents[1]))

from batch import prepare_data, predict_data

class FakeDV:
    def transform(self, dicts):
        return dicts


class FakeModel:
    def predict(self, X):
        return np.array([10.0, 20.0])


def test_prepare_data():
    data = [
        (None, None, dt(2023, 1, 1, 1, 1), dt(2023, 1, 1, 1, 10)),
        (1, 1, dt(2023, 1, 1, 1, 2), dt(2023, 1, 1, 1, 10)),
        (1, None, dt(2023, 1, 1, 1, 2, 0), dt(2023, 1, 1, 1, 2, 59)),
        (3, 4, dt(2023, 1, 1, 1, 2, 0), dt(2023, 1, 2, 1, 2, 1)),
    ]

    columns = [
        'PULocationID',
        'DOLocationID',
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
    ]

    df = pd.DataFrame(data, columns=columns)

    actual = prepare_data(df)

    actual_data = actual[
        ['PULocationID', 'DOLocationID', 'duration', 'PU_DO']
    ].to_dict(orient='records')

    expected_data = [
        {'PULocationID': '-1', 'DOLocationID': '-1', 'duration': 9.0, 'PU_DO': '-1_-1'},
        {'PULocationID': '1', 'DOLocationID': '1', 'duration': 8.0, 'PU_DO': '1_1'},
    ]

    assert actual_data == expected_data

    from batch import predict_data


def test_predict_data():
    df = pd.DataFrame([
        {'PU_DO': '-1_-1', 'duration': 9.0},
        {'PU_DO': '1_1', 'duration': 8.0},
    ])

    dv = FakeDV()
    model = FakeModel()

    actual = predict_data(df, dv, model)

    assert list(actual) == [10.0, 20.0]