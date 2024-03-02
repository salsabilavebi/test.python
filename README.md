# Panduan Menjalankan Aplikasi: 
### Persiapan Lingkungan: 
- Pastikan sudah memiliki Python terinstal di komputer Anda.
- Instal dependensi yang diperlukan dengan menjalankan pip install fastapi[all] faker.

### Menjalankan Aplikasi: 
- Pastikan sudah berada di direktori proyek yang sesuai.
- Jalankan perintah uvicorn main:app --reload.
- Server FastAPI akan berjalan di alamat lokal (biasanya http://127.0.0.1:8000).

### Akses API: 
- Setelah server berjalan, sudah dapat mengakses API melalui browser atau menggunakan alat seperti Postman.
- Endpoint API tersedia di http://localhost:8000/.
- Gunakan endpoint yang sesuai untuk mengambil, menambahkan, memperbarui, atau menghapus data pasien dan reservasi.

# Desain Skema:
### Pasien:
- id (Kunci Utama)
- nama
- email
- nomor_telepon

### Slot Konsultasi:
- id (Kunci Utama)
- tanggal
- waktu
- ketersediaan (boolean)

### Reservasi:
- id (Kunci Utama)
- patient_id (Kunci Asing mengacu pada Pasien)
- consultation_slot_id (Kunci Asing mengacu pada Slot Konsultasi)
- nomor_antrian

# Arsitektur FastAPI 

- Routes Layer: Di FastAPI, rute-rute (routes) API didefinisikan dalam file main.py. Rute-rute ini menentukan endpoint-endpoint HTTP dan menghubungkannya ke fungsi-fungsi yang menjalankan logika bisnis.
- Data Access Layer: Kode untuk berinteraksi dengan database diatur dalam bagian Definisikan model data dan Definisikan API endpoint di dalam file main.py. SQLAlchemy digunakan untuk membuat model-model database (tabel-tabel dan relasi antar-tabel), dan operasi-operasi dasar database, seperti pembacaan, penulisan, pembaruan, dan penghapusan dilakukan menggunakan SQLAlchemy ORM.
- Models Layer: Model-model data yang mewakili struktur database didefinisikan menggunakan SQLAlchemy dalam file yang sama (main.py).
- Pydantic Schemas: menggunakan Pydantic untuk menentukan skema permintaan dan respons API. Ini membantu dalam validasi data yang masuk dan keluar dari API.
- Uvicorn Server: Terakhir, aplikasi dijalankan menggunakan Uvicorn, yang merupakan server web ASGI yang sangat cepat dan efisien.

# Sruktur FastAPI
  - main.py: Ini adalah titik masuk utama untuk aplikasi FastAPI. Di sini, rute-rute API didefinisikan bersama dengan logika untuk mengatur permintaan HTTP dan meresponsnya.
  - models: Direktori ini berisi definisi model-model data yang mewakili struktur database.model-model tersebut didefinisikan menggunakan SQLAlchemy dalam file main.py.

# Dokumentasi 

### POST - membuat Patient:
- Endpoint: http://127.0.0.1:8000/patients/
- Metode: POST
- Body: Data JSON untuk membuat pasien baru (nama, email, nomor telepon).
- Response:
  {
    "name": "salsa",
    "email": "salsabilavebi68@gmail.com",
    "phone_number": "081271592009"
}

### POST - Membuat Consultation Slot:
- Endpoint: http://127.0.0.1:8000/consultation_slots/
- Metode: POST
- Body: Data JSON untuk membuat slot konsultasi baru (tanggal, waktu, ketersediaan).
- Response:
  {
   "date": "2024-03-03",
    "time": "10:00",
    "availability": true
}
  
### POST - Membuat Reservation for Patient:
- Endpoint: http://127.0.0.1:8000/patients/{patient_id}/reservations/
- Metode: POST
- Body: Data JSON untuk membuat reservasi baru untuk pasien tertentu (ID pasien, ID slot konsultasi).
- Response:
{
    "id": 1,
    "consultation_slot_id": 1,
    "patient_id": 1,
    "queue_number": 1
}
  
### GET - Lihat Consultation Slots:

- Endpoint: http://127.0.0.1:8000/consultation_slots/
- Metode: GET
- Response: Daftar slot konsultasi yang tersedia.

### GET - Lihat Patients:
- Endpoint: http://127.0.0.1:8000/patients/
- Metode: GET
- Response: Daftar pasien yang terdaftar.
  
### GET - Llihat Reservations for Patient:
- Endpoint: http://127.0.0.1:8000/patients/{patient_id}/reservations/
- Metode: GET
- Response: Daftar reservasi yang dibuat oleh pasien tertentu.
  
### PUT - Edit Reservation:
- Endpoint: http://127.0.0.1:8000/reservations/{reservation_id}
- Metode: PUT
- Body: Data JSON untuk memperbarui reservasi (ID pasien, ID slot konsultasi).
- Response:
  {
    "id": 1,
    "consultation_slot_id": 2,
    "patient_id": 1,
    "queue_number": 1
}
  
### DELETE - Hapus Reservation:
- Endpoint: http://127.0.0.1:8000/reservations/{reservation_id}
- Metode: DELETE
- Response:
  {
    "message": "Reservation deleted successfully"
}
