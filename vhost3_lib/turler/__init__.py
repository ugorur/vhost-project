#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import makedirs, system

from vhost3_lib import Lib

class Tur (Lib):

	def __init__(self, kullanici):
		self.kullanici = kullanici

	def yarat(self, domain, sifre, ha):
		self.dizinler()
		self.index()

	def dizinler(self):
		makedirs('/var/www/' + self.kullanici + '/logs')
		makedirs('/var/www/' + self.kullanici + '/public_html')

	def index(self):
		self._yaz('/var/www/' + self.kullanici + '/public_html/index.php', self._index % {'kullanici': self.kullanici})

	def sil(self):
		system('rm -Rf /var/www/' + self.kullanici)

	def yonet(self, komut):
		pass