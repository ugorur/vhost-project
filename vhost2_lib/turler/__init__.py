#!/usr/bin/env python
#-*-coding:utf-8-*-

from os import makedirs, system

class Tur (object):

	_index = """<!doctype html>
<html>
	<head>
		<meta charset="utf-8">
		<title>%(kullanici)s kullanıcısının sitesi açıldı</title>
	</head>
	<body>
		<?php echo "Merhaba Dünya" . PHP_EOL; ?>
	</body>
</html>"""

	def __init__(self, kullanici):
		self.kullanici = kullanici

	def yarat(self, domain, sifre, ha):
		self.dizinler()
		self.index()

	def dizinler(self):
		makedirs('/var/www/' + self.kullanici + '/logs')
		makedirs('/var/www/' + self.kullanici + '/public_html')

	def index(self):
		dosya = open('/var/www/' + self.kullanici + '/public_html/index.php', 'w')
		dosya.write(self._index % {'kullanici': self.kullanici})
		dosya.close()

	def sil(self):
		system('rm -Rf /var/www/' + self.kullanici)

	def yonet(self, komut):
		pass