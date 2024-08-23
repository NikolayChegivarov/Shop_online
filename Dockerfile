FROM python:3.12

WORKDIR /src

COPY . .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ENV MY_ENV=netology_02_06_2024

CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "5050"]
