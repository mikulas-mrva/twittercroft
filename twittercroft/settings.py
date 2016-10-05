import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '3fj*yce)oy+hz7q@*#b4@tvw_i*0tt@reyh%9qqgaq_e8i0c@z'

DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    #'django.contrib.sites',
    'django.contrib.staticfiles',
    'tweetmap',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'twittercroft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # 'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'twittercroft.wsgi.application'


LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# TODO Override those in your local settings
TWITTER_API_CONSUMER_KEY = None
TWITTER_API_CONSUMER_SECRET = None
TWITTER_API_ACCESS_TOKEN = None
TWITTER_API_ACCESS_SECRET = None

TWITTER_MAPLECROFT_SCRREEN_NAME = 'maplecroftrisk'
DEFAULT_NUMBER_OF_TWEETS = 10

try:
    from twittercroft.local_settings import *
except ImportError as e:
    pass
