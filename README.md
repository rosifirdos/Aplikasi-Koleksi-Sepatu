# Aplikasi Manajemen Koleksi Sepatu (UAS PBO)

Aplikasi sederhana untuk mengelola koleksi sepatu, dikembangkan sebagai bagian dari Ujian Akhir Semester (UAS) mata kuliah Pemrograman Berorientasi Objek. Aplikasi ini mengimplementasikan konsep-konsep OOP seperti Class & Object, Enkapsulasi, Inheritance, dan Polymorphism, serta dibangun dengan antarmuka grafis menggunakan PyQt5.

## Daftar Isi
- [Tujuan Proyek](#tujuan-proyek)
- [Fitur](#fitur)
- [Konsep OOP yang Diterapkan](#konsep-oop-yang-diterapkan)
- [Class Diagram](#class-diagram)
- [Struktur Proyek](#struktur-proyek)
- [Cara Menjalankan](#cara-menjalankan)
- [Kredit](#kredit)

## Tujuan Proyek
Proyek ini bertujuan untuk mendemonstrasikan pemahaman dan implementasi konsep-konsep dasar Pemrograman Berorientasi Objek dalam sebuah aplikasi manajemen data sederhana dengan antarmuka grafis. Tema yang dipilih adalah "Koleksi Barang" dengan fokus pada Sepatu.

## Fitur
- Menambahkan sepatu ke dalam koleksi (Sepatu Umum, Sepatu Olahraga, Sepatu Casual).
- Menampilkan daftar sepatu yang ada dalam koleksi.
- Mengklasifikasikan sepatu berdasarkan jenisnya (Olahraga, Casual) dengan atribut spesifik.

## Konsep OOP yang Diterapkan
Aplikasi ini mengimplementasikan konsep-konsep OOP sebagai berikut:
1.  **Class & Object**: Definisi class `Sepatu`, `SepatuOlahraga`, `SepatuCasual`, dan pembuatan objek-objek dari class tersebut.
2.  **Enkapsulasi**: Penggunaan atribut private (ditandai dengan `__` di awal nama atribut) dan metode getter publik untuk mengaksesnya.
3.  **Inheritance**: Class `SepatuOlahraga` dan `SepatuCasual` mewarisi properti dan perilaku dari class `Sepatu`.
4.  **Polymorphism**: Metode `display_info()` di-override pada class turunan (`SepatuOlahraga` dan `SepatuCasual`) untuk memberikan detail informasi yang berbeda sesuai jenis sepatu.
5.  **Modularisasi**: Kode dipecah menjadi beberapa modul (misalnya `models` untuk class-class objek, `gui` untuk antarmuka pengguna) untuk organisasi yang lebih baik.
6.  **GUI Python**: Antarmuka pengguna grafis dibangun menggunakan pustaka `PyQt5`.

## Class Diagram
Berikut adalah representasi class diagram proyek ini:

```mermaid
classDiagram
    class Sepatu {
        -String _merk
        -String _model
        -Float _ukuran
        -String _warna
        +__init__(merk, model, ukuran, warna)
        +get_merk() String
        +get_model() String
        +get_ukuran() Float
        +get_warna() String
        +display_info() String
    }

    class SepatuOlahraga {
        -String _tipe_olahraga
        -String _fitur_khusus
        +__init__(merk, model, ukuran, warna, tipe_olahraga, fitur_khusus)
        +get_tipe_olahraga() String
        +get_fitur_khusus() String
        +display_info() String
    }

    class SepatuCasual {
        -String _material
        -String _gaya
        +__init__(merk, model, ukuran, warna, material, gaya)
        +get_material() String
        +get_gaya() String
        +display_info() String
    }

    Sepatu <|-- SepatuOlahraga : Inherits
    Sepatu <|-- SepatuCasual : Inherits

```markdown
    ## Struktur Proyek
