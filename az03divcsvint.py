#Конечно! Для обработки данных в CSV файле и удаления строки " руб."
# в конце каждой строки, а также преобразования значений в числовой
# формат, можно использовать следующий код:

import csv

# Чтение данных из исходного CSV файла
with open('prices.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Пропустить заголовок
    prices = []
    for row in reader:
        price_str = row[0].replace(' руб.', '').replace(' ', '')  # Удаление " руб." и пробелов
        price_str = price_str.replace('руб.', '').strip()  # Удаление подстроки 'руб.' и пробелов
        price_num = int(price_str)  # Преобразование в число
        print(price_num)

        prices.append(price_num)

# Запись обработанных данных в новый CSV файл
with open('processed_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Price'])  # Запись заголовка
    for price in prices:
        writer.writerow([price])

print("Данные успешно обработаны и сохранены в файл processed_prices.csv")


#Этот код:
#1. Читает данные из файла `prices.csv`.
#2. Удаляет строку " руб." и пробелы в каждой строке цены.
#3. Преобразует строку цены в целое число.
#4. Записывает обработанные данные в новый CSV файл `processed_prices.csv`.

#Теперь ваши данные будут обработаны и сохранены в новом CSV файле, где
# каждая цена представлена в числовом формате.