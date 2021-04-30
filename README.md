# Deal-Finder - An university project :books:

As a webapp, dealFinder aims to help users to find the best possible food-related deals from nearby stores, allow users to have their own account in which they are able to have a number of budgets, shopping lists, and compare their actual spending (from shopping list) vs their budgets :moneybag: . 

## Technologies used:
 * Django 3.2
 * Python 3.9, SQL
 * HTML, CSS, JavaScript
 * SourceTree, and gitHub desktop. 


### The team :woman_technologist::man_technologist:
Five enthusiastic software engineering students 

### Development 
In process - please see the developing branch [here](https://github.com/NihalKPatel/Deal-Finder/tree/developer). 

##How to run from new environment
1. python -m pip install -r requirements.txt - to install the dependencies required to run this project
1. python manage.py migrate - migrates changed from django migrations to your local database
2. python manage.py createsuperuser - program requires a superuser to access the staff page and scrape product records 
3. visit http://127.0.0.1:8000/deals/staff/ after logging in to admin superuser and scrape product data (may take a while)
