#Конечно! Давайте изменим код так, чтобы информация о ценах сохранялась в CSV файл. Для этого нам понадобится библиотека `csv`, которая входит в стандартную библиотеку Python, поэтому вам не нужно устанавливать ее отдельно.

#Вот обновленный код:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv


# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу сайта
    driver.get('https://www.divan.ru/category/divany-i-kresla')

    # Немного подождать, чтобы страница загрузилась
    time.sleep(3)

    # Поиск всех элементов с классом цены
    prices = driver.find_elements(By.CSS_SELECTOR, '.ui-LD-ZU.KIkOH')

    # Открыть CSV файл для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Запись заголовка

        # Запись цен в CSV файл
        for price in prices:
            writer.writerow([price.text])

    print("Цены успешно сохранены в файл prices.csv")

finally:
    # Закрытие драйвера
    driver.quit()

#1. Использует библиотеку `csv` для записи данных.
#2. Открывает CSV файл `prices.csv` в режиме записи.
#3. Записывает заголовок столбца.
#4. Записывает каждую цену в отдельную строку CSV файла.
#5. Закрывает файл после записи.

#Теперь информация о ценах будет сохранена в файл `prices.csv`
# в той же директории, где находится ваш скрипт. Вы можете открыть
# этот файл с помощью любого текстового редактора или программы
# для работы с таблицами, такой как Microsoft Excel или Google Sheets.