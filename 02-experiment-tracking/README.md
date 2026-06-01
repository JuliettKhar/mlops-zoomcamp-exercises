## Notebooks

| Notebook                  | Description                                                                                 | Colab                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| HW_exper-tracking.ipynb   | Homework for Module 2: Experiment Tracking and Model Management.                            | [Open in Colab](https://colab.research.google.com/drive/1m1VWy0zc2wNgEQ05ak0-kBErnCyQcclA?usp=sharing) |
| mlflow-tracking.ipynb     | MLflow basics: logging parameters, metrics, artifacts, and models.                          | [Open in Colab](https://colab.research.google.com/drive/1VNFSJrl2uEvZ5vV4HZ961aJegn7HgqXo?usp=sharing) |
| duration-prediction.ipynb | Baseline NYC Taxi trip duration prediction using linear regression and feature engineering. | [Open in Colab](https://colab.research.google.com/drive/1ZHmzhr_fwyUZeDiqTwLd3I_VvLb_LcQ5?usp=sharing) |

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
