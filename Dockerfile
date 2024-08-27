FROM python:3.12

WORKDIR /src

COPY . .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "8000"]
