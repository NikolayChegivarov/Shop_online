FROM python:3.9-slim-buster

WORKDIR /src

COPY . .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel



CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "8000"]
