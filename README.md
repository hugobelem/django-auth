> A Django Project. Full user authentication.

## Features
- Django 5.1 & Python 3.12
- User log in/out, sign up, password change/reset
- Custom 400, 403, 404, and 500 error pages
----

## How it was build
- With the help of [LearnDjango](https://learndjango.com)
- Styling with [Bootstrap v5](https://getbootstrap.com/)
- Forms styling with [django-crispy-forms](https://django-crispy-forms.readthedocs.io)
- Custom user created with Django [AbstractUser](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project) class
- Forms created with Django [UserCreationFrom](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#custom-users-and-the-built-in-auth-forms) class
----


### Install

```
$ python -m venv dj

# macOS
$ source dj/bin/activate

(dj) $ pip install -r requirements.txt
(dj) $ python manage.py migrate
(dj) $ python manage.py createsuperuser
(dj) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```
