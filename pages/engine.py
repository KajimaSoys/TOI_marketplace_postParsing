import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def driverwork(querystr):
    page = 1
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    datalist = parsing(querystr, driver, page)
    driver.quit()
    return datalist


def parsing(querystr, driver, page):
    link = 'https://www.ozon.ru/search/?from_global=true&text=' + querystr + '&page=' + str(page)
    driver.get(link)
    #time.sleep(20)
    datalist = []
    div = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a0c6.a0c9.a0c8"))
    )
    div = driver.find_elements_by_class_name('a0c6.a0c9.a0c8')
    for item in div:
        data = []
        provider = 'Отсутствует'
        name = item.find_element_by_class_name('a2g0.tile-hover-target').text
        # noinspection PyBroadException

        if item.find_element_by_class_name('b5v6.b5v7'):
            price=item.find_element_by_class_name('b5v6.b5v7').text
        elif item.find_element_by_class_name('b5v6.b5v7.c4v8'):
            price = item.find_element_by_class_name('b5v6.b5v7.c4v8').text
        elif item.find_element_by_class_name('b5v6.c8c6.c4v8'):
            price = item.find_element_by_class_name('b5v6.c8c6.c4v8').text
        try:
            price = price.replace('\u2009', ' ')
            price = price.replace('&thinsp;', ' ')
        except Exception:
            print('Возникли проблемы c Price')

        #try:
        #    price = item.find_element_by_class_name('b5v6.b5v7.c4v8').text
        #except Exception:
        #    try:
        #        price = item.find_element_by_class_name('b5v6.c8c6.c4v8').text
        #    except Exception:
        #        pass
        #finally:


        url = item.find_element_by_class_name('a0v2.tile-hover-target').get_attribute("href")
        image = item.find_element_by_tag_name("img").get_attribute("src")
        provider = item.find_elements_by_css_selector('div.a0t6 > span')
        for subitem in provider:
            # noinspection PyBroadException
            try:
                provider = subitem.find_elements_by_tag_name('font')[1].text
            except Exception:
                pass
        data.extend([name, price, provider, url, image])
        datalist.append(data)
    return datalist

#querystr=input()
#result=driverwork(querystr)
#print(result)
# driverwork('ночник')
