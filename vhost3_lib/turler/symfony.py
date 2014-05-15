#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur
from vhost3_conf import *
from os import system, path, makedirs

class Symfony (Tur):

	def __init__(self, kullanici):
		self.apache = self._oku(path.dirname(__file__) + '/symfony/apache').replace("\n\n", "\n")
		self._index = self._oku(path.dirname(__file__) + '/symfony/index').replace("\n\n", "\n")
		
		super(Symfony, self).__init__(kullanici)

	def dizinler(self):
		super(Symfony, self).dizinler()

		makedirs('/var/www/' + self.kullanici + '/web')

	def yonet(self, komut):
		system('cd /var/www/' + self.kullanici + ' && ./app/console ' + komut)
		self._komutlar()

	def _komutlar(self):
		system('chmod -R 777 /var/www/' + self.kullanici)
		system('chown -R ' + VARSAYILAN_KULLANICI + ':www-data /var/www/' + self.kullanici)
		system('APACHEUSER=`ps aux | grep -E \'[a]pache|[h]ttpd|[_]www|[w]ww-data\' | grep -v root | head -1 | cut -d\  -f1` && setfacl -R -m u:"$APACHEUSER":rwX -m u:`whoami`:rwX /var/www/' + self.kullanici + '/app/cache /var/www/' + self.kullanici + '/app/logs && setfacl -dR -m u:"$APACHEUSER":rwX -m u:`whoami`:rwX /var/www/' + self.kullanici + '/app/cache /var/www/' + self.kullanici + '/app/logs')
		system('chmod 755 /var/www/phpmyadmin/public_html/config.inc.php')