#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import system

from . import Lib
from vhost2_conf import *

class Apache (Lib):

	def __init__(self, domain = False):
		self.domain = domain

	def ekle(self, apache_conf, kullanici):
		self._kontrol()

		self._yaz('/etc/apache2/sites-available/' + self.domain + '.conf', apache_conf % {'domain': self.domain, 'kullanici': kullanici, 'eposta': VARSAYILAN_EPOSTA_ADRESI})

		self.aktif()

	def aktif(self):
		self._kontrol()
		
		system('a2ensite ' + self.domain)

	def pasif(self):
		self._kontrol()
		
		system('a2dissite ' + self.domain)

	def sil(self):
		self._kontrol()
		
		self.pasif()
		system('rm -Rf /etc/apache2/sites-available/' + self.domain + '.conf')
	
	def _kontrol(self):
		if not self.domain:
			print '\033[1m\033[91mHATA:\033[0m Lütfen domain adresi bilgisi veriniz'
	 		exit()

	def yenile(self):
		system('service apache2 restart')