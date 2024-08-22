import requests
import json
import yaml
print("client")

# РЕГЕСТРИРУЕМ КЛИЕНТА.
# data = {
#     'first_name': 'Владимир',
#     'last_name': 'Иноземный',
#     'email': 'test@gmail.com',
#     'password': 'verystrongpassword789',
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
# login_data = {
#     'email': 'test@gmail.com',  # kolyapolosin85@gmail.com
#     'password': 'verystrongpassword789'  # verystrongpassword123
# }
# response = requests.post('http://localhost:8000/api/v1/user/login/', data=login_data)
# if response.status_code == 200:
#     print("Успешная авторизация")
# else:
#     print(f"Ошибка авторизации: {response.status_code}")
# ---------------------------------------------------------------------------------------------------------------------
# AccountDetails GET
# response = requests.get("http://127.0.0.1:8000/api/v1/user/details",
#                         params={'email': 'kolyapolosin85@gmail.com',
#                                 'password': 'verystrongpassword123'})
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# AccountDetails POST
# data_new = {
#     'first_name': 'Александр',
#     'last_name': 'Гусевский',
#     'email': 'kolyapolosin85@gmail.com',
#     'password': 'verystrongpassword123',
#     'company': 'Cola',
#     'position': 'director',
#     'VariationUser': 'SHOP_REPRESENTATIVE',
#     'shop_id': '5'
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.post("http://127.0.0.1:8000/api/v1/user/details", json=data_new, headers=headers)
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# Просмотр магазинов.
# response = requests.get("http://127.0.0.1:8000/api/v1/shops")
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# СОЗДАЕМ МАГАЗИН
# data = {
#     'name': 'Coca-Cola',
#     'url': 'http://127.0.0.1:8000/Coca-Cola',
#     'user': '61',
#     'state': 'True',
#     'email': 'kolyapolosin85@gmail.com',
#     'password': 'verystrongpassword123',
# }
# headers = {'Content-Type': 'application/json'}
# response = requests.post("http://127.0.0.1:8000/api/v1/shop/create", json=data, headers=headers)
# print(response.status_code)
# print(response.text)
# ---------------------------------------------------------------------------------------------------------------------
# ПОЛУЧАЕМ ИНФУ О МАГАЗИНЕ
# login_data = {
#     'email': 'test@gmail.com',  # kolyapolosin85@gmail.com
#     'password': 'verystrongpassword789'  # verystrongpassword123
# }
# response = requests.get("http://127.0.0.1:8000/api/v1/user/state")
# print(response.status_code)
# ---------------------------------------------------------------------------------------------------------------------
# ВЫВЕСТИ ВСЕХ ПОЛЬЗОВАТЕЛЕЙ (для теста)
# response = requests.get('http://localhost:8000/api/v1/user/list/')
# if response.status_code == 200:
#     print("прошла успешно:", response.status_code)
# else:
#     print("Ошибка :", response.status_code)
# ---------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------

# ДОБАВЛЯЕМ ПРАЙС
with open('shop1.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)
request_body = {}
if yaml_content is None:
    print("YAML file is empty or invalid.")
else:
    # Преобразование содержимого YAML в JSON
    yaml_data_json = json.dumps(yaml_content, ensure_ascii=False)
    print(yaml_data_json)
    # Дополнительные данные для проверки прав пользователя
    additional_data = {
        'id': '61',
        'first_name': 'Александр',
        'last_name': 'Гусевский',
        'email': 'kolyapolosin85@gmail.com',
        'password': 'verystrongpassword123',
        'company': 'Cola',
        'position': 'director',
        'VariationUser': 'SHOP_REPRESENTATIVE',
        'shop_id': '5',
    }

    # Объединение данных в одно тело запроса
    request_body = {
        'data': yaml_data_json,
        **additional_data
    }

    response = requests.post(
        'http://localhost:8000/api/v1/price/update',
        json=request_body,
        headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print("Data successfully loaded")
    else:
        try:
            print(f"Error loading data: {response.json()}")
        except requests.exceptions.JSONDecodeError:
            print("Сервер ответил пустым телом или неверным JSON..")
# ----------------------------------------------------------------
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


