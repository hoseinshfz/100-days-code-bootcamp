from web_scraper import Soup, SeleniumParser

ZILLOW_URL = "https://www.zillow.com/new-york-ny/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.917577%2C%22east%22%3A-73.700272%2C%22south%22%3A40.477399%2C%22west%22%3A-74.25909%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%7D"
FORM_URL = "THE FORM URL"

LINK_ATTR = {"data-test": "property-card-link", "tabindex": "0"}
PRICE_ATTR = {"data-test": "property-card-price"}
ADDRESS_ATTR = {"data-test": "property-card-addr"}

# Scrape the website for rental properties and their price, locations, and links

web_scraper_rent = Soup(ZILLOW_URL)

price_list = web_scraper_rent.get_prices(PRICE_ATTR)
link_list = web_scraper_rent.get_links(LINK_ATTR)
address_list = web_scraper_rent.get_address(ADDRESS_ATTR)

# print(price_list)
# print(link_list)
# print(address_list)

# fill the form with extracted information

form_filler = SeleniumParser(FORM_URL)
form_filler.fill_the_form(address_list, price_list, link_list)
