**THIS PROJECT IS OUTDATED.** The CREST API was discontinued.

# django-crest-example
This is an example for a simple Django App with EVE Online Single Sign-On (SSO) and authenticated CREST access.
It depends on [Python Social Auth](http://psa.matiasaguirre.net/) to integrate EVE SSO with Django's builtin user authentication system and uses [PyCrest](https://forums.eveonline.com/default.aspx?g=posts&t=398676) to interact with the CREST API.

## Live Demo
A live demo is not available anymore, since CREST is discontinued.

## Getting started
If you want to try it out on your own server, loosely follow these steps:

1. Get the code:
  ```bash
  git clone https://gitlab.com/flesser/django-crest-example.git
  ```

2. Install dependencies (mainly [PyCrest](https://github.com/Dreae/PyCrest) and [Python Social Auth](https://github.com/omab/python-social-auth)):
  ```bash
  pip install -r requirements.txt
  ```

3. Register a new application on https://developers.eveonline.com/applications
  - choose name and description as you like
  - for *Connection Type* select **CREST Access**
  - in *Permissions* add **publicData** to the Requested Scopes List
  - as *Callback URL* use `http://your-server.com/complete/eveonline/` (or `http://localhost:8000/complete/eveonline/` if you're using the Django development server)

4. edit `example/settings.py` and enter your application's Client ID and Secret Key:
  ```python
  SOCIAL_AUTH_EVEONLINE_KEY = '<Your EVE CREST Application Key>'
  SOCIAL_AUTH_EVEONLINE_SECRET = '<Your EVE CREST Application Secret>'
  ```

5. initialize the database:
  ```bash
  python manage.py migrate
  ```

6. run development server:
  ```bash
  python manage.py runserver
  ```

7. point your browser to [http://localhost:8000/](http://localhost:8000/)

8. ???

9. Profit!
