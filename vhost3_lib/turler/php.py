#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur
from os import path

class PHP (Tur):

	def __init__(self, kullanici):
		self.apache = self._oku(path.dirname(__file__) + '/php/apache').replace("\n\n", "\n")
		self._index = self._oku(path.dirname(__file__) + '/php/index').replace("\n\n", "\n")

		super(PHP, self).__init__(kullanici)
