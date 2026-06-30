# API Deteksi Risiko ISPA (Ensemble Learning)

API ini dibangun menggunakan **FastAPI** untuk memprediksi tingkat risiko infeksi saluran pernapasan akut (ISPA) menggunakan model **Ensemble Learning**. Proyek ini merupakan implementasi dari skripsi penulis, bertujuan untuk menyediakan inferensi yang cepat dan akurat berdasarkan data klinis pasien.

## 🚀 Fitur

* **Prediksi Berbasis AI:** Menggunakan model ensemble untuk mengklasifikasikan risiko pasien.
* **Validasi Input Ketat:** Menggunakan `Pydantic` dengan `Literal` untuk memastikan data yang masuk sesuai standar medis.
* **Integrasi Preprocessing:** Otomatis menangani encoding data kategorikal dan penskalaan fitur sebelum prediksi.
* **Dokumentasi API:** Terintegrasi secara otomatis dengan Swagger UI untuk kemudahan pengujian.

## 🛠 Teknologi yang Digunakan

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Model:** XGBoost & Scikit-learn (Ensemble)
* **Data Handling:** Pandas, Joblib
* **Server:** Uvicorn

## 📂 Struktur Proyek

```text
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
```

## ⚙️ Cara Menjalankan

1. **Clone repository:**

```bash
git clone https://github.com/username/fastapi-ispa-prediction.git
cd fastapi-ispa-prediction
```

2. **Setup Environment:**

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Jalankan Server:**

```bash
python -m uvicorn main:app --reload
```

5. **Akses API:** Buka `http://127.0.0.1:8000/docs` di browser Anda untuk melihat dokumentasi interaktif.

## 📋 Contoh Request (cURL)

```bash
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
```

## ⚠️ Catatan

* Pastikan semua file model `.pkl` ditempatkan di dalam folder `/models` agar API dapat memuat model dengan benar.
* Gunakan file `.gitignore` untuk mencegah folder `venv` dan model besar (jika menggunakan LFS) terunggah ke GitHub.
* Sebelum push ke GitHub, jalankan `pip freeze > requirements.txt` (saat `venv` aktif) agar daftar dependensi selalu sinkron dengan environment Anda.

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik (skripsi) dan dapat digunakan/dimodifikasi sesuai kebutuhan.
