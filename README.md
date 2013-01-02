django-instagram-uid
====================

Instagram User ID Lookup for Django

## Overview

This is the codebase for the Instagram User ID application, written for Django, located [here](http://instagram-uid.herokuapp.com/). It includes a basic implementation of the Instagram API and can be modified and expanded to utilize the full functionality of the API. 

This application adheres to generally accepted Django 1.4 best practices and works both with and without Javascript. As-is, this codebase is ready for deployment both locally and can be deployed to Heroku by adding a [Procfile](https://devcenter.heroku.com/articles/django#declare-processes).

[See this application written for Rails](http://www.github.com/zeantsoi/rails-instagram-uid).

## Dependencies

This application utilizes the [python-instagram](https://github.com/Instagram/python-instagram) library by Instagram, which in turn utilizes other dependencies, including [httplib2](http://code.google.com/p/httplib2/). JSON is parsed using the [simplejson](https://github.com/simplejson/simplejson) Python library.

    # Sample requirements.txt
    
    Django==1.4.3
    Jinja2==2.6
    Werkzeug==0.8.3
    dj-database-url==0.2.1
    httplib2==0.7.7
    psycopg2==2.4.6
    python-instagram==0.8.0
    simplejson==2.6.2
    wsgiref==0.1.2

## Usage

This application requires an Instagram access token, which is available by registering for [an Instagram developer's account](http://instagram.com/developer/register/). Your access token can be passed to the application either during your lookup request or by modifying the Instagram initializer file.

    # django_instagram_uid/settings.py
    
    INSTAGRAM_ACCESS_TOKEN = 'YOUR INSTAGRAM ACCESS TOKEN'
    
## License

Copyright (c) 2013 Zean Tsoi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.