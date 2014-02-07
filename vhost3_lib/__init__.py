#!/usr/bin/env python
#-*-coding:utf-8-*-

class Lib (object):

	def _oku(self, yol):
		dosya = open(yol)
		veriler = dosya.readlines()
		dosya.close()

		return "\n".join(veriler)

	def _yaz(self, yol, icerik, mod = 'w'):
		dosya = open(yol, mod)
		dosya.write(icerik)
		dosya.close()