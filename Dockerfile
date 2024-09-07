FROM python:3.9-slim-buster

COPY . .

# Настройка прокси
ENV http_proxy=http://79.174.91.58:8080
ENV https_proxy=http://79.174.91.58:8080

# Установка pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

# Установка переменных окружения
RUN pip3 config set global.use_new_style_url=True && \
    pip3 config set pypi.pypi.org/https://pypi.tuna.tsinghua.edu.cn/simple

# Установка зависимостей
RUN pip3 install --no-cache-dir -r requirements.txt --timeout=300

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
