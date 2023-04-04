import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "\chromedriver_win32\chromedriver.exe"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
INITIAL_URL = "https://www.zillow.com"


class WebScraper:
    """web scraper class"""
    def __init__(self, url):
        self.url = url


class SeleniumParser(WebScraper):
    """ Web Scraper class for parsing websites with Selenium"""

    def __init__(self, url):
        super().__init__(url)

    def fill_the_form(self, address_list, price_list, link_list):
        """fills the form with address_list, price_list, link_list as inputs"""
        chrome_options = webdriver.ChromeOptions();
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        chrome_options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER_PATH);
        driver.get(self.url)
        time.sleep(5)

        for i in range(len(address_list)):
            address = driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div["
                          "1]/input")
            price = driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div["
                          "1]/input")
            link = driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div["
                          "1]/input")
            submit = driver.find_element(
                By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")

            address.send_keys(address_list[i])
            price.send_keys(price_list[i])
            link.send_keys(link_list[i])
            time.sleep(0.5)
            submit.click()
            if i < len(address_list) -1:
                time.sleep(1)
                resubmit = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
                resubmit.click()
                time.sleep(3)

        print("Filling the form completed!")


class Soup(WebScraper):
    """ Web Scraper class for parsing html with BeautifulSoup"""
    def __init__(self, url):
        super().__init__(url)
        response = requests.get(url=self.url, headers=header)
        website_html = response.text
        self.soup = BeautifulSoup(website_html, "html.parser")

    def get_links(self, attr):
        """get links of the properties and returns a list of it"""
        link_list = []
        links = self.soup.find_all("a", attr)
        for item in links:
            link = str(item.get("href"))
            if len(link_list) == 0:
                link_list.append(link)
            else:
                link_list.append(f'{INITIAL_URL}{link}')
        return link_list

    def get_prices(self, attr):
        """get prices of the properties and returns a list of it"""
        price_list = []
        prices = self.soup.find_all("span", attr)
        for item in prices:
            price = str(item.text)[:6]
            price_list.append(price)
        return price_list

    def get_address(self, attr):
        """get addresses of the properties and returns a list of it"""
        adr = self.soup.find_all("address", attr)
        address_list = []
        for item in adr:
            address = str(item.text)
            address_list.append(address)
        return address_list
