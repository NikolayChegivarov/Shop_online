
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
authorization = сигнал автоматически срабатывает при регистрации, с помощью ConfirmEmailToken генерирует токен,  
отправляет письмо с токеном для подтверждения почты. 
ссылка ведет к представлению ConfirmEmail которая осуществляет проверку токена в ConfirmEmailToken меняет is_active на 
True, после чего удаляет токен. 
Входим на сайт с помощью LoginAccount



Для отправки писем вместо консоли на электронную почту, в settings.py поменяйте 'console' на 'smtp'.


