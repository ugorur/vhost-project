#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import system
from setuptools import setup, find_packages
import subprocess

VERSIYON = '3.4.0'

VARSAYILAN_CONF = """#!/usr/bin/env python
#-*-coding:utf-8-*-

VERSIYON = '%(versiyon)s'

PLATFORMLAR = ['django', 'php', 'symfony']
ISLEMLER = ['ekle', 'sil', 'yonet', 'pasif', 'aktif']

ROOT_SIFRE = '%(sifre)s'

VARSAYILAN_EPOSTA_ADRESI = '%(eposta)s'
VARSAYILAN_KULLANICI = '%(kullanici)s'
VARSAYILAN_UZANTI = '%(uzanti)s'
VARSAYILAN_HATA_AYIKLAMA = %(hata_ayiklama)s"""

XDEBUG_CONF = """zend_extension="/usr/lib/xdebug.so"
xdebug.remote_enable=1"""

class Kur(object):

	def __init__(self):
		self._sorular()
		self._system()
		self._composer()
		self._xdebug()
		self._ayar_olustur()
		self._dosya_olustur()
		
		self.olustur()

	def _sorular(self):
		self.sifre         = raw_input('MySQL Roots Şifresi Giriniz: ')
		self.eposta        = raw_input('E-Posta Adresinizi Giriniz: ')
		self.kullanici     = raw_input('Linux Kullanıcı Adınızı Giriniz: ')
		self.uzanti        = raw_input('Varsayılan Alan Adı Uzantınızı Giriniz: ')
		self.hata_ayiklama = raw_input('Hata Ayıklama Açılsın mı? (E/H): ')

	def _ayar_olustur(self):
		self.ayarlar = {
			'versiyon'     : VERSIYON,
			'sifre'        : self.sifre     if self.sifre                        else '1234',
			'eposta'       : self.eposta    if self.eposta                       else 'webmaster@localhost',
			'kullanici'    : self.kullanici if self.kullanici                    else 'www-data',
			'uzanti'       : self.uzanti    if self.uzanti                       else 'loc',
			'hata_ayiklama': 'True'         if self.hata_ayiklama.upper() != 'H' else 'False',
		}

	def _dosya_olustur(self):
		dosya = open('vhost3_conf.py', 'w')
		dosya.write(VARSAYILAN_CONF % self.ayarlar)
		dosya.close()

	def _xdebug(self):
		system('cd xdebug && phpize && ./configure --enable-xdebug && make && make install && cp modules/xdebug.so /usr/lib/.')
		dosya = open('/etc/php/7.0/apache2/conf.d/20-xdebug.ini', 'w')
		dosya.write(XDEBUG_CONF)
		dosya.close()

		dosya = open('/etc/php/7.0/cli/conf.d/20-xdebug.ini', 'w')
		dosya.write(XDEBUG_CONF)
		dosya.close()
		dosya.close()

	def _composer(self):
		system('php -r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"')
		system('php composer-setup.php --install-dir=/usr/bin --filename=composer')
		system('php -r "unlink(\'composer-setup.php\');"')
		
	def _system(self):
		p = subprocess.Popen(['apt-get install mysql-server mysql-client apache2 php7.0 libapache2-mod-php7.0 php7.0-mbstring php7.0-mysql php7.0-curl php7.0-gd php-pear php7.0-imap php7.0-mcrypt php7.0-pspell php7.0-pspell php7.0-recode php7.0-snmp php7.0-sqlite3 php7.0-bz2 php7.0-dev php7.0-zip php7.0-tidy php7.0-xmlrpc php7.0-xsl php7.0-json python-mysqldb python-pip git nscd python-imaging python-pythonmagick python-markdown python-textile python-docutils python-django snmp'],  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		stdout, stderr = p.communicate(input=self.sifre + '\n')

	def olustur(self):
		setup(
			name                 = 'Virtual Host Creater 3',
			version              = VERSIYON,
			description          = 'Virtual Host Creater Project',
			author               = 'ugorur',
			author_email         = "mail@ugorur.com",
			url                  = 'https://github.com/ugorur/vhost-project',
			license              = 'GPL v2',
			packages             = find_packages(),
			include_package_data = True,
			scripts              = ['vhost3_conf.py', 'vhost3.py'],
			package_data         = {'vhost3_lib': ['turler/php/*', 'turler/django/*', 'turler/symfony/*', 'turler/phpmyadmin/*']},
			entry_points         = {'console_scripts': ['vhost3 = vhost3:main', 'vhost2 = vhost3:main', 'vhost = vhost3:main']}
		)

	def __del__(self):
		system ('rm -rf vhost3_conf.py')
		system ('vhost kur')

def main():
	Kur()

if __name__ == '__main__':
	main()