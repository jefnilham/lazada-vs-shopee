from xml.sax import default_parser_list
import pandas as pd
from optparse import Option
from ssl import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


# user to input search item
item_to_search = input('Enter item to compare: ')

# settings for chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# scraping lazada
lazadasg_url = 'https://www.lazada.sg/catalog/?q=' 
full_lazadasg_url = lazadasg_url + item_to_search
driver.get(full_lazadasg_url)
sleep(5)

# from inspect element
item_to_search_name = driver.find_elements(by=By.CLASS_NAME, value='RfADt')
item_to_search_price = driver.find_elements(by=By.CLASS_NAME, value='aBrP0')
item_to_search_rating = driver.find_elements(by=By.CLASS_NAME, value='qzqFw')

# initializing for lazada
item_to_search_name_list = []
item_to_search_price_list = []
item_to_search_rating_list = []
item_to_search_source_list = []

# iterating thru search objects
for name in item_to_search_name:
    item_to_search_name_list.append(name.text)
    item_to_search_source_list.append("Lazada")

for price in item_to_search_price:
    item_to_search_price_list.append((price.text).lstrip("$"))

for rating in item_to_search_rating:
    item_to_search_rating_list.append(int((rating.text).lstrip("(").rstrip(")")))

# create dataframe for lazada scraped info
dfLazada = pd.DataFrame(zip(item_to_search_name_list, item_to_search_price_list, item_to_search_rating_list, item_to_search_source_list), columns=['Item Name', 'Price', 'Ratings', 'Source'])



# scraping shopee
shopeesg_url = 'https://shopee.sg/search?keyword='
full_shopeesgurl = shopeesg_url + item_to_search
driver.get(full_shopeesgurl)
sleep(5)

# from inspect element
item_to_search_name = driver.find_elements(by=By.CLASS_NAME, value='ZG__4J')
item_to_search_price = driver.find_elements(by=By.CLASS_NAME, value='_3c5u7X')
item_to_search_sold = driver.find_elements(by=By.CLASS_NAME, value='_1uq9fs')

# reinitialize for shopee
item_to_search_name_list = []
item_to_search_price_list = []
item_to_search_sold_list = []
item_to_search_source_list = []

# iterating thru search objects
for name in item_to_search_name:
    item_to_search_name_list.append(name.text)
    item_to_search_source_list.append("Shopee")

for price in item_to_search_price:
    item_to_search_price_list.append(price.text)

for sold in item_to_search_sold:
    sold_final = sold.text
    if 'k sold' in sold_final:
        sold_final = (sold_final.replace(".", "").replace("k sold", "")) + "00"
        sold_final = int(float(sold_final))
        item_to_search_sold_list.append(sold_final)
    elif ' sold' in sold_final:
        sold_final = sold_final.replace(" sold", "")
        sold_final = int(float(sold_final))
        item_to_search_sold_list.append(sold_final)
    else:
        item_to_search_sold_list.append(0)

# create dataframe for lazada scraped info
dfShopee = pd.DataFrame(zip(item_to_search_name_list, item_to_search_price_list, item_to_search_sold_list, item_to_search_source_list), columns=['Item Name', 'Price', 'Sold', 'Source'])

# Popularity ranking: sort by ratings for lazada and sold amount for shopee 
dfLazada = dfLazada.sort_values("Ratings", ascending=False)
dfShopee = dfShopee.sort_values("Sold", ascending=False)

# add ranking column and sort by increasing ranks
dfLazada["Rank"] = dfLazada["Ratings"].rank(ascending=False)
dfShopee["Rank"] = dfShopee["Sold"].rank(ascending=False)

# append shopee df to lazada df and rank again
dfFull = pd.concat([dfLazada, dfShopee], axis=0, join='inner')
dfFullSorted = dfFull.sort_values("Rank", ascending=True).reset_index(drop=True)
print(dfFullSorted)