# Django settings for postfixadmin project.

import os.path

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
JOIN = os.path.join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Claudio Borges', 'cbsfilho@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'postfix'
DATABASE_USER = 'postfix'
DATABASE_PASSWORD = 'Eir3so0kae1Ae'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = '/usr/share/pyshared/django/contrib/admin/media/'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '&+x4&8&wqicd$0)$ssjq1$x)=d!x9(n)q4*jn231&cyyz@outi'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'postfixadmin.urls'

TEMPLATE_DIRS = (
    JOIN(ROOT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    # Postfixadmin extensions
    'postfixadmin.aliases',
    'postfixadmin.domains',
    'postfixadmin.users',
    'postfixadmin.autoresponse'
)
