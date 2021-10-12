# MTG-Tracker

## 1) Introduction

With this Django application you can import your MTG (magic:the gathering) draft results either manually or from an Excel file. You can also modify delete your data if you want.

## 2) Creating your virtual environnement

First of all, you need to have **Python version 3.6** or plus and the package manager **pip**. It is recommended to use a virtual environnement in order to launch this application on your machine. This allows to install only the dependecies required by the application without affecting your external environnement. To create your virtual environnement (venv) you can use this command:

`python3 -m venv <folder_name>`

Then make sure to activate your virtual environnement with this command :

`source <folder_name>/bin/activate`

## 3) Installing the packages

Now that our virtual environnement is ready we can install all the packages necessary by using this command:

`python3 -m pip install -r requirements.txt`

## 4) Connecting to the database

In order to connect to the databse you created you will need to enter the infos of your database in the **mysite/mysite/settings.py** on this line:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '127.0.0.1',
        'PORT': '<port_number>',
    }
}`

Now that your application is connected to your database you can create the tables by applying the migrations:

`python3 manage.py migrate`

## 5) Generating a secret key

You will need to generate a secret key to enter in your **settings.py**. In order to do that you can use the function provided by Django : `django.core.management.utils.get_random_secret_key()` 

## 6) Starting the server

To launch the server provided by Django run this command you can choose a different port number than 8000:

`python3 manage.py runserver 8000`

You can now access the application by typing this address in your browser : 

`localhost:8000`