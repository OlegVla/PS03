
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time


def fetch_divan_data(url):
    # Если мы используем Chrome, пишем
    driver = webdriver.Chrome()

    # В отдельной переменной указываем сайт, который будем просматривать
    url = "https://www.divan.ru/category/divany-i-kresla"

    # Открываем веб-страницу
    driver.get(url)

    # Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
    time.sleep(3)


    data = []

    try:
        # Подождем, чтобы страница полностью загрузилась
        time.sleep(3)

        # Здесь мы предполагаем, что на странице divan.ru есть элементы с классом 'product-name' для
        # названия и 'price' для цены
        products = driver.find_elements(By.CLASS_NAME, "Pk6w8")

        for product in products:
            try:
                name = product.find_element(By.CSS_SELECTOR, 'div.c9h0M').text
                print(name)
                price = product.find_element(By.CSS_SELECTOR, 'div.lsooF').text

                data.append([name, price])
            except Exception as e:
                print(f"Error parsing product: {e}")

    finally:
        # Закрытие браузера
        driver.quit()

    return data


def save_to_csv(data,filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price'])  # Заголовки столбцов
        writer.writerows(data)


def main():
    url = 'https://divan.ru/category/divany-i-kresla'  # Замените на нужный URL
    data = fetch_divan_data(url)
    print(data)
    save_to_csv(data,'divans.csv')
    print("Data has been saved to divans.csv")



if __name__ == "__main__":
    main()
