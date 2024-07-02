# Gambaran Proyek

Proyek ini terdiri dari beberapa skrip Python dan file JSON, masing-masing memiliki tujuan yang berbeda mulai dari aplikasi web menggunakan Flask hingga aplikasi desktop PyQt5. Di bawah ini adalah deskripsi singkat dari setiap file dan fungsinya.

## Deskripsi File

### act1.py
Skrip ini menunjukkan penggunaan threading di Python. Skrip ini membuat daftar provinsi dan mencetak nama setiap provinsi dengan jeda 1 detik menggunakan beberapa thread.

```python:act1.py
startLine: 1
endLine: 40
```

### act2.py
Skrip ini membaca file JSON (`act2.json`) dan mencetak detail mahasiswa seperti nama, NPM, kelas, fakultas, dan jurusan.

```python:act2.py
startLine: 1
endLine: 14
```

### act2.json
File JSON yang berisi array objek mahasiswa dengan detail seperti nama, NPM, kelas, fakultas, dan jurusan.

```json:act2.json
startLine: 1
endLine: 24
```

### act3.py
Aplikasi web Flask sederhana dengan dua rute:
- `/`: Mengembalikan pesan selamat datang.
- `/data`: Mengembalikan string dengan nama dan NPM seorang mahasiswa.

```python:act3.py
startLine: 1
endLine: 16
```

### act3v2.py
Aplikasi web Flask yang merender template HTML (`index.html`) dan mengirimkan data mahasiswa ke dalamnya.

```python:act3v2.py
startLine: 1
endLine: 16
```

### act4.py
Aplikasi web Flask yang mencari mahasiswa berdasarkan nilai yang diberikan di URL dan mengembalikan data mahasiswa yang cocok.

```python:act4.py
startLine: 1
endLine: 24
```

### act4v2.py
Aplikasi web Flask yang menyediakan fungsi pendaftaran dan login pengguna. Menyimpan akun pengguna dalam sebuah dictionary.

```python:act4v2.py
startLine: 1
endLine: 39
```

### act5.py
Aplikasi web Flask yang mengelola data mahasiswa. Menyediakan rute untuk:
- Mendapatkan semua mahasiswa atau menambahkan mahasiswa baru.
- Mendapatkan, memperbarui, atau menghapus mahasiswa berdasarkan NPM.

```python:act5.py
startLine: 1
endLine: 88
```

### act6.py
Aplikasi desktop PyQt5 untuk mengelola aktivitas pembelajaran. Memungkinkan pengguna untuk menambah, mengedit, dan menghapus aktivitas.

```python:act6.py
startLine: 1
endLine: 97
```

### act7.py
File ini saat ini kosong dan tidak mengandung kode apa pun.

```python:act7.py
startLine: 1
endLine: 2
```

## Cara Menjalankan

### Aplikasi Flask
1. Instal Flask:
    ```bash
    pip install Flask
    ```
2. Jalankan aplikasi Flask:
    ```bash
    python <nama_file>.py
    ```

### Aplikasi PyQt5
1. Instal PyQt5:
    ```bash
    pip install PyQt5
    ```
2. Jalankan aplikasi PyQt5:
    ```bash
    python act6.py
    ```

## Catatan
- Pastikan Anda telah menginstal dependensi yang diperlukan sebelum menjalankan skrip.
- Direktori `templates` harus berisi file `index.html` untuk aplikasi Flask yang merender template.
- Direktori `static` disediakan untuk file statis seperti CSS dan JavaScript, jika diperlukan.