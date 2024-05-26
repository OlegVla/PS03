

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на страницу сайта
    driver.get('https://www.divan.ru/category/divany-i-kresla')

    # Немного подождать, чтобы страница загрузилась
    time.sleep(5)

    # Поиск всех элементов с классом цены
    prices = driver.find_elements(By.CSS_SELECTOR, '.ui-LD-ZU.KIkOH')

    # Вывод цен
    for price in prices:
        print(price.text)

finally:
    # Закрытие драйвера
    driver.quit()

#Этот скрипт:

#1. Инициализирует ChromeDriver с опцией запуска в фоновом режиме.
2#. Переходит на сайт `https://www.divan.ru/category/divany-i-kresla`.
#3. Ждет 5 секунд, чтобы страница полностью загрузилась.
#4. Ищет элементы, содержащие цены на диваны и кресла, с помощью CSS-селектора.
#5. Выводит найденные цены в консоль.
#6. Закрывает браузер.

#Обратите внимание, что при изменении структуры сайта или классов может потребоваться обновить селекторы в коде.