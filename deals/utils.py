import requests
from bs4 import BeautifulSoup
import lxml
import json

single_item_url = 'https://www.amazon.com/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/'
new_world_url = 'https://www.newworld.co.nz/shop/Search?q=apple'
pakinsave_url = 'https://www.paknsaveonline.co.nz/Search?q=apple'


def get_single_item_data_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept-Language': 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price


def get_item_search_data_nw(url):
    name_and_price = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept-Language': 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    products = soup.select(selector=".js-product-card-footer")
    product_data = []

    for product in products:
        if "data-options" in product.attrs:
            product_data.append(json.loads(product["data-options"]))

    for item in product_data:
        name_and_price.append((item['productName'], item['ProductDetails']['PricePerItem']))
    return name_and_price

# print(get_item_search_data_nw(new_world_url))
# itemStringNw = ''
# for item in get_item_search_data_nw(new_world_url):
#     itemStringNw += (item['productName'] + " " + item['ProductDetails']['PricePerItem'] + ",")
# print(itemStringNw)
# print(get_item_search_data_nw(pakinsave_url))
# itemStringPak = ''
# for item in get_item_search_data_nw(pakinsave_url):
#     itemStringPak += (item['productName'] + " " + item['ProductDetails']['PricePerItem'] + ",")
# print(itemStringPak)
