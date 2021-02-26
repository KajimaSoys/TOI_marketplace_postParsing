from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#подключаем ХромДрайвер
options = webdriver.ChromeOptions() 
#options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser")#Стандартное место загрузки
driver = webdriver.Chrome(options=options)# путь к драйверу chrome

#querystr=input()
#link='https://www.ozon.ru/search/?from_global=true&text='+querystr
link='https://www.ozon.ru/search/?from_global=true&text=ночник'

#Делаем запрос на сайт
driver.get(link)
time.sleep(3)
div=driver.find_elements_by_class_name('a0c6.a0c9.a0c8')
i=1
for item in div:
    name=item.find_element_by_class_name('a2g0.tile-hover-target').text
    try:
        price=item.find_element_by_class_name('b5v6.b5v7.c4v8').text
    except Exception:
        price=item.find_element_by_class_name('b5v6.b5v7').text
    price=price.replace('&thinsp;',' ')
    url=item.find_element_by_class_name('a0v2.tile-hover-target').get_attribute("href")
    image = item.find_element_by_tag_name("img").get_attribute("src")
    print(str(i))
    i=i+1
    print(name)
    print(price)
    print(url)
    print(image)
    print()


print('Конец')
#Задаем задержку, чтобы файл успел скачаться
time.sleep(60)
#Выходим из драйвера
driver.quit()

