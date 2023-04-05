from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def handler(site):
    print(f"Обработка поста {site}")
    driver.get(site)
    try:
        search_button = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[2]/div[5]/div[2]/button[2]')
        search_button.click()
        print(f"{site} - Успешно зарегестрированы в розыгрыше!")
        pass
    except Exception as err:
        try:
            search_button = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[2]/div[7]/div[2]/button[2]')
            search_button.click()
            print(f"{site} - Успешно зарегестрированы в розыгрыше!")
            pass
        except:
            print(f"{site} - Поиск кнопки провалился!")

def start():
    try:
        driver.get("https://scrap.tf/raffles")
        time.sleep(3)
    except:
        print("какая то ошибка которую я фиксил и не пофиксил!(НЕ КРИТИЧНО)") #Аня я буду любить тебя вечно, даже в другой жизни найду и полюблю!
    for j in range(4):
        driver.execute_script("window.scrollBy(0,10000)","")
        time.sleep(2)
    m = 1
    result = []
    while True:
        try:
            post_search = driver.find_element(By.XPATH, f'//*[@id="raffles-list"]/div[{m}]/div[1]/div[1]/a')
            result.append(post_search.get_attribute("href"))
            m = m + 1
        except Exception as error:
            print(f"Массив собран! Всего ссылок - {len(result)}\nДебагер сбора: {error}")
            m = 1
            break
    x = 0
    while True:
        try:
            target = result[x]
            handler(target)
            time.sleep(5)
            x = x + 1
        except Exception as debug:
            if x == len(result):
                print(f"Обработано ссылок: {x}/{len(result)}")
                print("Ухожу в сон на 30 сек")
                time.sleep(30) #Тут можете указать время отдыха между обновлениями страницы в секундах
                start()
            else:
                print(f"Ошибка!\nДебагер: {debug}")
                x = x + 1
                
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(f"--user-data-dir=C:/Users/User404/Desktop/proxy/Users") #Тут путь до папки Users где будут храниться данные браузера 
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36") #Тут заполните useragent
try:
    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe') #Тут путь до файла драйвера
except:
    print("Где то ошибка!\nВозможно нет драйвера или ошибка пути")
    exit()

start()