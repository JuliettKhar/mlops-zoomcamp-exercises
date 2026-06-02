## Notebooks

| Notebook                  | Description                                                                                         | Colab                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| duration-prediction.ipynb | Converting the notebook into a Python script and preparing the training pipeline for orchestration. | [Open in Colab](https://colab.research.google.com/drive/1Mi6SFjXagT5mnKuEpaszjKdXFUKKcx6-?usp=sharing) |
| duration-prediction.py    | Python version of the training pipeline used for orchestration.                                     | —                                                                                                      |
| HW03.ipynb                | Homework for Module 3: ML Pipelines and Workflow Orchestration.                                     | [Open in Colab](https://colab.research.google.com/drive/1p_4QQfXLYXLhvKVg0PPJsESDlRkSaeEM?usp=sharing) |
| HW03.py                   | Python implementation of the homework workflow.                                                     | —                                                                                                      |
| hello.py                  | Simple example script used for testing the orchestration setup.                                     | —                                                                                                      |
| Prefect Pipeline Demo     | Example of running the workflow with an orchestrator.                                               | [Open in Colab](https://colab.research.google.com/drive/1m8K3-kfCCc4ziJ3BPNnJWo6Xv1tAidz1?usp=sharing) |

## Project Structure

| Directory / File | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| data/            | NYC Taxi datasets used for training and validation.                         |
| artifacts/       | Generated artifacts produced by the pipeline.                               |
| mlruns/          | MLflow tracking data, including experiments, runs, metrics, and parameters. |
| models/          | Saved trained models.                                                       |
| mlflow.db        | SQLite database used by MLflow.                                             |
| run_id.txt       | Stored MLflow run identifier for model registration and reproducibility.    |
| README.md        | Documentation and project overview.                                         |
