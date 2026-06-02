## Notebooks

| Notebook                  | Description                                                                        | Colab                                                                                                  |
| ------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| starter.ipynb             | Homework for Module 4: Model Deployment. Batch scoring of NYC Taxi trip durations. | [Open in Colab](https://colab.research.google.com/drive/1zvaJJRdQoU-7HIQoRXgnQ4MINJ3x1cgc?usp=sharing) |
| duration-prediction.ipynb | Training the linear regression model used for the deployment service.             | —                                                                                                      |

## Project Structure

| Directory / File                          | Description                                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------------- |
| web-service/                              | Flask web service that serves the duration-prediction model.                      |
| web-service/predict.py                    | Flask app exposing the `/predict` endpoint for online inference.                  |
| web-service/test.py                       | Client script that sends a sample ride to the deployed service.                   |
| web-service/starter.py                    | Batch scoring script (converted from `starter.ipynb`).                            |
| web-service/starter-docker.py             | Batch scoring script adapted to run inside the Docker container.                  |
| web-service/Dockerfile                    | Image definition for running the web service.                                     |
| web-service/Dockerfile.06                 | Alternative Dockerfile variant used for the homework.                             |
| web-service/Pipfile / Pipfile.lock        | Pipenv environment with the service dependencies.                                 |
| web-service/lin_reg.bin                   | Serialized `DictVectorizer` and linear regression model.                          |
| web-service/models/                       | Saved model and preprocessor artifacts.                                           |
| web-service/*_predictions.parquet         | Batch prediction outputs for the scored NYC Taxi datasets.                        |
| README.md                                 | Documentation and project overview.                                               |
