FROM python:3.9-slim-buster

WORKDIR /simple_app

COPY ./simple_app/requirements.txt ./simple_app/requirements.txt

RUN pip install --no-cache-dir -r simple_app/requirements.txt

COPY ./simple_app ./simple_app

EXPOSE 8080

CMD ["uvicorn", "simple_app.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
