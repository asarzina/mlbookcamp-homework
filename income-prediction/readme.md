# Midterm project: income prediction

[https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/07-midterm-project)

Dataset: [https://www.kaggle.com/lodetomasi1995/income-classification](https://www.kaggle.com/lodetomasi1995/income-classification)

Goal: prediction task is to determine whether a person makes over 50K a year.

## Description

The project is a classification problem. I want to determine if a person makes over 50K a year.

I try multiple models anche the best one in XGBoost.

## Repository

[https://github.com/asarzina/mlbookcamp-homework/tree/main/income-prediction](https://github.com/asarzina/mlbookcamp-homework/tree/main/income-prediction)

## Run locally with Docker

To run locally with Docker it's needed to comment the last line of Dockerfile

```Dockerfile
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
# ENTRYPOINT ["gunicorn", "predict:app"]
```

```
docker build -t project_income .

docker run -it --rm -p 9696:9696 project_income:latest
```

## Demo APIs

Endpoint: [https://ml-zoomcamp-income-prediction.herokuapp.com](https://ml-zoomcamp-income-prediction.herokuapp.com)

### Heartbit API

GET `/heartbit`

Example:

```bash
curl --location --request GET 'https://ml-zoomcamp-income-prediction.herokuapp.com/heartbit'
```

### Predict API

GET `/predict`

Example:

```bash
curl --location --request POST 'https://ml-zoomcamp-income-prediction.herokuapp.com/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 35,
    "workclass": "private",
    "fnlwgt": 159449,
    "education": "bachelors",
    "education-num": 13,
    "marital-status": "married-civ-spouse",
    "occupation": "exec-managerial",
    "relationship": "husband",
    "race": "white",
    "sex": "male",
    "capital-gain": 3000,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "italy"
}'
```

## Deploy to Heroku

To deploy to Heroku it's needed to uncomment the last line of Dockerfile

```Dockerfile
# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
ENTRYPOINT ["gunicorn", "predict:app"]
```

- Install Heroku CLI locally (see [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli))
- Login to Heroku
- Create Heroku app

```bash
heroku login

heroku container:login

heroku create ml-zoomcamp-income-prediction
```

- Compile Docker image and deploy to Heroku

```bash
heroku container:push web -a ml-zoomcamp-income-prediction

heroku container:release web -a ml-zoomcamp-income-prediction
```
