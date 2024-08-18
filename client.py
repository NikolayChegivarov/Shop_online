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
# response = requests.delete('http://localhost:8000/api/v1/user/delete/24/')
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
    login_response_json = response.json()
    if 'Token' in login_response_json:
        print(f"Полученный токен: {login_response_json['Token']}")
    else:
        print("Токен не найден в ответе.")
else:
    print(f"Ошибка авторизации: {response.status_code}")
# ---------------------------------------------------------------------------------------------------------------------
# details
# response = requests.get("http://127.0.0.1:8000/api/v1/user/details")
# if response.status_code == 200:
#     print("Регистрация прошла успешно:", response.json())
# else:
#     print("Ошибка при регистрации:", response.status_code, response.text)
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

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------
# ПОДТВЕРЖДАЕМ


