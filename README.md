### Panduan Menjalankan Aplikasi: 
# Persiapan Lingkungan: 
- Pastikan sudah memiliki Python terinstal di komputer Anda.
- Instal dependensi yang diperlukan dengan menjalankan pip install fastapi[all] faker.

# Menjalankan Aplikasi: 
- Pastikan sudah berada di direktori proyek yang sesuai.
- Jalankan perintah uvicorn main:app --reload.
- Server FastAPI akan berjalan di alamat lokal (biasanya http://127.0.0.1:8000).

# Akses API: 
- Setelah server berjalan, sudah dapat mengakses API melalui browser atau menggunakan alat seperti Postman.
- Endpoint API tersedia di http://localhost:8000/.
- Gunakan endpoint yang sesuai untuk mengambil, menambahkan, memperbarui, atau menghapus data pasien dan reservasi.

### Desain Skema:
# Pasien:
- id (Kunci Utama)
- nama
- email
- nomor_telepon

# Slot Konsultasi:
- id (Kunci Utama)
- tanggal
- waktu
- ketersediaan (boolean)

# Reservasi:
- id (Kunci Utama)
- patient_id (Kunci Asing mengacu pada Pasien)
- consultation_slot_id (Kunci Asing mengacu pada Slot Konsultasi)
- nomor_antrian

### Arsitektur FastAPI 

- Routes Layer: Di FastAPI, rute-rute (routes) API didefinisikan dalam file main.py. Rute-rute ini menentukan endpoint-endpoint HTTP dan menghubungkannya ke fungsi-fungsi yang menjalankan logika bisnis.
- Data Access Layer: Kode untuk berinteraksi dengan database diatur dalam bagian Definisikan model data dan Definisikan API endpoint di dalam file main.py. SQLAlchemy digunakan untuk membuat model-model database (tabel-tabel dan relasi antar-tabel), dan operasi-operasi dasar database, seperti pembacaan, penulisan, pembaruan, dan penghapusan dilakukan menggunakan SQLAlchemy ORM.
- Models Layer: Model-model data yang mewakili struktur database didefinisikan menggunakan SQLAlchemy dalam file yang sama (main.py).
- Pydantic Schemas: menggunakan Pydantic untuk menentukan skema permintaan dan respons API. Ini membantu dalam validasi data yang masuk dan keluar dari API.
- Uvicorn Server: Terakhir, aplikasi dijalankan menggunakan Uvicorn, yang merupakan server web ASGI yang sangat cepat dan efisien.

### Sruktur FastAPI
  - main.py: Ini adalah titik masuk utama untuk aplikasi FastAPI. Di sini, rute-rute API didefinisikan bersama dengan logika untuk mengatur permintaan HTTP dan meresponsnya.
  - models: Direktori ini berisi definisi model-model data yang mewakili struktur database.model-model tersebut didefinisikan menggunakan SQLAlchemy dalam file main.py.
