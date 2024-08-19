> A Django project exercise. Objetive: user authentication.

## 🚀 Features

- Django 5.1 & Python 3.12
- User log in/out, sign up, password reset
- Styling with [Bootstrap v5](https://getbootstrap.com/)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- Custom 404, 500, and 403 error pages
----

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)

----


### Pip

```
$ python -m venv .dj

# macOS
$ source .dj/bin/activate

(.dj) $ pip install -r requirements.txt
(.dj) $ python manage.py migrate
(.dj) $ python manage.py createsuperuser
(.dj) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```