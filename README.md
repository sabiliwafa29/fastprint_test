# Fastprint Test - Junior Programmer

Aplikasi CRUD manajemen produk dengan integrasi API Fastprint.

## 📋 Requirements

- Python 3.8+
- PostgreSQL 12+ atau MySQL 8+
- pip (Python package manager)

## 🚀 Setup & Installation

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd fastprint_test
```

### 2. Buat Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database

#### PostgreSQL:
```bash
# Login ke PostgreSQL
psql -U postgres

# Buat database
CREATE DATABASE fastprint_db;
CREATE USER fastprint_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE fastprint_db TO fastprint_user;
\q
```

#### MySQL:
```bash
# Login ke MySQL
mysql -u root -p

# Buat database
CREATE DATABASE fastprint_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'fastprint_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON fastprint_db.* TO 'fastprint_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Setup Environment Variables
```bash
# Copy file .env.example ke .env
cp .env.example .env

# Edit file .env sesuai konfigurasi database Anda
```

### 6. Jalankan Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Import Data dari API
```bash
python manage.py import_products
```

### 9. Jalankan Server
```bash
python manage.py runserver
```

Aplikasi akan berjalan di `http://127.0.0.1:8000/`

## 📁 Struktur Database

### Table: Kategori
| Field | Type | Description |
|-------|------|-------------|
| id_kategori | Integer (PK) | Primary key |
| nama_kategori | String(255) | Nama kategori |

### Table: Status
| Field | Type | Description |
|-------|------|-------------|
| id_status | Integer (PK) | Primary key |
| nama_status | String(100) | Nama status |

### Table: Produk
| Field | Type | Description |
|-------|------|-------------|
| id_produk | Integer (PK) | Primary key |
| nama_produk | String(255) | Nama produk |
| harga | Decimal(10,2) | Harga produk |
| kategori_id | Integer (FK) | Foreign key ke Kategori |
| status_id | Integer (FK) | Foreign key ke Status |

## 🎯 Fitur

- ✅ Import data produk dari API Fastprint
- ✅ Tampilkan semua produk
- ✅ Filter produk berdasarkan status "bisa dijual"
- ✅ Tambah produk baru dengan validasi form
- ✅ Edit produk dengan validasi form
- ✅ Hapus produk dengan konfirmasi alert
- ✅ Serializer untuk validasi data

## 🔗 URL Endpoints

| URL | Description |
|-----|-------------|
| `/` | Halaman utama (list produk) |
| `/bisa-dijual/` | List produk yang bisa dijual |
| `/tambah/` | Form tambah produk |
| `/edit/<id>/` | Form edit produk |
| `/hapus/<id>/` | Hapus produk |

## 👨‍💻 Author

Rosyad Wafa