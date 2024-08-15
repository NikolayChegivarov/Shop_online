
pip install django

pip install python-dotenv  Для .env

pip install django-rest-passwordreset  Для генерации токена  

pip install djangorestframework  

pip install psycopg2      
pip install psycopg2-binary  

python manage.py migrate

pip install pyyaml

разобраться с авторизацией
создать магазин
загрузить прайс

Порядок действий: 
RegisterAccount = сохраняем персональные данные пользователя в БД.
new_user_registered_signal = сигнал автоматически срабатывает при регистрации с помощью ConfirmEmailToken генерирует токен

Для отправки писем вместо консоли на электронную почту, в settings.py поменяйте 'console' на 'smtp'.


