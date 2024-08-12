import requests
print("client")

# РЕГЕСТРИРУЕМ КЛИЕНТА.

# Данные для регистрации пользователя
data = {
    'first_name': 'Николай',
    'last_name': 'Гусаров',
    'email': 'kolyapolosin85@gmail.com',
    'password': 'verystrongpassword123',
    'company': 'Efes',
    'position': 'manager'
}

# Отправляем POST-запрос на регистрацию пользователя
response = requests.post("http://127.0.0.1:8000/api/v1/user/register", data=data)

# Проверяем ответ от сервера
if response.status_code == 200:
    print("Регистрация прошла успешно:", response.json())
else:
    print("Ошибка при регистрации:", response.status_code, response.text)

# УДАЛЯЕМ КЛИЕНТА.

