psa-passwordless
================

Passwordless Email Auth 

How to run this application
---------------------------

1. Create a virtualenv, activate and install dependencies::

    $ virtualenv ~/.virtualenvs/foobar
    $ . ~/.virtualenvs/foobar/bin/activate
    $ pip install -r requirements.txt

2. Initialize the needed settings for sending email::

    $ cd pless
    $ cp app/local_settings.py.template app/local_settings.py
    $ vi app/local_settings.py

3. Syncdb and runserver::

    $ python manage.py syncdb
    $ python manage.py runserver

4. Open your browser at http://localhost:8000 and test it.
