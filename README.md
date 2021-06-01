# Deal-Finder - An university project :books:

DealFinder is a user focused webapp. The description bellow is instented to people would like to use DealFinder in future stages of Spring 3. To work in this project we follow scrum as our agile methology. 

## Technologies used:
 * Django 3.2
 * Python 3.9, SQL
 * HTML, CSS, JavaScript, bootstrao.
 * SourceTree, and gitHub desktop. 
 * See the requirements.txt file for all dependencies 

### The team :woman_technologist::man_technologist:
DealFinder was created in a collaboration of five team members :arrow_down:

![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/readme%20about%20us.png)

### Development 
Currently at spring 2 - please see the main branch [here](https://github.com/NihalKPatel/Deal-Finder/tree/main). 
In future springs, we aim to have more user-focused features. 

### How to run from new environment
1. python -m pip install -r requirements.txt - to install the dependencies required to run this project
2. python manage.py migrate - migrates changed from django migrations to your local database
3. python manage.py createsuperuser - program requires a superuser to access the staff page and scrape product records 
4. visit http://127.0.0.1:8000/deals/staff/ after logging in to admin superuser and scrape product data (may take a while)

### How to setup scheduled weekly budgets
1. Firstly install RabbitMQ message broker from https://www.rabbitmq.com/download.html
2. run the worker with the following: celery -A dealfinder worker -l info --pool=solo
3. run the beat scheduler with: celery -A dealfinder beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
