import time
from selenium import webdriver


def driverwork(querystr):
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    datalist=parsing(querystr, driver)
    driver.quit()
    return datalist


def parsing(querystr, driver):
    link = 'https://www.ozon.ru/search/?from_global=true&text=' + querystr
    driver.get(link)
    time.sleep(3)
    datalist = []
    div = driver.find_elements_by_class_name('a0c6.a0c9.a0c8')
    for item in div:
        data = []
        provider = 'Отсутствует'
        name = item.find_element_by_class_name('a2g0.tile-hover-target').text
        # noinspection PyBroadException
        try:
            price = item.find_element_by_class_name('b5v6.b5v7.c4v8').text
        except Exception:
            price = item.find_element_by_class_name('b5v6.b5v7').text
        finally:
            price = price.replace('\u2009', ' ')
        price = price.replace('&thinsp;', ' ')
        url = item.find_element_by_class_name('a0v2.tile-hover-target').get_attribute("href")
        image = item.find_element_by_tag_name("img").get_attribute("src")
        provider = item.find_elements_by_class_name('a2g6')
        for subitem in provider:
            # noinspection PyBroadException
            try:
                provider = subitem.find_element_by_tag_name('font').text
            except Exception:
                pass
        data.extend([name, price, provider, url, image])
        datalist.append(data)
    return datalist


# driverwork('ночник')
