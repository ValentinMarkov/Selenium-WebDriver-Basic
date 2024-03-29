import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

# Some basic navigation to www.amazon.com

# Create driver instance
service = Service('C:\\Users\\ValMar\\Downloads\\chromedriver.exe')
# service = Service('C:\\Users\\Lenovo\\Downloads\\chromedriver.exe')

driver = webdriver.Chrome(service=service)
url = "https://www.amazon.com"
driver.maximize_window()
driver.get(url)


def write_up_item_title(up_int):
    """Create new txt file with test result"""
    fp = open('amazon_reports/' + datetime.datetime.now().strftime("%Y-%m-%d - %H.%M.%S") + '.txt', 'w+', encoding="utf-8")
    count = 0
    for i in up_int:
        count += 1
        fp.write(f'{count}. {i}\n')
        fp.write('---' * 20)
        fp.write('\n')
    fp.close()


search_field = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
search_field.send_keys("mouse")

search_btn = driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button')
search_btn.click()

list_of_items = driver.find_elements(By.CSS_SELECTOR, '.s-main-slot .s-result-item span.a-size-medium')

title_list = []
for item in list_of_items:
    title_list.append(item.text)

write_up_item_title(title_list)

driver.quit()
