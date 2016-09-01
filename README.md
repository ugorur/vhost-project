Ubuntu için Apache Virtual Host Yönetim Projesi
===============================================

Kurulum
_______

Programı kendi makinamıza klonluyoruz.

```bash
git clone https://github.com/ugorur/vhost-project.git
```
Klonladığımız dizine girerek kurulumu tamamlıyoruz.

Kurulum sırasında bizden istediği bilgiler ve anlamları:
 * MySQL Roots Şifresi Giriniz: Gerekli paketleri kurarken girdiğiniz MySQL Server Root şifresi
 * E-Posta Adresinizi Giriniz: Zorunlu değil, HTTP 500 hata sayfalarında görünür.
 * Linux Kullanıcı Adınızı Giriniz: Açılan Virtual Host'lar için dosya kopyalama falan yaparken sıkıntı yaşamamanız için gerekli
 * Varsayılan Alan Adı Uzantınızı Giriniz: Her Virtual Host için tek tek girmek yerine, ilk seferde girmeniz size zaman kazandırır. Varsayılan olarak ** loc ** değeri tanımlıdır.
 * Hata Ayıklama Açılsın mı? (E/H): Django için yeni bir host açılınca hata ayıklama modu için gerekli. Diğer paketlerde henüz işlevi yoktur.

```bash
cd vhost-project
sudo chmod +x setup.py
sudo ./setup.py install
```

Kurulum tamamlandıktan sonra sistemi kullanmak için tek yapmanız gereken sudo ile vhost'u çalıştırmak olacaktır.

** PHP için Kullanım **

Yeni PHP Virtual Host Açmak:

```bash
sudo vhost php ekle
```

 * Kullanıcı Adı: Host için kullanıcı adı. Domain adresi ile aynı özelliklere sahip olmalı. ** Uzantı vermeyin. **
 * Uzantı: Varsayılan olarak kurulumda verdiğiniz uzantıdır. Bu uzantı sizin Virtual Hostunuz için adres olacaktır. (www.{kullanici_adi}.{uzanti})
 * Şifre: Varsayılan olarak MySQL Root şifresidir. Bu şifre, bu virtual host için açılan database için kullanılır. (Database Adı: {kullanici_adi}_db, Database Kullanıcısı: {kullanici_adi}, Database Şifre: {sifre})
 * Hata Ayıklama Açılsın mı? (E/H): (PHP için fark etmez)

Ayrıca www.{kullanici_adi}.{uzanti}/phpmyadmin ile bu kullanıcıya özgü phpmyadmin sayfasına giriş yapabilirsiniz.

PHP Virtual Host Silmek:

```bash
sudo vhost php sil
```

 * Kullanıcı Adı: Host için kullanıcı adı.
 * Uzantı: Virtual Host için verdiğiniz uzantı
