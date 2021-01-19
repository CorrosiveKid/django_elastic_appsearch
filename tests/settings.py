# -*- coding: utf-8
"""Settings module for django_elastic_appsearch."""
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^ce%0j9&!!ih1&7qtws%wi#v0gfieslnu2k9l=z*qw_kydc4dd"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_elastic_appsearch",
    "example",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()

APPSEARCH_HOST = 'example_appsearch_host'
APPSEARCH_API_KEY = 'example_appsearch_api_key'
APPSEARCH_CHUNK_SIZE = 5
