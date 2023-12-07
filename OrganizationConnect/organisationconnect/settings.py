from pathlib import Path
import os
from django.contrib.messages import constants as messages
import environ



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'ckeditor_uploader',
    

      'settings.apps.SettingsConfig',

        'wiki.apps.WikiConfig',
    'members.apps.MembersConfig',
    'search.apps.SearchConfig',
    'forum.apps.ForumConfig',

    # Local apps
    'accounts.apps.AccountsConfig',
    'magazine',
    'category',
    'dashboard',
    'chat',
    'tinymce',

    # Third party apps
    'ckeditor',
    
    'taggit',
    'active_link',
       "crispy_forms",
    "crispy_bootstrap4",
]

 
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'organisationconnect.urls'

# Templates Directory
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.cat_links',
            ],
        },
    },
]

WSGI_APPLICATION = 'organisationconnect.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'

CKEDITOR_UPLOAD_PATH = "uploads/"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

 

 

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

# Path where static files are stored
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ckeditor uploaded media path
CKEDITOR_UPLOAD_PATH = "uploads/"

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# CKeditor configurations
CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'full',
        'tabSpaces': 4,
        'image2_altRequired':  'true',
        # 'contentsCss': 'static/css/style.css',

        'stylesSet.add':  [
            {
                "name": 'Lead',
                "element": 'p',
                "attributes": {'class': 'lead'},
            },
            {
                "name": 'quote',
                "element": 'div',
                "styles": {'background-color': '#F9F9FF',
                           'padding': '20px',
                           'border-radius': '20px',
                           'margin-top': '30px',
                           'margin-bottom': '30px',
                           'text-align': 'center', },
            },
            {
		'name': 'container white',
		'element': 'div',
		'styles': {
                    'padding': '5px 10px',
                 			'background': '#fff',
                 			'border': 'none'
		}
            },
        ],
        'extraPlugins': ','.join(['codesnippet',
                                  'devtools',
                                  'templates',
                                  'widget',
                                  'uicolor',
                                  'dialog',
                                  'filetools',
                                  'stylesheetparser',
                                  'image2'

                                  ]),

    },
}

ACTIVE_LINK_STRICT = True
ACTIVE_LINK_CSS_CLASS = False


# SMTP configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_USE_TLS = True