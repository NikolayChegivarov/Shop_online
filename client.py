import requests
print("client")

# Регистрируем клиента.

# Данные для регистрации пользователя
data = {
    'first_name': 'Николай',
    'last_name': 'Гусаров',
    'email': 'nikolai_polos@mail.ru',
    'password': 'verystrongpassword123',
    'company': 'Example Inc.',
    'position': 'Developer'
}

# Отправляем POST-запрос на регистрацию пользователя
response = requests.post("http://127.0.0.1:8000/api/v1/user/register", data=data)

# Проверяем ответ от сервера
if response.status_code == 200:
    print("Регистрация прошла успешно:", response.json())
else:
    print("Ошибка при регистрации:", response.status_code, response.text)



