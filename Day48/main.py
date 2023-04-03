from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


CHROME_DRIVER_PATH = "D:\me\Job\Skill\Code\python\100 Days\myCodes\chromedriver_win32\chromedriver.exe"

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH);

URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)

pos = driver.find_element(By.CLASS_NAME, "fc-button-label")
time.sleep(3)
pos.click()
pos = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
pos.click()
time.sleep(0.5)
pos = driver.find_element(By.ID, "langSelect-EN")
pos.click()
time.sleep(4)


def get_products_price():
    products_price = []
    for i in range(5):
        product = driver.find_element(By.CSS_SELECTOR, f"#productPrice{i}")
        price = str(product.text).replace(',', '')
        if price != '':
            products_price.append(int(price))
    return products_price


def cookie_click(num):
    for _ in range(num):
        cookie_pos.click()


def click_upgrade(product):
    driver.find_element(By.CSS_SELECTOR, f"#product{product}").click()


cookie_pos = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
money = driver.find_element(By.CSS_SELECTOR, "#cookies")

end_game = False
while not end_game:
    cookie_click(100)
    coin = int(money.text.split()[0].replace(',', ''))
    prices = get_products_price()
    try:
        upgrade = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[19]/div[3]/div[5]/div[1]')
        upgrade.click()
    except NoSuchElementException:
        pass

    upgrade_costs = []
    counter = 0
    for price in prices:
        if price <= coin:
            upgrade_costs.append(counter)
        counter += 1
    if len(upgrade_costs) > 0:
        click_upgrade(upgrade_costs[-1])


