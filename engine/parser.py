from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#подключаем ХромДрайвер
options = webdriver.ChromeOptions() 
options.add_argument("download.default_directory=D:\Учеба\АИС\torgi_parser")#Стандартное место загрузки
driver = webdriver.Chrome(options=options,executable_path=r'C:\Users\Kajima\chromedriver.exe')# путь к драйверу chrome

querystr=input()
link='https://www.ozon.ru/search/?from_global=true&text='+querystr

#Делаем запрос на сайт
driver.get(link)



#Задаем задержку, чтобы файл успел скачаться
time.sleep(20)
#Выходим из драйвера
driver.quit()

