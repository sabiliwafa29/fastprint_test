# DOKUMENTASI LENGKAP - FASTPRINT TEST

## 📚 Daftar Isi
1. [Penjelasan Project](#penjelasan-project)
2. [Teknologi yang Digunakan](#teknologi-yang-digunakan)
3. [Struktur Database](#struktur-database)
4. [Instalasi & Setup](#instalasi--setup)
5. [Cara Menjalankan](#cara-menjalankan)
6. [Fitur-Fitur](#fitur-fitur)
7. [Testing](#testing)
8. [Screenshot](#screenshot)

---

## Penjelasan Project

Project ini adalah aplikasi CRUD (Create, Read, Update, Delete) untuk manajemen produk yang mengambil data dari API Fastprint. Aplikasi ini dibuat menggunakan Django Framework dengan fitur-fitur:

- Import data produk dari API
- Tampilkan semua produk
- Filter produk berdasarkan status "bisa dijual"
- Tambah, edit, dan hapus produk
- Validasi form (nama produk wajib diisi, harga harus angka)
- Konfirmasi alert sebelum hapus
- Menggunakan Django Serializer untuk validasi data

---

## Teknologi yang Digunakan

### Backend
- **Python 3.8+**
- **Django 4.2.7** - Web framework
- **Django REST Framework 3.14.0** - Untuk serializer dan validasi
- **Requests 2.31.0** - Untuk komunikasi dengan API

### Database
- **PostgreSQL 12+** atau **MySQL 8+**

### Frontend
- **Bootstrap 5.3** - CSS framework
- **Font Awesome 6.4** - Icons
- **JavaScript** - Client-side validation

---

## Struktur Database

### 1. Tabel `kategori`
```sql
CREATE TABLE kategori (
    id_kategori SERIAL PRIMARY KEY,
    nama_kategori VARCHAR(255) UNIQUE NOT NULL
);
```

### 2. Tabel `status`
```sql
CREATE TABLE status (
    id_status SERIAL PRIMARY KEY,
    nama_status VARCHAR(100) UNIQUE NOT NULL
);
```

### 3. Tabel `produk`
```sql
CREATE TABLE produk (
    id_produk SERIAL PRIMARY KEY,
    nama_produk VARCHAR(255) NOT NULL,
    harga DECIMAL(10, 2) NOT NULL,
    kategori_id INTEGER REFERENCES kategori(id_kategori),
    status_id INTEGER REFERENCES status(id_status)
);
```

### Relasi:
- `produk.kategori_id` → `kategori.id_kategori` (Foreign Key)
- `produk.status_id` → `status.id_status` (Foreign Key)

---

## Instalasi & Setup

### A. Prerequisites
Pastikan sudah terinstall:
- Python 3.8 atau lebih baru
- PostgreSQL atau MySQL
- Git

### B. Clone Repository
```bash
git clone <repository-url>
cd fastprint_test
```

### C. Setup Database

#### PostgreSQL:
```bash
# Login sebagai postgres
sudo -u postgres psql

# Buat database dan user
CREATE DATABASE fastprint_db;
CREATE USER fastprint_user WITH PASSWORD 'password123';
ALTER ROLE fastprint_user SET client_encoding TO 'utf8';
ALTER ROLE fastprint_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE fastprint_user SET timezone TO 'Asia/Jakarta';
GRANT ALL PRIVILEGES ON DATABASE fastprint_db TO fastprint_user;

\q
```

#### MySQL:
```bash
# Login sebagai root
mysql -u root -p

# Buat database dan user
CREATE DATABASE fastprint_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'fastprint_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON fastprint_db.* TO 'fastprint_user'@'localhost';
FLUSH PRIVILEGES;

EXIT;
```

### D. Setup Project

#### Windows:
```batch
# Jalankan setup script
setup.bat
```

#### Linux/Mac:
```bash
# Berikan permission
chmod +x setup.sh

# Jalankan setup script
./setup.sh
```

#### Manual Setup:
```bash
# 1. Buat virtual environment
python -m venv venv

# 2. Aktivasi virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy .env file
cp .env.example .env

# 5. Edit .env sesuai konfigurasi database Anda
# Buka file .env dan sesuaikan:
# - DB_ENGINE (postgresql atau mysql)
# - DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

# 6. Jalankan migrations
python manage.py makemigrations
python manage.py migrate
```

---

## Cara Menjalankan

### 1. Import Data dari API
```bash
python manage.py import_products
```

Output:
```
Memulai import data dari API...
Menghubungi API...
Berhasil mendapat 30 produk dari API

Berhasil import data:
- Kategori baru: 15
- Status baru: 2
- Produk baru: 30
- Total produk di database: 30
```

### 2. Buat Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 3. Jalankan Development Server
```bash
python manage.py runserver
```

Akses aplikasi di: `http://127.0.0.1:8000/`

Admin panel: `http://127.0.0.1:8000/admin/`

---

## Fitur-Fitur

### 1. Halaman Utama - List Semua Produk
**URL:** `/`

**Fitur:**
- Tampilkan semua produk dalam tabel
- Menampilkan: ID, Nama Produk, Harga, Kategori, Status
- Badge warna untuk status (hijau: bisa dijual, merah: tidak bisa dijual)
- Tombol Edit dan Hapus untuk setiap produk
- Tombol filter ke halaman "Bisa Dijual"
- Tombol "Tambah Produk"

### 2. Halaman Produk Bisa Dijual
**URL:** `/bisa-dijual/`

**Fitur:**
- Filter otomatis menampilkan hanya produk dengan status "bisa dijual"
- Interface sama dengan halaman utama
- Tombol kembali ke "Lihat Semua Produk"

### 3. Halaman Tambah Produk
**URL:** `/tambah/`

**Fitur:**
- Form untuk tambah produk baru
- Field: Nama Produk, Harga, Kategori, Status
- **Validasi:**
  - Nama produk: wajib diisi (tidak boleh kosong)
  - Harga: wajib diisi, harus berupa angka positif
  - Kategori: wajib dipilih
  - Status: wajib dipilih
- Validasi dilakukan di backend (Django Form) dan frontend (JavaScript)
- Menggunakan Serializer untuk validasi tambahan

### 4. Halaman Edit Produk
**URL:** `/edit/<id_produk>/`

**Fitur:**
- Form pre-filled dengan data produk yang dipilih
- Validasi sama seperti form tambah
- Update data produk ke database

### 5. Fitur Hapus Produk
**URL:** `/hapus/<id_produk>/`

**Fitur:**
- Konfirmasi dialog dengan JavaScript `confirm()`
- Menampilkan nama produk yang akan dihapus
- Hanya hapus jika user konfirmasi "OK"
- Redirect ke halaman utama setelah berhasil

---

## Testing

### Menjalankan Unit Tests
```bash
python manage.py test
```

### Test Coverage:
- Model tests (Kategori, Status, Produk)
- View tests (Index, Bisa Dijual, Tambah, Edit)
- Form validation tests

---

## Screenshot

### 1. Halaman Utama
- Tabel responsif dengan Bootstrap
- Filter dan tombol aksi

### 2. Form Tambah/Edit
- Form dengan validasi
- Error messages untuk input tidak valid

### 3. Konfirmasi Hapus
- Alert box konfirmasi sebelum hapus

### 4. Filter Bisa Dijual
- Hanya menampilkan produk dengan status "bisa dijual"

---

## API Integration

### Endpoint API Fastprint
```
URL: https://recruitment.fastprint.co.id/tes/api_tes_programmer
Method: POST
Content-Type: application/x-www-form-urlencoded

Body:
- username: tesprogrammer030226C18
- password: [MD5 hash dari bisacoding-3-2-26]
```

### Response Format:
```json
{
    "error": 0,
    "version": "220523.0.1",
    "data": [
        {
            "no": "7",
            "id_produk": "6",
            "nama_produk": "Product Name",
            "kategori": "Category Name",
            "harga": "12500",
            "status": "bisa dijual"
        }
    ]
}
```

---

## Troubleshooting

### 1. Error Database Connection
- Pastikan database sudah dibuat
- Cek konfigurasi di file `.env`
- Pastikan database service sedang running

### 2. Error Import Products
- Pastikan koneksi internet aktif
- Cek kredensial API di `.env`
- Pastikan format password MD5 benar

### 3. Error Migration
```bash
# Reset migrations (hati-hati, akan hapus data!)
python manage.py migrate products zero
python manage.py makemigrations products
python manage.py migrate
```

---

## File Structure

```
fastprint_test/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── products/
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── import_products.py
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── products/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
├── setup.sh
├── setup.bat
├── README.md
└── DOKUMENTASI.md
```

---

## Submission Checklist

- [x] Django Framework digunakan
- [x] PostgreSQL/MySQL sebagai database
- [x] 3 Tabel (Produk, Kategori, Status) dengan relasi
- [x] Import data dari API
- [x] Tampilkan semua produk
- [x] Filter produk "bisa dijual"
- [x] CRUD (Create, Read, Update, Delete)
- [x] Validasi form (nama wajib, harga angka)
- [x] Konfirmasi alert sebelum hapus
- [x] Menggunakan Serializer
- [x] Dokumentasi lengkap
- [x] README.md
- [x] .gitignore
- [x] Setup scripts

---

## Author
[Nama Anda]
[Email Anda]

## License
MIT License - Free to use for educational purposes
