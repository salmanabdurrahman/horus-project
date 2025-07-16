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
    python run.py
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

3.  **Jalankan development server**:

    ```bash
    npm run dev
    ```

4.  **Akses aplikasi di browser**:
    Buka browser Anda dan navigasi ke `http://localhost:5173` (atau port lain yang ditampilkan di terminal Anda).
