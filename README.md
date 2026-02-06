===========================================================================================
===========================================================================================

Jawaban Tugas Analisis 1–6 
Analisis 1

Kalau hero1.hp diubah jadi 500 setelah objek dibuat, nilainya langsung ikut berubah. Karena atribut itu milik objek dan bisa diakses bebas. Jadi print(hero1.hp) bakal nampilin 500.

Analisis 2

Parameter lawan itu objek utuh, bukan sekadar nama. Ini penting karena kita bisa langsung akses data dan method lawan (HP, diserang, dll). Kalau cuma string, objeknya nggak bisa berinteraksi.

Analisis 3

Saat super() dihapus, atribut dari class Hero (seperti name) nggak ikut dibuat. Makanya muncul error object has no attribute. Fungsi super() itu penghubung supaya data dari parent ikut dipakai di child.

Analisis 4

HP masih bisa muncul walau private karena Python pakai name mangling. Tapi ini nggak disarankan karena melanggar konsep keamanan data.

Tanpa validasi di setter, HP bisa jadi negatif. Setter penting biar data tetap masuk akal dan nggak rusak.

Analisis 5

Error muncul karena Hero belum memenuhi kontrak dari abstract class. Artinya janji method belum ditepati.

Abstract class memang bukan buat objek nyata, tapi sebagai kerangka biar class turunan rapi dan konsisten.

Analisis 6

Program tetap jalan walau ditambah Healer, ini bukti polymorphism bikin kode gampang dikembangin.

Kalau nama method beda, program error. Di polymorphism, nama method harus sama supaya bisa dipanggil dengan cara yang sama.

===========================================================================================
===========================================================================================

E. Rangkuman Istilah

Bagian ini berisi rangkuman istilah utama yang digunakan dalam pembuatan program TechMaster dengan konsep Object Oriented Programming (OOP) menggunakan Python. Penjelasan dibuat singkat agar mudah dipahami.

1. Class

Class adalah cetakan atau blueprint yang digunakan untuk membuat object. Class berisi atribut dan method yang akan dimiliki oleh object.

2. Object

Object adalah hasil nyata dari class yang sudah dibuat. Object dapat digunakan untuk menjalankan method dan menyimpan data.

3. Inheritance

Inheritance adalah konsep pewarisan fitur dari class induk ke class anak, sehingga class anak dapat menggunakan atribut dan method milik class induk.

4. Encapsulation

Encapsulation adalah konsep melindungi data agar tidak bisa diakses langsung dari luar class. Biasanya menggunakan atribut bersifat private.

5. Polymorphism

Polymorphism adalah kemampuan satu nama method yang sama untuk memiliki perilaku yang berbeda pada class yang berbeda.

6. Abstraction

Abstraction adalah konsep penyederhanaan dengan hanya menampilkan fungsi penting, sementara detail implementasi disembunyikan.

7. Interface

Interface berfungsi sebagai kontrak method yang harus dimiliki oleh class, sehingga komunikasi antar object menjadi lebih terstruktur dan konsisten.

===========================================================================================
===========================================================================================