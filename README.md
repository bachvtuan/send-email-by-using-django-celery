send-email-by-using-django-celery
=================================

This repository demonstrate how to using django celery to send a email, so you don't need wating for email is sent before inform the result.

## How to deploy
### Below is short guide

1. Install django
2. Install djano-celery by using pip

 ```sudo pip install django-celery```
3. Install redis

 ```
sudo apt-get install redis
sudo pip install redis
```

3. Here is the full guide to integrate celery to django [link](https://pypi.python.org/pypi/django-celery) and [here](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

5.  Next, you need input smtp in settings.py. I inputed dumy data like this.

 ```
SMTP_SERVER = "your.smtpserver.domain"
SENDER =     "sender@yourdomain.com"
EMAIL_USERNAME = "smtpuser@domain.com"
EMAIL_PASSWORD = "smtppassword" 
```
6. Run code by using 2 below commands( seperate in 2 windows )

 ```
python manage.py runserver
celery -A app worker -l info
```
