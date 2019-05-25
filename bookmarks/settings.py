import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '2l&rh3b+hb^#bt4vt_)e6**7di&br+bg#kbwhwjf59v8%!00v0'

DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', 'dc1826c4.ngrok.io']

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'images.apps.ImagesConfig',
    'actions.apps.ActionsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "bootstrap4",
    'social_django',
    'sorl.thumbnail',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmarks.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bookmarks/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'account.authentication.EmailAuthBackend',
  'social_core.backends.facebook.FacebookOAuth2',
  'social_core.backends.twitter.TwitterOAuth',
  'social_core.backends.google.GoogleOAuth2',
]


# Social Login
SOCIAL_AUTH_FACEBOOK_KEY = 'XXX'
SOCIAL_AUTH_FACEBOOK_SECRET = 'XXX'

SOCIAL_AUTH_TWITTER_KEY = 'XXX'
SOCIAL_AUTH_TWITTER_SECRET = 'XXX'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'XXX'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XXX'


from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
  'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}


# REDIS 
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0