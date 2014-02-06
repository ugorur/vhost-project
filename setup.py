#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import system
from setuptools import setup, find_packages

VERSIYON = '0.0.4'

VARSAYILAN_CONF = """#!/usr/bin/env python
#-*-coding:utf-8-*-

PLATFORMLAR = ['django', 'php']
ISLEMLER = ['ekle', 'sil', 'yonet', 'pasif', 'aktif']

ROOT_SIFRE = '%(sifre)s'

VARSAYILAN_EPOSTA_ADRESI = '%(eposta)s'
VARSAYILAN_KULLANICI = '%(kullanici)s'
VARSAYILAN_UZANTI = '%(uzanti)s'
VARSAYILAN_HATA_AYIKLAMA = %(hata_ayiklama)s"""

class Kur(object):

	def __init__(self):
		self.sorular()
		self.ayar_olustur()

		dosya = open('vhost2_conf.py', 'w')
		dosya.write(VARSAYILAN_CONF % self.ayarlar)
		dosya.close()

		self.olustur()

	def sorular(self):
		self.sifre         = raw_input('MySQL Roots Şifresi Giriniz: ')
		self.eposta        = raw_input('E-Posta Adresinizi Giriniz: ')
		self.kullanici     = raw_input('Linux Kullanıcı Adınızı Giriniz: ')
		self.uzanti        = raw_input('Varsayılan Alan Adı Uzantınızı Giriniz: ')
		self.hata_ayiklama = raw_input('Hata Ayıklama Açılsın mı? (E/H): ')

	def ayar_olustur(self):
		self.ayarlar = {
			'sifre'        : self.sifre     if self.sifre         else '1234',
			'eposta'       : self.eposta    if self.eposta        else 'webmaster@localhost',
			'kullanici'    : self.kullanici if self.kullanici     else 'www-data',
			'uzanti'       : self.uzanti    if self.uzanti        else 'loc',
			'hata_ayiklama': 'True'         if self.hata_ayiklama else 'False',
		}

	def olustur(self):
		setup(
			name = 'Virtual Host Creater',
			version = VERSIYON,
			description = 'Virtual Host Creater Project',
			author = 'ugorur',
			author_email = "mail@ugorur.com",
			url = 'https://github.com/ugorur/vhost-project',
			license = 'GPL v2',
			packages = find_packages(),
			include_package_data = True,
			scripts = ['vhost2_conf.py', 'vhost2.py'],
			package_data = {
				'vhost2_lib': ['turler/php/*', 'turler/django/*']
			},
			entry_points = {'console_scripts': ['vhost2 = vhost2:main']}
		)

	def __del__(self):
		system ('rm -rf vhost2_conf.py')

def main():
	Kur()

if __name__ == '__main__':
	main()