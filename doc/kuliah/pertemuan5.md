# CREAT SHAPEFIE

## Latar Belakang Masalah
Pada Sistem Infomasi Geografis mempunyai 2 garis, yaitu data raster dan data vector. Data raster merupakan cara untuk menentukan tata suatu letak wilayah pada permukaan bumi, sedangkan data vektor merupakan cara menentukan letak wilayah baik atas, bawah, dan juga penentuan berapa jumlah kota dalam suatu lokasi yang ada di permukaan bumi dengan cara menggunakan titik, garis, dan polygon. Cara yang kita gunakan pada penentuan jumlah kota pada suatu lokasi menggunakan python karen tergolong mudah dan sederhana.
# ISI
Shapefile dibagi menjadi dua bagian:
1. File/ Geometri
2. Dbf ( tabel identifikasi geometri)
 
SHP merupakan salah satu file yang berada didalam shapefile yang menyimpan data geometri.
Didalam file shp terdapat beberapa data seperti:
dalam shp dibagi menjadi 4 : 




1. Bbox adalah sebuah boundary box (koordinat 4 titik) atau koordinat batas view yang ada pada peta.
 

2. Part ialah apakah record ini bagian dari record lain/ precahan relasi
3. Point adalah titik suatu koordinat
4. Shapetype adalah jenis data geometri yang mempunyai standar nomor yang ditetapkan oleh ESRI

DBF adalah sebuah file yang menyimpan file tabular yang menyimpan data attribut.

## Method dari DBF
fields
record(n)
Record (n) baris ke (n) records

## Geometri
Data koordinat yang membentuk bangun datar/ruang diantaranya:
1. Point/titik [1]
2. Line/garis [3] Shape,type
3. Polygon [5]


Operasi Pengambilan Data
Library pyshp class shapefile
1. Buka/baca
   
# PENUTUP
## Kesimpulan
Kesimpulan dari penulisan karya tulis ini adalah untuk mengetahui bagaimana cara penggunaan class dan method method dalam memanipulasi retrieve data seperti contoh diatasm menampilan record dari sebuah negara dengan pemanfaatan class dan method.

## Saran
Alangkah baiknya adanya praktek, supaya kita bisa lebih mudah paham. 
Nama : Tentri May Simbolon
Npm : 1144027
Kelas : D4 Teknik Informatika 3C
Kampus : Politeknik Pos Indonesia

Link Github:

Referensi : https://pypi.python.org/pypi/pyshp/1.1.4 


Link Plagiarisme
Smallseotools : https://drive.google.com/open?id=0B7tQon2iaQFdTHEzM1QyTmNXUnc
Duplichecker: https://drive.google.com/open?id=0B7tQon2iaQFdZU82M1FKU2NlcTQ

