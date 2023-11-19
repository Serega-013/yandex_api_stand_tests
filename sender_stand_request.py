import requests
import configuration
import data


# создание нового пользователя
def post_new_user(body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())


# Функцию создания нового набора
def post_new_client_kit(kit_body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=data.headers)


print(response.status_code)
