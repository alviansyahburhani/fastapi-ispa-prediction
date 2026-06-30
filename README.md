API Deteksi Risiko ISPA
Ini adalah API berbasis FastAPI yang digunakan untuk mendeteksi risiko ISPA (Infeksi Saluran Pernapasan Akut) menggunakan model Ensemble Learning.

Fitur Utama
Endpoint Prediksi: Menerima data klinis pasien dan mengembalikan prediksi risiko beserta probabilitasnya.

Validasi Input: Menggunakan Pydantic dengan Literal untuk memastikan input data sesuai dengan format yang diharapkan model.

Preprocessing Otomatis: Menangani pemetaan label gender dan penyesuaian nama kolom secara otomatis sebelum prediksi.

Persyaratan
Python 3.10+

Library utama: fastapi, uvicorn, pandas, scikit-learn, xgboost, joblib.

Cara Menjalankan
Clone repository ini:

Bash
git clone https://github.com/username/fastapi-ispa-prediction.git
cd fastapi-ispa-prediction
Buat Virtual Environment & Install Dependencies:

Bash
python -m venv venv
# Aktifkan venv (Windows)
.\venv\Scripts\activate
# Install library
pip install -r requirements.txt
Jalankan API:

Bash
python -m uvicorn main:app --reload
Akses Dokumentasi:
Buka browser dan akses http://127.0.0.1:8000/docs untuk melihat dokumentasi API (Swagger UI).

Contoh Request
Anda dapat menggunakan curl untuk melakukan prediksi:

Bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "JenisKelamin": "Laki-laki",
  "Umur": 25,
  "BatukKering": 1,
  "BatukBerdahak": 0,
  "Demam": 1,
  "Pilek": 0,
  "HidungTersumbat": 0,
  "SesakNapas": 0,
  "NyeriTenggorokan": 1,
  "SakitKepala": 0,
  "MualMuntah": 0,
  "NyeriDada": 0,
  "SuaraSerak": 0,
  "NafsuMakanMenurun": 0,
  "HilangPenciuman": 0,
  "NyeriSaatMenelan": 1
}'
Saran Tambahan agar Proyek Anda "Bersih":
Buat file requirements.txt:
Di terminal (dengan venv aktif), jalankan:

Bash
pip freeze > requirements.txt
Ini akan mencatat semua library yang Anda gunakan. File ini wajib di-push ke GitHub agar orang lain bisa menginstal library yang sama dengan Anda.

Struktur Folder yang Disarankan:
Agar rapi, pastikan susunannya seperti ini:

Plaintext
fastapi-ispa-prediction/
├── models/
│   ├── ensemble_model_ispa.pkl
│   ├── le_jk.pkl
│   ├── le_target.pkl
│   └── preprocessor_ispa.pkl
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
