# grocery-dev-py
Sample Django project for CS451

# Setup after cloning?
You will need run ```python manage.py migrate``` to create the base database, its tables, and the app specific tables.

To use the admin, you'll need to create a local superuser account: ```python manage.py createsuperuser``` The credentials you provide are only relevant to your local working sqlite database. This database is **ignored** by git so it will not be located in the public repository.


# Pulling changes from other team members?
If they made changes to the models, you'll need to run ```python manage.py migrate``` to register db modifications in your local working db. 
