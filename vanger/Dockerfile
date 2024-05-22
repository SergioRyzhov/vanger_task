FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.pip /app/

RUN apt-get update \
    && apt-get install -y gcc python3-dev default-libmysqlclient-dev \
    && pip install --no-cache-dir -r req.pip \
    && apt-get purge -y --auto-remove gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

ENV PYTHONPATH="/app/vanger"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]