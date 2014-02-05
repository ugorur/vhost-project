#!/usr/bin/env python
#-*-coding:utf-8-*-

from sys import exit, argv
from os import makedirs, system, path
import MySQLdb

class Host(object):

	def __init__(self):
		len_argv = len(argv);
		if len_argv > 1:
			if argv[1] == 'restart':
				self.restart()
			elif argv[1] == 'delete':
				if len_argv > 2:
					self.domain = argv[2]
				else:
					self.domain = raw_input('Domain: ')

				if not self.domain:
			 		print '\033[1m\033[91mHATA:\033[0m Domain adı olmadan olmaz!!!\033[1m\033[91m!!!\033[0m'
			 		exit()

				if not path.isdir('/var/www/' + self.domain):
					print '\033[1m\033[91mHATA:\033[0m Bu adres daha önce kullanılMAmış\033[1m\033[91m!!!\033[0m'
					exit()

				self.delete_settings()
				self.delete_mysql()
				self.delete_dirs()
				self.delete_hosts()
				self.restart()
			elif argv[1] == 'django':
				if len_argv > 2:
					self.domain = argv[2]

					self.kontrol()

					if len_argv > 3 and (argv[3] == 'Y' or argv[3] == 'y'):
						if len_argv == 5:
							self.mysql(argv[4])
						else:
							self.mysql(False)
				else:
					self.domain = raw_input('Domain: ')

					self.kontrol()

					db = raw_input('Database? (Y/N): ')
					if db == 'Y' or db == 'y':
			 			self.mysql(raw_input('Password: '))

				self.django_mkdirs()
				self.django_settings()
				self.django_apache()
				self.hosts()
			 	self.settings()
				self.restart()

			self.domain = argv[1]

			self.kontrol()
				
			if len_argv > 2 and (argv[2] == 'Y' or argv[2] == 'y'):
				if len_argv == 4:
					self.mysql(argv[3])
				else:
					self.mysql(False)
		else:
			self.domain = raw_input('Domain: ')

			self.kontrol()

			db = raw_input('Database? (Y/N): ')
			if db == 'Y' or db == 'y':
	 			self.mysql(raw_input('Password: '))
		
	 	self.mkdirs()
		self.apache()
		self.index()
		self.hosts()
	 	self.settings()
		self.restart()

	def apache(self):
		dosya = open('/etc/apache2/sites-available/' + self.domain + '.loc.conf', 'w')
		dosya.write('<VirtualHost ' + self.domain + '.loc>\n\tServerAdmin mail@ugorur.com\n\tServerName ' + self.domain + '.loc\n\tServerAlias *.' + self.domain + '.loc\n\tDocumentRoot /var/www/' + self.domain + '/public_html\n\tAlias /phpmyadmin /var/www/phpmyadmin/public_html\n\t<Directory /var/www/' + self.domain + '/public_html>\n\t\tDirectoryIndex index.php\n\t\tOptions Indexes FollowSymLinks\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\t<Directory /var/www/phpmyadmin/public_html>\n\t\tDirectoryIndex index.php\n\t\tOptions Indexes FollowSymLinks\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\tErrorLog /var/www/' + self.domain + '/logs/error.log\n\tCustomLog /var/www/' + self.domain + '/logs/access.log common\n</VirtualHost>')
		dosya.close()

	def django_apache(self):
		dosya = open('/etc/apache2/sites-available/' + self.domain + '.loc.conf', 'w')
		dosya.write('<VirtualHost ' + self.domain + '.loc>\n\tServerAdmin mail@ugorur.com\n\tServerName ' + self.domain + '.loc\n\tServerAlias *.' + self.domain + '.loc\n\tDocumentRoot /var/www/' + self.domain + '/' + self.domain + '\n\tAlias /phpmyadmin /var/www/phpmyadmin/public_html\n\tAlias /static/admin /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin\n\tAlias /static /var/www/' + self.domain + '/static\n\tAlias /media /var/www/' + self.domain + '/media\n\t<Directory /var/www/' + self.domain + '/' + self.domain + '>\n\t\tOptions All\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\t<Directory /var/www/' + self.domain + '/media>\n\t\tOptions All\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\t<Directory /var/www/' + self.domain + '/static>\n\t\tOptions All\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\t<Directory /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin>\n\t\tOptions All\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\t<Directory /var/www/phpmyadmin/public_html>\n\t\tDirectoryIndex index.php\n\t\tOptions Indexes FollowSymLinks\n\t\tAllowOverride All\n\t\tRequire all granted\n\t</Directory>\n\tErrorLog /var/www/' + self.domain + '/logs/error.log\n\tCustomLog /var/www/' + self.domain + '/logs/access.log common\n\tWSGIScriptAlias / /var/www/' + self.domain + '/' + self.domain + '/wsgi.py\n\tWSGIDaemonProcess ' + self.domain + ' python-path=/var/www/' + self.domain + '/' + self.domain + ' processes=2 threads=15 display-name=' + self.domain + '\n\tWSGIProcessGroup ' + self.domain + '\n</VirtualHost>')
		dosya.close()

	def mkdirs(self):
		makedirs('/var/www/' + self.domain + '/logs')
		makedirs('/var/www/' + self.domain + '/public_html')

	def django_mkdirs(self):
		makedirs('/var/www/' + self.domain + '/logs')
		makedirs('/var/www/' + self.domain + '/static')
		makedirs('/var/www/' + self.domain + '/media')

	def index(self):
		dosya = open('/var/www/' + self.domain + '/public_html/index.php', 'w')
		dosya.write('<!doctype html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8">\n\t\t<title>' + self.domain + ' kullanıcısının sitesi açıldı</title>\n\t</head>\n\t<body>\n\t\t<?php echo "Merhaba Dünya"; ?>\n\t</body>\n</html>')
		dosya.close()

	def mysql(self, password):
		if not password:
			password = 'umur5990'

		bag = MySQLdb.connect('localhost', 'root', 'umur5990')
		im = bag.cursor()

		database = self.domain + '_db'

		im.execute('CREATE DATABASE IF NOT EXISTS ' + database + ' CHARACTER SET utf8 COLLATE utf8_general_ci')
		im.execute('GRANT ALL ON ' + database + '.* TO ' + self.domain + '@localhost IDENTIFIED BY \'' + password + '\'')
		im.execute('FLUSH PRIVILEGES')

		bag.commit()
		bag.close()

	def delete_mysql(self):
		bag = MySQLdb.connect('localhost', 'root', 'umur5990')
		im = bag.cursor()

		database = self.domain + '_db'

		im.execute('CREATE DATABASE IF NOT EXISTS ' + database)
		im.execute('GRANT USAGE ON ' + database + '.* TO ' + self.domain + '@localhost')
		im.execute('DROP DATABASE ' + database)
		im.execute('DROP USER ' + self.domain + '@localhost')
		im.execute('FLUSH PRIVILEGES')

		bag.commit()
		bag.close()

	def django_settings(self):
		system('django-admin.py startproject ' + self.domain + ' /var/www/' + self.domain)
		
		dosya = open('/var/www/' + self.domain + '/' + self.domain + '/wsgi.py', 'w')
		dosya.write("import sys\nsys.path.append('/var/www')\nsys.path.append('/var/www/" + self.domain + "')\nsys.path.append('/var/www/" + self.domain + "/" + self.domain + "')\n\nimport os\nos.environ.setdefault('DJANGO_SETTINGS_MODULE', '" + self.domain + ".settings')\n\nfrom django.core.wsgi import get_wsgi_application\napplication = get_wsgi_application()")
		dosya.close()

	def settings(self):
		system('a2ensite ' + self.domain + '.loc')
		system('chmod -R 777 /var/www/' + self.domain)
		system('chown -R ugorur:www-data /var/www/' + self.domain)

	def delete_settings(self):
		system('a2dissite ' + self.domain + '.loc')
		system('rm -Rf /etc/apache2/sites-available/' + self.domain + '.loc.conf')

	def restart(self):
		system('service apache2 restart')
		system('service nscd restart')
		
		exit()

	def hosts(self):
		dosya = open('/etc/hosts', 'a')
		dosya.write('\n127.0.0.1\t' + self.domain + '.loc\twww.' + self.domain + '.loc')
		dosya.close()

	def kontrol(self):
		if not self.domain:
	 		print '\033[1m\033[91mHATA:\033[0m Domain adı olmadan olmaz!!!\033[1m\033[91m!!!\033[0m'
	 		exit()

		if path.isdir('/var/www/' + self.domain):
			print '\033[1m\033[91mHATA:\033[0m Bu adres daha önce kullanılmış\033[1m\033[91m!!!\033[0m'
			exit()

	def delete_dirs(self):
		system('rm -Rf /var/www/' + self.domain)

	def delete_hosts(self):
		dosya = open('/etc/hosts', 'r')
		lines = dosya.readlines()
		dosya.close()

		dosya = open('/etc/hosts', 'w')
		for line in lines:
			if line != '127.0.0.1\t' + self.domain + '.loc\twww.' + self.domain + '.loc' or line != '127.0.0.1\t' + self.domain + '.loc\twww.' + self.domain + '.loc\n':
				dosya.write(line)
		dosya.close()

if __name__ == '__main__':
	host = Host()