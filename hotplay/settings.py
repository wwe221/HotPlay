"""
Django settings for hotplay project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#7)9edgh+zlt#%3ts=!i$vt85*y)!!_k!j_0w26e*&9hy-9843'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://hotplay.herokuapp.com/','localhost','127.0.0.1','hotplay.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'crawling',
    'subfunction',
    'imagekit',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotplay.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'hotplay.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AUTH_USER_MODEL = 'accounts.user'

"""
STATIC_URL은 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
이 최상위 경로 자체는 실제 파일이나 디렉터리가 아니며, URL로만 존재하는 단위
그래서 이용자 마음대로 정해도 무방
문자열은 반드시 / 로 끝나야 함
http://localhost:8000/static/~/~
STATIC_URL은 정적 파일이 실제 위치한 경로를 참조하며, 
이 실제 경로는 STATICFILES_DIRS 설정 항목에 지정된 경로가 아닌 STATIC_ROOT 설정 항목에 지정된 경로
"""
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

"""
STATIC_ROOT는 Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로
한 곳에 모으는 기능은 manage.py 파일의 collectstatic 명령어로 수행
Django가 모든 파일을 검사하여 정적 파일로 사용하는지 여부를 확인한 뒤 모으는 건 아니고,
각 Django 앱 디렉터리에 있는 static 디렉터리와 STATICFILES_DIRS에 지정된 경로에 있는 모든 파일을 모은다.
개발 과정에서 정확히는 settings.py의 DEBUG가 True로 설정되어 있으면 STATIC_ROOT 설정은 작용하지 않으며, 
STATIC_ROOT는 실 서비스 환경을 위한 설정 항목
개발 과정에선 STATIC_ROOT에 지정한 경로가 실제로 존재하지 않거나 STATIC_ROOT 설정 항목 자체가 없어도 문제없이 동작
"""

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'j89959343@gmail.com'

EMAIL_HOST_PASSWORD = '******'
EMAIL_USE_TLS = True