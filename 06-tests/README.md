## Overview

Homework for Module 6 (Best Practices): a batch scoring script for NYC Taxi trip
duration prediction, covered with `pytest` unit tests.

## Project Structure

| File                    | Description                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| batch.py                | Batch scoring pipeline: load model, read and prepare data, predict, and write predictions.       |
| lin_reg.bin             | Serialized `DictVectorizer` and linear regression model.                                         |
| tests/test_batch.py     | Unit tests for `prepare_data` and `predict_data` using fake vectorizer/model stubs.              |
| tests/\_\_init\_\_.py   | Marks `tests/` as a Python package.                                                               |

## batch.py

Reads the public NYC TLC yellow taxi dataset, prepares features, predicts trip
duration, and saves the results to a parquet file. Run it for a given year/month:

```bash
python batch.py --year 2023 --month 1
```

Functions: `read_model`, `read_data`, `prepare_data`, `predict_data`, `build_ride_id_col`.

## Running the tests

```bash
pytest
```

`test_prepare_data` checks feature engineering and outlier filtering; `test_predict_data`
checks prediction wiring with stubbed `DictVectorizer` and model objects.
