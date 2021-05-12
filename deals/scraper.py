import requests
from bs4 import BeautifulSoup
import lxml
import json
from .models import Product
from enum import Enum

single_item_url = 'https://www.amazon.com/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/'
new_world_url = 'https://www.newworld.co.nz/shop/Search?q='
paknsave_url = 'https://www.paknsaveonline.co.nz/Search?q='
noel_leeming_url = 'https://www.noelleeming.co.nz/search.html?q='


class StoreType(Enum):
    FOOD = 'FOOD',
    ELECTRONICS = 'ELECTRONICS',


class Store:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept-Language': 'en',
    }
    url = None
    data = {}
    type = None

    # returns a 2-tuple (name, price)
    def scrape_product_data(self):
        pass

    # save product data as product models
    def save_to_db(self):
        pass


class NewWorld(Store):
    url = 'https://www.newworld.co.nz/shop/Search?q='
    type = StoreType.FOOD


class NoelLeeming(Store):
    url = 'https://www.noelleeming.co.nz/search.html?q='
    type = StoreType.ELECTRONICS


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


def scrape_all_products():
    Product.objects.all().delete()
    for i in range(1, 51):
        print("Scraping page " + str(i) + " from new world")
        for item in get_item_search_data_nw(new_world_url + '&pg=' + str(i)):
            Product.objects.create(name=item[0], price=item[1], link='https://www.newworld.co.nz/', location='New World')


