import data
import sender_stand_request


# Изменение параметра firstname
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Изменение тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


# Создание 'authToken'
def get_new_client_token(first_name):
    user_body = get_user_body(first_name)
    client_response = sender_stand_request.post_new_client_kit(user_body)
    return client_response


# Позитивные проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name


# Негативные проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


data.headers["Authorization"] = f"Bearer {get_new_client_token}"


# тест 1 Допустимое количество символов 1
def test_1_letter_in_name_positive():
    positive_assert("a")


# тест 2 Допустимое количество символов 511
def test_511_letter_in_name_positive():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# тест 3 Количество символов меньше допустимого 0
def test_zero_letter_in_name_negative():
    negative_assert_code_400("")


# тест 4 Количество символов больше допустимого 512
def test_512_letter_in_name_negative():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# тест 5 Разрешены английские буквы
def test_eng_letter_in_name_positive():
    positive_assert("QWErty")


# тест 6 Разрешены русские буквы
def test_rus_letter_in_name_positive():
    positive_assert("Мария")


# тест 7 Разрешены спецсимволы
def test_specsymbols_in_name_positive():
    positive_assert(""'@-№%'"")


# тест 8 Разрешены пробелы
def test_space_in_name_positive():
    positive_assert("Человек и КО")


# тест 9 Разрешены цифры
def test_numbers_in_name_positive():
    positive_assert("123")


# тест 10 Параметр не передан в запросе
def test_no_parameter_in_request_name_negative():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


# тест 11 Передан другой тип параметра (число)
def test_other_parameter_type_in_name_negative():
    negative_assert_code_400(123)
