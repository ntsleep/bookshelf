#Bookshelf
Application written in Django for organizing read books.

##Pre-Installation
Enable russian locale
For Debian:
* uncomment ```ru_RU.UTF-8``` in ```/etc/locale.gen```
* run ```sudo locale-gen```

##Installation
* enter project directory
* run ```pip install -r requirements.txt```
* run ```python manage.py makemigrations```
* run ```python manage.py migrate```
* run project ```python manage.py runserver```