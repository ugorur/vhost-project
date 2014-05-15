#!/usr/bin/env python
#-*-coding:utf-8-*-

from sys import exit, argv
from os import system, environ, path

from vhost3_conf import *

from vhost3_lib.apache import Apache
from vhost3_lib.hosts import Hosts
from vhost3_lib.mysql import MySQL
from vhost3_lib.turler.php import PHP
from vhost3_lib.turler.symfony import Symfony
from vhost3_lib.turler.django import Django

class Program (object):

	domain = None
	uzanti = VARSAYILAN_UZANTI
	sifre = ROOT_SIFRE
	hata_ayiklama = VARSAYILAN_HATA_AYIKLAMA

	def __init__(self):
		self._kontrol()
		self._argv()
		self._kullanici()
		self._platformlar()
	 	self._islemler()

	def _islemler(self):
		eval('self._' + self.islem + '()')
		self._yenile()

	def _sil(self):
		self._uzanti()

		hosts = Hosts(self.domain)
		hosts.sil()

		apache = Apache(self.domain)
		apache.sil()

		self.platform.sil()

		mysql = MySQL(self.kullanici)
		mysql.yoket()

	def _ekle(self):
		self._kullanici_varmi_kontrol()
		self._uzanti()
		self._sifre()
		self._hata_ayiklama()

		hosts = Hosts(self.domain)
		hosts.ekle()

		self.platform.yarat(self.domain, self.sifre, self.hata_ayiklama)

		apache = Apache(self.domain)
		apache.ekle(self.platform.apache, self.kullanici)

		mysql = MySQL(self.kullanici)
		mysql.yarat(self.sifre)

		system('chmod -R 777 /var/www/' + self.kullanici)
		system('chown -R ' + VARSAYILAN_KULLANICI + ':www-data /var/www/' + self.kullanici)

	def _uzanti(self):
		uzanti = raw_input('Uzantı: ')

		if uzanti:
			self.uzanti = uzanti

		self.domain = self.kullanici + '.' + self.uzanti

	def _yonet(self):
		komut = raw_input('Komut: ')

		if not komut:
			print '\033[1m\033[91mHATA:\033[0m Lüften bir komut giriniz'
			exit()

		self.platform.yonet(komut)

	def _sifre(self):
		sifre = raw_input('Şifre: ')

		if sifre:
			self.sifre = sifre

	def _hata_ayiklama(self):
		if raw_input('Hata Ayıklama Açılsın mı? (E/H): ').lower() == 'h':
			self.hata_ayiklama = False

	def _yenile(self):
		apache = Apache(self.domain)
		apache.yenile()

		system('chmod 755 /var/www/phpmyadmin/public_html/config.inc.php')

		system('service nscd restart')
		exit()

	def _pasif(self):
		self._uzanti()

		apache = Apache(self.domain)
		apache.pasif()

	def _aktif(self):
		self._uzanti()

		apache = Apache(self.domain)
		apache.aktif()

	def _kontrol(self):
		if 'SUDO_UID' in environ.keys():
			if len(argv) == 2:
				if argv[1] == 'yenile':
					self._yenile()
				elif argv[1] == '--versiyon' or argv[1] == '-v':
					print VERSIYON
					exit()

			if len(argv) < 3:
				print '\033[1m\033[91mHATA:\033[0m Lüften programı bir komut ile çalıştırın: "sudo vhost3 <platform> <islem>"'
				exit()
		else:
			print '\033[1m\033[91mHATA:\033[0m Yönetici girişi yapmak gerek. Lüften programı "sudo vhost3 <platform> <islem>" komutu ile çalıştırın'
			exit()

	def _argv(self):		
		self._platform = argv[1]
		self.islem = argv[2]
		self._argv_kontrol()

	def _argv_kontrol(self):
		if self._platform not in PLATFORMLAR:
			print '\033[1m\033[91mHATA:\033[0m Lütfen geçerli platform giriniz'
			print 'Geçerli platformlar: ' + ', '.join(PLATFORMLAR)
			exit()

		if self.islem not in ISLEMLER:
			print '\033[1m\033[91mHATA:\033[0m Lütfen geçerli işlem giriniz'
			print 'Geçerli işlemler: ' + ', '.join(ISLEMLER)
			exit()

	def _kullanici(self):
		self.kullanici = raw_input('Kullanıcı Adı: ')
		self._kullanici_kontrol()

	def _kullanici_kontrol(self):
		if not self.kullanici:
			print '\033[1m\033[91mHATA:\033[0m Kullanıcı Adı olmadan olmaz'
			exit()

	def _kullanici_varmi_kontrol (self):
		if path.isdir('/var/www/' + self.kullanici):
			print '\033[1m\033[91mHATA:\033[0m Bu adres daha önce kullanılmış'
			exit()

	def _platformlar(self):
		if self._platform == 'django':
			self.platform = Django(self.kullanici)
		elif self._platform == 'php':
			self.platform = PHP(self.kullanici)
		elif self._platform == 'symfony':
			self.platform = Symfony(self.kullanici)

def main():
	Program()

if __name__ == '__main__':
	main()