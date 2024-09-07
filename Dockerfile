FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools wheel

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "8000"]
