# Resume Pertemuan 6 Sistem Informasi Geografis

## Latar Belakang Masalah

Dalam Penggunaan Sistem Informasi Geografis, masih banyak diantara kita yang belum mengetahui bagaimana cara menggunakan data pada editor. Pada pertemuan ke-6 Sistem Informasi Geografi ini saya akan menjelaskan bagaimana cara penggunaan editor. Editor berfungsi untuk melakukan editing pada shapefile, yang dimana editor ini bisa membuat CRUD(Create Read Update Delete) pada file shapefile.

## Solusi Materi

Editor berfungsi untuk melakukan editing pada shapefile. Contohmya delete road. Selain editor ada juga Writer, Writer adalah method di shape file untuk membuat file shp baru (shp dan dbt)

Untuk langkag-langkah dalam melakukan editor sebagai berikut :

Import shape file

Sf = shape file.editor(war.shp)

Sf.point(16,10,0,0)

Sf.record (‘padang’)

Sf.save

Sf.save (‘war.shp’)

a=shapefile.reoder(‘war.shp’)

a.recorders()

a.shapes().

a.shape()[0]

a.shape()[0] points

[(10,0,10,0)]

Untuk delete

Sf.delete(0)

a.shapes()[0].points [(10,0,10,0)]

sf.points [16,10,0,0]

sf.record(‘padang’)

sf.saver(‘wr.shp’)

## Kesimpulan

Editor berfungsi untuk melakukan editing pada shapefile. Banyak hal yang dapat dilakukan di editor. Contohmya delete road. Selain editor ada juga Writer, Writer adalah method di shape file untuk membuat file shp baru.

## Saran

Lebih membanyak ilmu dan mencari referensi lain untuk bahan praktek editor di system informasi geografi tentunya ilmu yang langsung implementasi atau praktek agar bisa membuat langsung GIS.

* Nama : Tentri May Simbolon
* Npm : 1144027
* Kelas : D4 Teknik Informatika 3C
* Kampus : Politeknik Pos Indonesia