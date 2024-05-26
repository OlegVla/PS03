

#Есть сайт “циан”, на котором мы можем снимать или покупать квартиры.Нам нужно
#спарсить цены и с``-*оставить график этих цен.   Заходим в  Нейрокота и
# отправляем запрос:  ✍напиши  код  с  использованием  библиотеки selenium для
# парсинга  цен  с  сайта[сайт]
# 2. Копируем код, вставляем в файл и удаляем  лишнее.
#3.  Отправляем запрос: ✍измени данный код так, чтобы информация о ценах
# сохранялась в csv файл
#4. Копируем нужную часть кода, вставляем в файл.  Создаём файл с ценами:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Импортируем модуль CSV
import csv

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

# URL страницы
url = 'https://www.divan.ru/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "span.ui-Ld-ZU.KIkOH")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

#Сейчас цены находятся в файле.Но всё написанное считается текстом.Нам нужно убрать
# нечисловую часть и преобразовать числа в числовой формат.
# Создаём отдельный файл. Отправляем Нейрокоту запрос:
# ✍🏻 Нужно обработать данные в csv файле, нужн убрат в конце каждой строчки ₽ / мес.и
#реобразовать   тип данных число
#апиши код на Python
#3 Вставляем и проверяем код:
import csv

def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace(' ₽/мес.', '').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")

#оздаё график  Создаём новый файл. Отправляем Нейрокоту запрос: # ✍Нужно
#остроить график гистограмму для получившихся цен из файла# ”cleaned_prices.csv” с
#спользованием модул matplotlib
#3 Вставляем и проверяем код:
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению


# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()