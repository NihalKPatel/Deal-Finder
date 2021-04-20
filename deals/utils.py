import requests
from bs4 import BeautifulSoup
import lxml

single_item_url = 'https://www.amazon.com/PlayStation-5-DualSense-Wireless-Controller/dp/B08H99BPJN/'
item_search_url = 'https://www.amazon.com/s?k=controller'


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


def get_item_search_data_amazon(url):
    product_list = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept-Language': 'en',
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select(selector=".s-result-item")
    price = soup.select(selector=".s-result-item .a-offscreen")

    for i in range(len(name)):
        # if name[i].attrs["data-component-type"] == 's-search-result':
        if "data-component-id" in name[i].attrs:
            print(name[i].select_one(selector='.a-text-normal').getText())
        print()
    # for i in range(len(price)):
    #     product = {
    #         'name': name[i],
    #         'price': price[i],
    #     }
    #     product_list.append(product)
    return name


print(get_item_search_data_amazon(item_search_url))

# print(get_single_item_data_amazon(url))
