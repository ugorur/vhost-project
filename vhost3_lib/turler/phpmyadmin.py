#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur
from MySQLdb import connect
from vhost3_conf import *
from os import path, makedirs, rename, system
from shutil import move, rmtree
from random import SystemRandom
import urllib2, zipfile, subprocess

PHPMYADMIN_VERSION = "4.7.3"

class PHPMyAdmin (Tur):

	def __init__(self):
		self.apache = self._oku(path.dirname(__file__) + '/phpmyadmin/apache').replace("\n\n", "\n")
		self.config = self._oku(path.dirname(__file__) + '/phpmyadmin/config').replace("\n\n", "\n")

		makedirs('/var/www/phpmyadmin/logs')

	def kur(self):
		self._indir_ac()
		self._mysql_ac()
		self._sql_file()
		self._mysql_sorgu()
		self._dizinleri_duzenle()
		self._ayarlar()

	def _ayarlar(self):
		self._yaz('/var/www/phpmyadmin/public_html/config.inc.php', self.config % {
			'gizli': ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(32)]),
			'root_sifre' : ROOT_SIFRE
		})

	def _indir_ac(self):
		f = urllib2.urlopen('https://files.phpmyadmin.net/phpMyAdmin/' + PHPMYADMIN_VERSION + '/phpMyAdmin-' + PHPMYADMIN_VERSION + '-all-languages.zip')

		with open('/tmp/phpmyadmin.zip', "wb") as local_file:
			local_file.write(f.read())

		zfile = zipfile.ZipFile("/tmp/phpmyadmin.zip")
		zfile.extractall('/var/www/phpmyadmin/')

		rename('/var/www/phpmyadmin/phpMyAdmin-' + PHPMYADMIN_VERSION + '-all-languages', '/var/www/phpmyadmin/public_html')

	def _dizinleri_duzenle(self):
		rmtree('/var/www/phpmyadmin/public_html/doc')
		rmtree('/var/www/phpmyadmin/public_html/examples')
		rename('/var/www/phpmyadmin/public_html/locale/tr', '/var/www/phpmyadmin/public_html/tr')
		rmtree('/var/www/phpmyadmin/public_html/locale')
		makedirs('/var/www/phpmyadmin/public_html/locale')
		rename('/var/www/phpmyadmin/public_html/tr', '/var/www/phpmyadmin/public_html/locale/tr')

	def _mysql_ac(self):
		root = connect('localhost', 'root', ROOT_SIFRE)
		imlec = root.cursor()
		imlec.execute('CREATE DATABASE IF NOT EXISTS phpmyadmin_db CHARACTER SET utf8 COLLATE utf8_general_ci')
		imlec.execute('GRANT ALL ON phpmyadmin_db.* TO phpmyadmin@localhost IDENTIFIED BY \'' + ROOT_SIFRE + '\'')
		imlec.execute('FLUSH PRIVILEGES')
		root.commit()
		root.close()

	def _mysql_sorgu(self):
		proc = subprocess.Popen(["mysql", "--user=phpmyadmin", "--password=" + ROOT_SIFRE, "phpmyadmin_db"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		out, err = proc.communicate(file("/tmp/phpmyadmin.sql").read())

	def _sql_file(self):
		sql_file = []
		next_line = 0

		for line in open("/var/www/phpmyadmin/public_html/sql/create_tables.sql"):
			if next_line:
				sql_file.append('-- ' + line)
				next_line -= 1
			elif line[:15] == 'CREATE DATABASE':
				sql_file.append('-- ' + line)
				next_line = 2
			else:
				sql_file.append(line)

		yeni_sql = open('/tmp/phpmyadmin.sql', "w")
		yeni_sql.writelines(sql_file)
		yeni_sql.close()

	def __del__(self):
		system ('rm -rf /tmp/phpmyadmin.zip')
		system ('rm -rf /tmp/phpmyadmin.sql')
