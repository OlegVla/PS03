
import matplotlib.pyplot as plt
import csv


# Функция для очистки и преобразования строки цены в число
def clean_price(price_str):
    # Удаление подстроки 'руб.' и пробелов
    price_str = price_str.replace('руб.', '').strip()
    # Преобразование строки в целое число
    return int(price_str)


# Путь к файлу
file_path = 'processed_prices.csv'

# Список для хранения цен
prices = []

# Чтение данных из CSV файла
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Предполагается, что цена находится в первой колонке
        price_str = row[0]
        try:
            price = clean_price(price_str)
            prices.append(price)
        except ValueError:
            # Игнорируем строки, которые не могут быть преобразованы в число
            pass

# Построение гистограммы
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()


### Пояснения:
#1. ** Импортирование модулей **: - `matplotlib.pyplot` для
# построения графиков.    - `csv` для чтения данных из CSV файла.

#2. ** Функция `clean_price` **: - Эта функци  принимает строку
# цены, удаляет подстроку 'руб.'и пробелы, и затем преобразует
# очищенную строку в целое число.

#3. ** Чтение данных из CSV файла **: - Открываем CSV файл и
# читаем  его построчно. - Для каждой строки первая колонка
# (предполагается, что в ней содержится цена) проходит через
# функцию `clean_price`. - Если преобразование успешно, цена
# добавляется  в список `prices`.Если нет, строка игнорируется.

#4. ** Построение  гистограмм
