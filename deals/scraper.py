import requests
from bs4 import BeautifulSoup
import lxml
import json
from .models import Product
from enum import Enum

paknsave_url = 'https://www.paknsaveonline.co.nz/Search?q='

class StoreType(Enum):
    FOOD = 'FOOD',
    ELECTRONICS = 'ELECTRONICS',


class Store:
    name = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept-Language': 'en',
    }
    url = None
    type = None

    # returns a 2-tuple (name, price)
    def scrape_product_data(self, d=1):
        pass

    # save product data as product models
    def save_to_db(self):
        pass


class NewWorld(Store):
    name = 'New World'
    url = 'https://www.newworld.co.nz/shop/Search?q=&ps=50'
    type = StoreType.FOOD

    def scrape_product_data(self, page=1):
        name_and_price = []

        r = requests.get(f'{self.url}&pg={page}', headers=self.headers)

        soup = BeautifulSoup(r.text, "lxml")

        products = soup.select(selector=".js-product-card-footer")
        print(str(len(products)) + "HERE")
        product_data = []

        for product in products:
            if "data-options" in product.attrs:
                product_data.append(json.loads(product["data-options"]))

        for item in product_data:
            name_and_price.append((item['productName'], item['ProductDetails']['PricePerItem']))
        return name_and_price

    def save_to_db(self):
        Product.objects.filter(location=self.name).delete()
        for i in range(1, 21):
            name_price_tuples = self.scrape_product_data(i)
            for item in name_price_tuples:
                name = item[0]
                if len(name) > 50:
                    name = name[:50]
                Product.objects.create(name=name, price=item[1], link='https://www.newworld.co.nz/', location=self.name)


class ComputerLounge(Store):
    name = 'Computer Lounge'
    url = 'https://www.computerlounge.co.nz/ProductCatList.aspx?q='
    type = StoreType.ELECTRONICS

    def scrape_product_data(self, page=1):
        name_and_price = []

        r = requests.get(f'{self.url}&page={page}', headers=self.headers)

        soup = BeautifulSoup(r.text, "lxml")

        products = soup.select(selector=".js-product-data")

        for product in products:
            if "data-name" in product.attrs and "data-price" in product.attrs:
                name_and_price.append((product['data-name'], product['data-price']))
        print(name_and_price)
        return name_and_price

    def save_to_db(self):
        Product.objects.filter(location=self.name).delete()
        for i in range(1, 98):
            print(f'Attempting to scrape page {i}')
            print(f'{self.url}&page={i}')
            name_price_tuples = self.scrape_product_data(i)
            for item in name_price_tuples:
                Product.objects.create(name=item[0], price=item[1], link='https://www.computerlounge.co.nz/', location=self.name)


all_stores = [NewWorld(), ComputerLounge()]

def main():
    pass

if __name__ == "__main__":
    main()