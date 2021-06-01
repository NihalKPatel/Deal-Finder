# Deal-Finder - An university project :books:

DealFinder is a user focused webapp. The description bellow is instented to people would like to use DealFinder in future stages of Spring 3. To work in this project we follow scrum as our agile methology. 

## Technologies used:
 * Django 3.2
 * Python 3.9, SQL
 * HTML, CSS, JavaScript, bootstrao.
 * SourceTree, and gitHub desktop. 
 * See the requirements.txt file for all dependencies 

### Some of the implemented features :arrow_down:

  * Create your own profile, and upload your own photo! 
  
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/profile.png)
    
  * Create a shopping list 
  
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/creating%20a%20shoppingList.png)
    
  * Customise your own budget!
  
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/budget%20standardUserView.png)
  
  * Find your nearest New World supermarket
  
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/map.png)
    
  * Find a product from New World!
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/findingProducts%20from%20supermarket.png)
    
  * Use our budget calculator to help you organizing your expenses
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/calculator.png)
    
  * Do you have a question? - check out our FAQ page
    ![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/FAQ.png)
    
    
These are just some of the few things that DealFinder can do! If you have any suggestions don't forget to use our suggestion form. 


### The team :woman_technologist::man_technologist:
DealFinder was created in a collaboration of five team members :arrow_down:

![](https://github.com/NihalKPatel/Deal-Finder/blob/main/imagesReadMe/readme%20about%20us.png)

### Development 
Currently at spring 2 - please see the main branch [here](https://github.com/NihalKPatel/Deal-Finder/tree/main). 
In future springs, we aim to have more user-focused features. 

### How to run from new environment
1. python -m pip install -r requirements.txt - to install the dependencies required to run this project
1. python manage.py migrate - migrates changed from django migrations to your local database
2. python manage.py createsuperuser - program requires a superuser to access the staff page and scrape product records 
3. visit http://127.0.0.1:8000/deals/staff/ after logging in to admin superuser and scrape product data (may take a while)
