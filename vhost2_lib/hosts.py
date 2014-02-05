#!/usr/bin/env python
#-*-coding:utf-8-*-

class Hosts (object):

	def __init__(self, domain):
		self.domain = domain

	def ekle(self):
		dosya = open('/etc/hosts', 'a')
		dosya.write('\n127.0.0.1\t' + self.domain + '\twww.' + self.domain)
		dosya.close()

	def sil(self):
		dosya = open('/etc/hosts', 'r')
		satirlar = dosya.readlines()
		dosya.close()

		dosya = open('/etc/hosts', 'w')
		for satir in satirlar:
			if satir.strip() == '127.0.0.1\t' + self.domain + '\twww.' + self.domain:
				continue
			dosya.write(satir.strip() + '\n')
		dosya.close()