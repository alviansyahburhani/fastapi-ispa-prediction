# API Deteksi Risiko ISPA (Ensemble Learning)

API ini dibangun menggunakan **FastAPI** untuk memprediksi tingkat risiko infeksi saluran pernapasan akut (ISPA) menggunakan model **Ensemble Learning**. Proyek ini bertujuan untuk menyediakan inferensi yang cepat dan akurat berdasarkan data klinis pasien.

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

⚙️ Cara Menjalankan
Clone repository:

Bash
git clone [https://github.com/username/fastapi-ispa-prediction.git](https://github.com/username/fastapi-ispa-prediction.git)
cd fastapi-ispa-prediction
Setup Environment:

Bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Jalankan Server:

Bash
python -m uvicorn main:app --reload
Akses API:
Buka http://127.0.0.1:8000/docs di browser Anda untuk melihat dokumentasi interaktif.

📋 Contoh Request (cURL)

curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
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

⚠️ Catatan
Pastikan semua file model .pkl ditempatkan di dalam folder /models agar API dapat memuat model dengan benar.

Gunakan file .gitignore untuk mencegah folder venv dan model besar (jika menggunakan LFS) terunggah ke GitHub.


---

### Tips untuk Git:
Setelah Anda menyimpan file di atas, pastikan Anda telah membuat file `requirements.txt` dengan cara:
1. Pastikan `venv` aktif.
2. Jalankan: `pip freeze > requirements.txt`

Dengan adanya `README.md` dan `requirements.txt`, proyek Anda sudah siap untuk di-push ke GitHub dan orang lain akan sangat mudah menggunakannya. Apakah ada bagian lain yang ingin Anda tambahkan?
