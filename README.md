# Proyek Horus - Aplikasi User Management

## 📝 Deskripsi

**Proyek Horus** adalah aplikasi web untuk manajemen data pengguna. Terdiri dari dua bagian utama yaitu backend yang menangani data dan autentikasi, serta frontend yang menyediakan tampilan dan interaksi pengguna.

## ✨ Fitur Utama

- **Autentikasi Pengguna:** Registrasi dan login dengan keamanan dasar.
- **Akses Terproteksi:** Hanya pengguna terautentikasi yang dapat mengakses halaman tertentu.
- **Manajemen Data Pengguna:** Tambah, lihat, ubah, dan hapus data pengguna.
- **Pencarian & Pengurutan:** Fitur pencarian dan pengurutan data pengguna.
- **Desain Responsif:** Tampilan yang menyesuaikan berbagai perangkat.
- **Notifikasi Interaktif:** Umpan balik aksi pengguna melalui notifikasi.

## ⚙️ Setup Database

Sebelum menjalankan backend, siapkan database MySQL Anda terlebih dahulu.

### 1. Buat Database

Buka tools database Anda (phpMyAdmin, DBeaver, dll) dan jalankan perintah SQL berikut:

```sql
CREATE DATABASE horus_salman_db
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. Buat Tabel Pengguna (users)

Setelah membuat database, pilih database tersebut dan jalankan perintah SQL ini untuk membuat tabel yang dibutuhkan:

```sql
CREATE TABLE `users` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `users_email_unique` (`email`),
    UNIQUE KEY `users_username_unique` (`username`)
);
```

## ⚙️ Cara Menjalankan Proyek

Untuk menjalankan proyek ini secara penuh, Anda perlu menjalankan **backend** dan **frontend** secara bersamaan di dua terminal terpisah.

### **1. Backend (Flask API)**

1.  **Buka terminal pertama** dan masuk ke direktori backend:

    ```bash
    cd backend
    ```

2.  **Buat dan aktifkan virtual environment**:

    ```bash
    # Membuat venv
    python -m venv venv

    # Mengaktifkan venv (contoh untuk Git Bash di Windows)
    source venv/Scripts/activate
    ```

3.  **Install semua dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Environment**:

      - Salin file `.env.example` menjadi `.env`.
      - Sesuaikan detail koneksi database (`DB_USERNAME`, `DB_PASSWORD`, dll) di dalam file `.env`.
      - Pastikan Anda sudah membuat database `horus_salman_db` di MySQL (nama database dapat disesuaikan).

5.  **Jalankan server backend**:

    ```bash
    python run.py atau venv/Scripts/python run.py
    ```

    > API akan berjalan di `http://127.0.0.1:5000`.

### **2. Frontend (Vue App)**

1.  **Buka terminal kedua** dan masuk ke direktori frontend:

    ```bash
    cd frontend
    ```

2.  **Install semua dependencies**:

    ```bash
    npm install
    ```

3.  **Konfigurasi Environment**:

    - Salin file `.env.example` menjadi `.env`.
    - Sesuaikan variabel berikut pada file `.env`:
      ```
      VITE_API_BASE_URL=http://127.0.0.1:5000/api
      ```
    - Pastikan URL di atas sesuai dengan alamat api backend Flask Anda.

4.  **Jalankan development server**:

    ```bash
    npm run dev
    ```

5.  **Akses aplikasi di browser**:
    Buka browser Anda dan navigasi ke `http://localhost:5173` (atau port lain yang ditampilkan di terminal Anda).
