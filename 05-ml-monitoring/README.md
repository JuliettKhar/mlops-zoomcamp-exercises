## Notebooks

| Notebook                          | Description                                                                                       | Colab                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| HW_5.ipynb                        | Homework for Module 5: Model Monitoring. Data and prediction drift with Evidently.               | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/05-ml-monitoring/HW_5.ipynb)               |
| baseline_model_nyc_taxi_data.ipynb | Baseline model, Evidently drift reports, and daily metrics written to Postgres for Grafana.       | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/05-ml-monitoring/baseline_model_nyc_taxi_data.ipynb) |
| debug_nyc_taxi.ipynb              | Debugging drift on a problematic day with an Evidently test suite.                               | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/05-ml-monitoring/debug_nyc_taxi.ipynb)     |

## Project Structure

| Directory / File          | Description                                                                |
| ------------------------- | -------------------------------------------------------------------------- |
| data/                     | Green NYC Taxi datasets and the `reference.parquet` baseline for drift.    |
| models/                   | Trained model (`lin_reg.bin`) with the bundled preprocessor.              |
| config/                   | Grafana provisioning (datasources and dashboard configuration).           |
| dashboards/               | Grafana dashboard definition for data drift (`data_drift.json`).          |
| docker-compose.yml        | Postgres + Adminer + Grafana stack used for the monitoring dashboards.    |
| requirments.txt           | Project dependencies required to run the notebooks.                       |
| README.md                 | Documentation and project overview.                                       |
