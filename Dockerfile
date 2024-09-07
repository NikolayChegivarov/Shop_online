FROM python:3.9-slim-buster

COPY . .

#ENV http_proxy http://79.174.91.58:8080
#ENV https_proxy http://79.174.91.58:8080
#RUN pip3 install --no-cache-dir -r requirements.txt --timeout=120  # --upgrade

RUN pip3 install --no-cache-dir -r requirements.txt --timeout=120 && \
    export http_proxy=http://79.174.91.58:8080 && \
    export https_proxy=http://79.174.91.58:8080 && \
    pip3 install --no-cache-dir -r requirements.txt --timeout=120

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
