import requests


# assert <условие>, <кастомное сообщение об ошибке>

response = requests.get("https://evilinsult.com/generate_insult.php")

assert response.status_code == 200, "Запрос на получение оскорбления сломан"

print(response.text)

response = requests.get("https://evilinsult.com/generate_insult.ph")

assert response.status_code == 200, "Запрос на получение оскорбления сломан"

print(response.text)


assert 2 == 2, "Ошибка" # Пример 1

assert "Hello" in "Hello, world", "Текст не содержится в строке"

assert "Hello" in " world", "Текст не содержится в строке"

assert 10 == 5, "Ошибка, 10 != 5" # Пример 2

assert 10 == 10 # Пример 3 (без сообщения об ошибке)

assert response.status_code == 200, "Ошибка" # Пример 4
