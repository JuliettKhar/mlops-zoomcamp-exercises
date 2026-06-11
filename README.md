# MLOps Zoomcamp — Exercises

End-to-end MLOps practice — hands-on exercises from the **MLOps Zoomcamp** course (DataTalks.Club), worked through module by module on the NYC Taxi trip duration prediction task: from model training through experiment tracking, deployment, monitoring, and testing.

Course materials I followed: [JuliettKhar/mlops-zoomcamp](https://github.com/JuliettKhar/mlops-zoomcamp/tree/main)

## Tech stack

- **ML:** Python, pandas, scikit-learn, XGBoost
- **Experiment tracking:** MLflow, Hyperopt
- **Pipelines:** parameterized training scripts, Prefect (demo)
- **Deployment:** Flask, Docker
- **Monitoring:** Evidently, PostgreSQL, Grafana
- **Testing:** pytest

## Modules

| Module | Topic | Description |
| ------ | ----- | ----------- |
| [01-intro](01-intro/) | Introduction | Linear regression baseline for NYC Taxi trip duration prediction. |
| [02-experiment-tracking](02-experiment-tracking/) | Experiment Tracking | Logging parameters, metrics, and models with MLflow; model registry. |
| [03-ml-pipelines](03-ml-pipelines/) | ML Pipelines | Turning the notebook into an orchestrated training pipeline. |
| [04-deploy](04-deploy/) | Deployment | Serving the model as a Flask web service and as a batch scoring script. |
| [05-ml-monitoring](05-ml-monitoring/) | Monitoring | Data and prediction drift with Evidently; metrics to Postgres + Grafana. |
| [06-tests](06-tests/) | Best Practices | Unit testing the batch scoring pipeline with pytest. |
| [07-final-project](07-final-project/) | Final Project | End-to-end MLOps app — [used car price prediction](https://github.com/JuliettKhar/used-car-price-prediction-mlops) (separate repo). |

Each module folder has its own `README.md` with the notebooks, descriptions, and "Open in Colab" links.

## Running the notebooks in Google Colab

The "Open in Colab" links in each module README are **GitHub-backed** — they always load the latest version of the notebook straight from this repository.

Every Colab-ready notebook starts with two commented setup cells:

```python
# Colab reproducibility — uncomment to clone the repo and enter this folder:
# !git clone https://github.com/JuliettKhar/mlops-zoomcamp-exercises.git
# %cd mlops-zoomcamp-exercises/<module>

# Colab setup — uncomment to install packages not preinstalled in Colab:
# !pip install ...
```

Uncomment them when running in Colab to clone the repo (for local data/model files) and install any packages that aren't preinstalled. Public NYC TLC datasets are loaded directly from their URLs, so they work everywhere without setup.
