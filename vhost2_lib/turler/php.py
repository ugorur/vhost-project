#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur

class PHP (Tur):

	def __init__(self, kullanici):
		self.apache = self._oku(path.dirname(__file__) + '/php/apache')
		self._index = self._oku(path.dirname(__file__) + '/php/index')

		super(PHP, self).__init__(kullanici)
