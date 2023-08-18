FROM python:3.11-slim

WORKDIR /app
COPY ./requirements.txt /app
COPY ./hello_rest_api /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]