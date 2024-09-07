FROM python:3.9-slim-buster

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt --timeout=60  # --upgrade

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

