import requests
from urllib.request import urlopen

# Запрашиваем у пользователя почту
#email = input("Введите вашу электронную почту: ")

email = "tdgr4vkfio@waterisgone.com"
#Открываем файл с ссылками
with open('links.txt', 'r') as f:
    # Читаем все ссылки из файла
    for i, link in enumerate(f):
        # Удаляем символ новой строки
        link = link.strip() + email
        try:
        	response = requests.get(link, timeout=7)
        	print(f"Отправил {i+1} запрос")
        except:
        	print("Error")
