"""
Django settings for minister_ext project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# settings.py

import os
import firebase_admin
from firebase_admin import credentials



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize Firebase Admin SDK
firebase_credentials_path = os.path.join(BASE_DIR, 'firebase', 'consrimcasa-89f6e-firebase-adminsdk-vd1lo-83a337bd3e.json')
firebase_credentials = credentials.Certificate(firebase_credentials_path)
firebase_admin.initialize_app(firebase_credentials)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(e$r9#zt2&)j-zo$^eeru5%+#lb4l1cdtz2e_$*()_ec=32kdt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "app1",
    # "tinymce",
    "adminapp",
    # "crispy_forms",
    "usersmanagement"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #add it exactlyhere
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minister_ext.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': ['templates'],
        # 'APP_DIRS': True,
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

# WSGI_APPLICATION = 'minister_ext.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# from django.utils.translation import gettext_lazy as _

LOCALE_PATHS=(
  os.path.join(BASE_DIR,'locale'),  
)


# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    # ('en', _('English')),
    ('fr', _('French')),
    ('ar', _('Arabic')),
    
    
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# if  not DEBUG:    # Tell Django to copy statics to the `static files` directory
#     # in your application directory on Render.
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# else:  
#     STATICFILES_DIRS =[
#         os.path.join(BASE_DIR, "static"),
#         # '/var/www/static'
#     ]

# STATIC_URL = '/static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static/"),
# ]
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# if not DEBUG :
#     STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
# else :
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, "/static/"),
#     ]
    
# # Base url to serve media filess
# MEDIA_URL = '/media/'

# # Path where media is stored
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# JAZZMIN_SETTINGS = {
#     # "title": "Université De Nouakchott",
#     # "site_title": "Université De Nouakchott",
#     # "site_header": "Université De Nouakchott",

#     # Logo
#     "site_logo": "logo.png",

#     # Welcome message on login screen
#     # "welcome_sign": "Welcome to University Of Nouakchott Administration",
#     "welcome_sign": "Minister de l'exterieure",

#     # "copyright": " University Of Nouakchott",
    
#     # "language_chooser": True,
    

#     # UI Tweaks
#     "show_ui_builder": True,
   
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": False,
#     "brand_small_text": False,
#     "brand_colour": False,
#     "accent": "accent-primary",
#     # "navbar": "navbar-success navbar-dark",
#     "navbar": "navbar-dark-primary", 
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": False,
#     "sidebar": "sidebar-dark-primary",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": False,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "default",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-primary",
#         "secondary": "btn-secondary",
#         "info": "btn-info",
#         "warning": "btn-warning",
#         "danger": "btn-danger",
#         "success": "btn-success"
#     }

    
# }


# JAZZMIN_SETTINGS = {
#     "title": "Minister de l'exterieure",
#     "site_title": "Minister de l'exterieure",
#     "site_header": "Minister de l'exterieure",

#     # Logo
#     "site_logo": "logo.ico",


#     # Welcome message on login screen
#     "welcome_sign": "Bienvenu à la siteweb de la Minister de l'exterieure",

#     "copyright": " Minister de l'exterieure",
    
#     # "language_chooser": True,
    
#     # UI Tweaks
#     # "show_ui_builder": True,

# }

# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": False,
#     "brand_small_text": False,
#     "brand_colour": "navbar-success",
#     "accent": "accent-primary",
#     "navbar": "navbar-success navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": False,
#     "sidebar": "sidebar-dark-primary",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": False,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "default",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-outline-primary",
#         "secondary": "btn-outline-secondary",
#         "info": "btn-outline-info",
#         "warning": "btn-outline-warning",
#         "danger": "btn-outline-danger",
#         "success": "btn-outline-success"
#     }
# }


# settings.py

# TINYMCE_DEFAULT_CONFIG = {
#     'height': 360,
#     'width': 800,
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 20,
#     'selector': 'textarea',
#     'theme': 'modern',
#     'plugins': '''
#         textcolor save link image media preview codesample contextmenu
#         table code lists fullscreen  insertdatetime  nonbreaking
#         contextmenu directionality searchreplace wordcount visualblocks
#         visualchars code fullscreen autolink lists  charmap print  hr
#         anchor pagebreak
#         ''',
#     'toolbar1': '''
#         fullscreen preview bold italic underline | fontselect,
#         fontsizeselect  | forecolor backcolor | alignleft alignright |
#         aligncenter alignjustify | indent outdent | bullist numlist table |
#         | link image media | codesample |
#         ''',
#     'toolbar2': '''
#         visualblocks visualchars |
#         charmap hr pagebreak nonbreaking anchor |  code |
#         ''',
#     'contextmenu': 'formats | link image',
#     'menubar': True,
#     'statusbar': True,
# }

# settings.py

# TINYMCE_DEFAULT_CONFIG = {
#     'selector': 'textarea',  # Apply TinyMCE to all textareas
#     'plugins': 'a11ychecker advcode code editor emoticons fullscreen help hr image link lists media menubar paste search wordcount',
#     'toolbar': 'undo redo | formatselect | bold italic strikethrough | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | code',
#     # Add other configuration options as needed
# }

