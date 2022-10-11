from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import parametros_airbnb
import time

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def search_url(destination, checkin_date, checkout_date, adults, children):
    url = "https://www.airbnb.com/s/"
    url+= destination.replace(" ","-").replace(",","--") + "/"
    url+= "homes?"
    url+= "checkin="+checkin_date+"&"
    url+= "checkout="+checkout_date+"&"
    url+= "adults="+adults+"&"
    url+= "children"+children
    return url

target = search_url(parametros_airbnb.destination, parametros_airbnb.checkin_date, parametros_airbnb.checkout_date, parametros_airbnb.adults, parametros_airbnb.children)
print(target)

driver.get(target)

time.sleep(2)


filter_but = driver.find_element(by = By.CLASS_NAME, value='v4b1g6f')
filter_but.click()
promedio_por_noche = driver.find_element(by = By.CLASS_NAME, value='s1kx2c1w').text
print(promedio_por_noche)

driver.quit()