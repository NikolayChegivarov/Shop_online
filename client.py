import requests
print("client")

# РЕГЕСТРИРУЕМ КЛИЕНТА.
# data = {
#     'first_name': 'Александр',
#     'last_name': 'Гусевский',
#     'email': 'kolyapolosin85@gmail.com',
#     'password': 'verystrongpassword123',
#     'company': 'Efes',
#     'position': 'manager'
# }
# response = requests.post("http://127.0.0.1:8000/api/v1/user/register", data=data)
# if response.status_code == 200:
#     print("Регистрация прошла успешно:", response.json())
# else:
#     print("Ошибка при регистрации:", response.status_code, response.text)
# ---------------------------------------------------------------------------------------------------------------------
# УДАЛЯЕМ КЛИЕНТА.
# response = requests.delete('http://localhost:8000/api/v1/user/delete/61/')
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# АВТОРИЗУЕМСЯ НА САЙТЕ.
login_data = {
    'email': 'kolyapolosin85@gmail.com',
    'password': 'verystrongpassword123'
}
response = requests.post('http://localhost:8000/api/v1/user/login/', data=login_data)
if response.status_code == 200:
    print("Успешная авторизация")
else:
    print(f"Ошибка авторизации: {response.status_code}")
# ---------------------------------------------------------------------------------------------------------------------
# details
# headers = {"Authorization": "Token <y9812d54dd2f0ceaf51d5355486296202d439f7c32>",}
#
# response = requests.get("http://127.0.0.1:8000/api/v1/user/details", headers=headers)
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# СОЗДАЕМ МАГАЗИН


# ---------------------------------------------------------------------------------------------------------------------
# ДОБАВЛЯЕМ ПРАЙС
# headers = {'Content-Type': 'application/x-yaml'}
# response = requests.post('http://localhost:8000/api/v1/partner/update/, headers, ')
#
# with open('path/to/your/file.yaml', 'r') as file:
#     yaml_content = file.read()
# response = requests.post(url, data=yaml_content, headers=headers)
# print(response.text)

# ---------------------------------------------------------------------------------------------------------------------
# ВЫВЕСТИ ВСЕХ ПОЛЬЗОВАТЕЛЕЙ (для теста)
# response = requests.get('http://localhost:8000/api/v1/user/list/')
# if response.status_code == 200:
#     print("прошла успешно:", response.status_code)
# else:
#     print("Ошибка :", response.status_code)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# ПОДТВЕРЖДАЕМ


