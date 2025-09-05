# API/Dockerfile
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .


RUN useradd -m -u 1000 django
USER django


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]