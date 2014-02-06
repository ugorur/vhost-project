#!/usr/bin/env python
#-*-coding:utf-8-*-

from MySQLdb import connect

from . import Lib
from vhost2_conf import *

class MySQL (Lib):

	root = connect('localhost', 'root', ROOT_SIFRE)

	def __init__(self, kullanici):
		self.kullanici = kullanici
		self.imlec = self.root.cursor()

	def yarat(self, sifre = ROOT_SIFRE):
		self.imlec.execute('CREATE DATABASE IF NOT EXISTS ' + self.kullanici + '_db CHARACTER SET utf8 COLLATE utf8_general_ci')
		self.imlec.execute('GRANT ALL ON ' + self.kullanici + '_db.* TO ' + self.kullanici + '@localhost IDENTIFIED BY \'' + sifre + '\'')

	def yoket(self):
		self.yarat()

		self.imlec.execute('DROP DATABASE '  + self.kullanici + '_db')
		self.imlec.execute('DROP USER ' + self.kullanici + '@localhost')

	def __del__(self):
		self.imlec.execute('FLUSH PRIVILEGES')

		self.root.commit()
		self.root.close()