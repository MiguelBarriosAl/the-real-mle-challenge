FROM python:3.8-slim-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api /app/api
COPY models /app/models
COPY tests /app/tests
COPY utils /app/utils

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
