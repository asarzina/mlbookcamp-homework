FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN apt-get update && apt-get install -y libgomp1
RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
# ENTRYPOINT ["gunicorn", "predict:app"]