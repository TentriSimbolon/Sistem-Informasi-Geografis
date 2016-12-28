# Resume Pertemuan 6 Sistem Informasi Geografis

## Latar Belakang Masalah
1.	Pengertian MapServer
2.	Langkah-langkah install MapServer
3.	Pengertian MapProxy
4.	Langkah-langkah install MapProxy
5.	Cara Testing

## Pengertian MapServer
MapServer adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG. MapServer pertama kali dikembangkan oleh University of Minnesota, namun sekarang MapServer sudah dikelola oleh pengembang diseluruh dunia. MapServer berjalan pada semua sistem operasi utama dan akan bekerja dengan semua web server. MapServer memiliki Mapscript yang mendukung banyak bahasa populer seperti PHP, Python, Perl, C# dan Java. Menggunakan Mapscript membuatnya cepat dan mudah untuk membangun aplikasi web geospasial yang kompleks.

## Langkah-langkah install MapServer
Langkah instalasi MapServer melalui repository elgis dengan menambahkan repository elgis terlebih dahulu, repository elgis juga membutuhkan repository epel.
~~~
# rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# rpm -Uvh http://elgis.argeo.org/repos/6/elgis-release-6-6_0.noarch.rpm
~~~

Edit file epel.repo tambahkan exclude=armadillo :
~~~
# vi /etc/yum.repos.d/epel.repo
~~~

Instalasi wget :
~~~
# yum install wget
~~~

Instalasi armadillo :
~~~
# wget http://elgis.argeo.org/repos/6/elgis/x86_64/gdal-1.9.2-4.el6.x86_64.rpm
# wget http://proj.badc.rl.ac.uk/cedaservices/raw-attachment/ticket/670/armadillo-3.800.2-1.el6.x86_64.rpm
# yum install armadillo-3.800.2-1.el6.x86_64.rpm
~~~

kemudian lanjutkan proses instalasi :
~~~
# yum install gpsbabel
# yum install gdal
# yum install mapserver
# yum install glibc
# yum install libpng libpng-devel
# yum install gd gd-devel
# yum install giflib-devel
# yum install proj-epsg
# rpm -ql mapserver
# /usr/libexec/mapserver -v
~~~

## Pengertian MapProxy
Map Proxy adalah program yang berfungsi untuk menampung hasil gambar dari map server agar konsumsi komputer bisa di reduksi.

## Langkah-langkah install MapProxy
Langkah instalasi MapProxy :
~~~
# yum install python-pip python-devel
# pip install MapProxy
~~~

## Cara Testing
1. Download peta Indonesia beserta map proxy konfigurasinya di Halaman Download simpan di folder/var 
2. Jalankan map proxy dengan cara ketik perintah #vwsqi map proxy ini 
3. Peta seudah bisa diakses di browser localhost


## Kesimpulan
MapServer adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan.

## Saran
Harus memaksimalkan praktikum

* Nama : Tentri May Simbolon
* Npm : 1144027
* Kelas : D4 Teknik Informatika 3C
* Kampus : Politeknik Pos Indonesia