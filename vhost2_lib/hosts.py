#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Lib

class Hosts (Lib):

	def __init__(self, domain):
		self.domain = domain

	def ekle(self):
		self._yaz('/etc/hosts', '\n127.0.0.1\t' + self.domain + '\twww.' + self.domain, 'a')

	def sil(self):
		icerik = self._oku('/etc/hosts')

		veriler = []

		for satir in icerik.split("\n"):
			if satir.strip() != '127.0.0.1\t' + self.domain + '\twww.' + self.domain:
				veriler.append(satir.strip())

		self._yaz('/etc/hosts', "\n".join(veriler))