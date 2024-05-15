FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY ./website /app

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "streamlit", "run", "main.py" , "--server.port", "8080"]
