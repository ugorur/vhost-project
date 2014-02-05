#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import Tur

class PHP (Tur):

	apache = """<VirtualHost %(domain)s>
	ServerAdmin mail@ugorur.com

	ServerName %(domain)s
	ServerAlias www.%(domain)s

	DocumentRoot /var/www/%(kullanici)s/public_html

	Alias /phpmyadmin /var/www/phpmyadmin/public_html

	ErrorLog /var/www/%(kullanici)s/logs/error.log
	CustomLog /var/www/%(kullanici)s/logs/access.log common

	<Directory /var/www/%(kullanici)s/public_html>
		DirectoryIndex index.html index.php
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	<Directory /var/www/phpmyadmin/public_html>
		DirectoryIndex index.php
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>
</VirtualHost>"""

	def __init__(self, kullanici):
		super(PHP, self).__init__(kullanici)
