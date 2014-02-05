#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur
from random import SystemRandom

class Django (Tur):

	apache = """<VirtualHost %(domain)s>
	ServerAdmin mail@ugorur.com

	ServerName %(domain)s
	ServerAlias www.%(domain)s

	DocumentRoot /var/www/%(kullanici)s/%(kullanici)s

	Alias /phpmyadmin /var/www/phpmyadmin/public_html
	Alias /static/admin /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin

	Alias /public /var/www/%(kullanici)s/public
	Alias /static /var/www/%(kullanici)s/static
	Alias /media /var/www/%(kullanici)s/media

	ErrorLog /var/www/%(kullanici)s/logs/error.log
	CustomLog /var/www/%(kullanici)s/logs/access.log common

	WSGIScriptAlias / /var/www/%(kullanici)s/%(kullanici)s/wsgi.py
	WSGIDaemonProcess %(kullanici)s python-path=/var/www/%(kullanici)s/%(kullanici)s processes=2 threads=15 display-name=%(kullanici)s
	WSGIProcessGroup %(kullanici)s

	<Directory /var/www/%(kullanici)s/%(kullanici)s>
		Options All
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /var/www/phpmyadmin/public_html>
		DirectoryIndex index.php
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin>
		Options All
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /var/www/%(kullanici)s/public_html>
		DirectoryIndex index.html index.php
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /var/www/%(kullanici)s/static>
		DirectoryIndex index.html
		Options All
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /var/www/%(kullanici)s/media>
		DirectoryIndex index.html
		Options All
		AllowOverride All
		Require all granted
	</Directory>
</VirtualHost>"""

	_wsgi = """import sys
sys.path.append('/var/www')
sys.path.append('/var/www/%(kullanici)s')
sys.path.append('/var/www/%(kullanici)s/%(kullanici)s')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%(kullanici)s.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()"""

	_settings = """import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '%(gizli)s'
DEBUG = %(hata_ayiklama)s
TEMPLATE_DEBUG = %(hata_ayiklama)s
ALLOWED_HOSTS = ['%(domain)s', 'www.%(domain)s']
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
)
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = '%(kullanici)s.urls'
WSGI_APPLICATION = '%(kullanici)s.wsgi.application'
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'HOST': 'localhost',
		'PORT': 3306,
		'NAME': '%(kullanici)s_db',
		'USER': '%(kullanici)s',
		'PASSWORD': '%(sifre)s',
		'OPTIONS': {
			'init_command': 'SET storage_engine=INNODB'
		}
	}
}
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
		'LOCATION': '/var/www/%(kullanici)s/cache',
	}
}
LANGUAGE_CODE = 'tr-TR'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = 'http://www.%(domain)s/static/'
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]"""

	_izin_yok = """<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Giriş yasak!!!</title>
	</head>
	<body>
		Bu sayfaya girmeniz mahkeme kararı ile olmasada yasaklandı...
	</body>
</html>"""

	def __init__(self, kullanici):
		super(Django, self).__init__(kullanici)

	def yarat(self, domain, sifre, ha):
		self.dizinler()
		self.index()

		system('django-admin.py startproject ' + self.kullanici + ' /var/www/' + self.kullanici)

		dosya = open('/var/www/' + self.kullanici + '/' + self.kullanici + '/wsgi.py', 'w')
		dosya.write(self._wsgi % {'kullanici': self.kullanici})
		dosya.close()

		if ha:
			hata_ayiklama = 'True'
		else:
			hata_ayiklama = 'False'

		dosya = open('/var/www/' + self.kullanici + '/' + self.kullanici + '/settings.py', 'w')
		dosya.write(self._settings % {
			'kullanici': self.kullanici, 
			'domain': domain, 
			'sifre': sifre, 
			'hata_ayiklama': hata_ayiklama,
			'gizli': ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
		})
		dosya.close()

	def dizinler(self):
		super(Django, self).dizinler()

		makedirs('/var/www/' + self.kullanici + '/static')
		makedirs('/var/www/' + self.kullanici + '/cache')
		makedirs('/var/www/' + self.kullanici + '/media')
		makedirs('/var/www/' + self.kullanici + '/templates')

	def index(self):
		super(Django, self).index()

		dosya = open('/var/www/' + self.kullanici + '/static/index.html', 'w')
		dosya.write(self._izin_yok)
		dosya.close()

		dosya = open('/var/www/' + self.kullanici + '/media/index.html', 'w')
		dosya.write(self._izin_yok)
		dosya.close()

	def yonet(self, komut):
		system('cd /var/www/' + self.kullanici + ' && python manage.py ' + komut)
		system('chmod -R 777 /var/www/' + self.kullanici)
		system('chown -R ugorur:www-data /var/www/' + self.kullanici)
