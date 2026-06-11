**Module 2 — Experiment Tracking.** Tracking experiments with MLflow — logging parameters, metrics and artifacts, hyperparameter tuning with Hyperopt, and registering models in the MLflow Model Registry.

## Notebooks

| Notebook                  | Description                                                                                 | Colab                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| HW_exper-tracking.ipynb   | Homework for Module 2: Experiment Tracking and Model Management.                            | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/02-experiment-tracking/HW_exper-tracking.ipynb) |
| mlflow-tracking.ipynb     | MLflow basics: logging parameters, metrics, artifacts, and models.                          | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/02-experiment-tracking/mlflow-tracking.ipynb) |
| duration-prediction.ipynb | Baseline NYC Taxi trip duration prediction using linear regression and feature engineering. | [Open in Colab](https://colab.research.google.com/github/JuliettKhar/mlops-zoomcamp-exercises/blob/main/02-experiment-tracking/duration-prediction.ipynb) |

## Project Structure

| Directory / File         | Description                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------- |
| data/                    | Input datasets used for training and validation.                                   |
| artifacts/               | MLflow artifacts, including logged models and experiment outputs.                  |
| mlartifacts/             | Local artifact storage used by MLflow.                                             |
| mlruns/                  | MLflow tracking data containing experiments, runs, parameters, and metrics.        |
| output/                  | Generated outputs and intermediate results.                                        |
| preprocessor/            | Saved preprocessing objects such as DictVectorizer and feature transformers.       |
| homework/                | Homework-related files and resources.                                              |
| running-mlflow-examples/ | Additional examples demonstrating MLflow experiment tracking and model management. |
| mlflow.db                | SQLite database used by MLflow Tracking Server.                                    |
| requirements.txt         | Project dependencies required to run the notebooks and experiments.                |
