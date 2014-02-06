#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur
from vhost2_conf import *
from random import SystemRandom
from os import path, makedirs

class Django (Tur):

	def __init__(self, kullanici):
		self.apache = self._oku(path.dirname(__file__) + '/django/apache')
		self._wsgi = self._oku(path.dirname(__file__) + '/django/wsgi')
		self._settings = self._oku(path.dirname(__file__) + '/django/settings')
		self._izin_yok = self._oku(path.dirname(__file__) + '/django/izinyok')
		self._index = self._oku(path.dirname(__file__) + '/django/index')
		
		super(Django, self).__init__(kullanici)

	def yarat(self, domain, sifre, hata_ayiklama):
		self.dizinler()
		self.index()

		system('django-admin.py startproject ' + self.kullanici + ' /var/www/' + self.kullanici)

		self._yaz('/var/www/' + self.kullanici + '/' + self.kullanici + '/wsgi.py', self._wsgi % {'kullanici': self.kullanici})

		self.yaz('/var/www/' + self.kullanici + '/' + self.kullanici + '/settings.py', self._settings % {
			'kullanici': self.kullanici, 
			'domain': domain, 
			'sifre': sifre, 
			'hata_ayiklama': 'True' if hata_ayiklama else 'False',
			'gizli': ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
		})

	def dizinler(self):
		super(Django, self).dizinler()

		makedirs('/var/www/' + self.kullanici + '/static')
		makedirs('/var/www/' + self.kullanici + '/cache')
		makedirs('/var/www/' + self.kullanici + '/media')
		makedirs('/var/www/' + self.kullanici + '/templates')

	def index(self):
		super(Django, self).index()

		self._yaz('/var/www/' + self.kullanici + '/static/index.html', self._izin_yok)
		self._yaz('/var/www/' + self.kullanici + '/media/index.html', self._izin_yok)

	def yonet(self, komut):
		system('cd /var/www/' + self.kullanici + ' && python manage.py ' + komut)
		system('chmod -R 777 /var/www/' + self.kullanici)
		system('chown -R ' + VARSAYILAN_KULLANICI + ':www-data /var/www/' + self.kullanici)