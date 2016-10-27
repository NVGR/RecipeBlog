# create a virtualenv
virtaulenv recipe_env

# activate virtualenv
source recipe_env/bin/activate

# Install required packages
pip install -r requirements.txt

# Create Database & User
# If you are planning to use different DB credentials update my.cnf file

create DATABASE recipedb;
CREATE USER 'recipeuser'@'localhost' IDENTIFIED BY 'recipeowd';
GRANT ALL PRIVILEGES ON recipedb.* TO 'recipeuser'@'localhost';
flush PRIVILEGES;

# DB Migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic


User Guide:
     To create a new Recipe user must logged in
        In My Recipe tab there is an option to Create Recipe
        
     We have two tabs one is Home tab which displays all posts, My Recipe Tab which displays user posted Recipes.


Things covered in this app:
    Django in built Authentication
    Generic & Functional views
    Django Models with One-to-many mapping
    Template Inheritance
    Django apps
    Dynamic URL
    Django Pagination
    Django Search
    Django Models & Forms
    Django Messaging
    Register Models in Django Admin
    Django Migrations
    Django builtin Template tags & Filters
    Jinja Template
    Mysql DB
    Bootstrap

