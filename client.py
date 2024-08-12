import requests
print("client")

# РЕГЕСТРИРУЕМ КЛИЕНТА.

# Данные для регистрации пользователя
data = {
    'first_name': 'Николай',
    'last_name': 'Гусев',
    'email': 'kolyapolosin85@gmail.com',
    'password': 'verystrongpassword123',
    'company': 'Efes',
    'position': 'manager'
}

# Отправляем POST-запрос на регистрацию пользователя
response = requests.post("http://127.0.0.1:8000/api/v1/user/register", data=data)
#
# # Проверяем ответ от сервера
# if response.status_code == 200:
#     print("Регистрация прошла успешно:", response.json())
# else:
#     print("Ошибка при регистрации:", response.status_code, response.text)

# УДАЛЯЕМ КЛИЕНТА.
# response = requests.delete('http://localhost:8000/api/v1/user/delete/2/')
# print(response.status_code)
#
# # Проверяем статус ответа
# if response.status_code == 204:  # 204 No Content - успешное удаление без возврата тела ответа
#     print("Пользователь успешно удален.")
# else:
#     print(f"Ошибка при удалении пользователя: {response.status_code}")

# # ПРОВЕРЯЕМ ПОЧТУ
# response = requests.post('http://localhost:8000/api/v1/test_email/')
#
# # ДОБАВЛЯЕМ ПРАЙС
# response = requests.post('http://localhost:8000/api/v1/partner/update/')
# Создаем магазин

# ПОДТВЕРЖДАЕМ


