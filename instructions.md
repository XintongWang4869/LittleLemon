django-admin startproject littlelemon

cd littlelemon
python3 manage.py runserver

python3 manage.py startapp restaurant

add the app to INSTALLED_APPS in settings.py

push to git



build two APIs. One API to order food using the Menu API. You need to build the Table booking API to facilitate reserving a table for dining in the restaurant on a specific date and for a certain number of people.