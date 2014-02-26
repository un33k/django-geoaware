Django GeoAware Application
====================

A Django application that can include GeoIP related info in the session and/or the context of your application.

**Author:** Val Neekman, [ info@neekware.com, @vneekman]

Overview
========

Django GeoAware provides a middleware as well as a context processor for including
GeoIP related info in the session and/or the context of your application.

How to install
==================

    **Prerequisites:**
    
    Please ensure that you have properly configured your system as per:
    https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/
    
    **Install**
    1. easy_install django-geoaware
    2. pip install django-geoaware
    3. git clone http://github.com/un33k/django-geoaware
        a. cd django-geoaware
        b. run python setup.py
    4. wget https://github.com/un33k/django-geoaware/zipball/master
        a. unzip the downloaded file
        b. cd into django-geoaware-* directory
        c. run python setup.py

How to use
=================


Include 'geoware' in your `INSTALLED_APPS` somewhere after `'django.contrib.gis'`.

   ```python
   INSTALLED_APPS = [
      'some apps go here',
      'django.contrib.gis',
      'some other apps can go here',
      'geoaware',
      'some other apps can go here',
   ]
   ```

To include GeoIP related info in the session:
    
    Include geoaware middleware in your `MIDDLEWARE_CLASSES` after the session middleware.

   ```python
   MIDDLEWARE_CLASSES = [
      'django.middleware.common.CommonMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'some middleware can go here',
      'geoaware.middleware.GeoAwareSessionMiddleware',
      'some more middleware can go here',
   ] 
   # The GeoIP related info would be available in request.session['geo_info']
   ```

To include GeoIP related info in the context:
    
   Include geoware context processor in your `TEMPLATE_CONTEXT_PROCESSORS` after `'django.core.context_processors.request'`.
   
   ```python
   TEMPLATE_CONTEXT_PROCESSORS = [
      'django.contrib.auth.context_processors.auth',
      'some context processor can go here',
      'django.core.context_processors.request',
      'some context processor can go here',
      'geoaware.context_processors.geoaware',
      'some context processor can go here',
   ]
   # The GeoIP related info would be available in your context as geo_info.
   ```

To access the GeoIP data:

   Note that geo_info is a dictionary that includes the following:
   ```python
   geo_info = {
      'fqdn_or_ip': '',
      'city': '', 
      'continent_code': '', 
      'region': '',
      'charset': 0,
      'area_code': 0,
      'longitude': 0.0,
      'country_code3': '',
      'latitude': 0.0,
      'postal_code': None,
      'dma_code': 0,
      'country_code': '',
      'country_name': '',
   }
   # If some fields are not available they are left unpopulated.
   ```

To access the GoeIP data via template tags:

The following filters are available for extracting specific GeoIP data in the templates.
Requirement:  ``django.core.context_processors.request`` must be present in your `TEMPLATE_CONTEXT_PROCESSORS`.

    {% load geoaware %} # Or set `GEOIP_INCLUDE_TEMPLATE_TAGS = True` in your settings to auto include tags

    {{ request|geo_country_name }}
    {{ request|geo_country_code }}
    {{ request|geo_country_code3 }}
    {{ request|geo_city }}
    {{ request|geo_latitude }}
    {{ request|geo_longitude }}
    {{ request|geo_postal_code }}
    {{ request|geo_region }}
    {{ request|geo_dma_code }}
    {{ request|geo_area_code }}
    {{ request|geo_fqdn_or_ip }}
    {{ request|geo_charset }}


Running the tests
=================

To run the tests against the current environment:

    python manage.py test geoaware # ToDo

    Note: if you are running on localhost in DEBUG mode, then you can add to your settings.py 
          `GEOIP_DEBUG_DOMAIN_OR_IP = 'google.com'` OR `GEOIP_DEBUG_DOMAIN_OR_IP = 'some valid public ip'`. 
          This is for testing purposes ONLY.


Changelog
=========

0.5.0 
-----
* default to GEOIP_MEMORY_CACHE = GEOIP_STANDARD if not provided

0.4.0
-----
* allow auto tag inclusion if flag is set

0.3.0
-----
* force cookie to be saved
* changed default GeoIP caching option

0.2.0
-----
* added template tags (filters)

0.1.0
-----
* initial release


License
=======

Copyright © Val Neekman

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Note: Django is a registered trademark of the Django Software Foundation.

