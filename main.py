from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import joblib
import pandas as pd

app = FastAPI(title="API Deteksi Risiko ISPA")

# Muat komponen
try:
    preprocessor = joblib.load('models/preprocessor_ispa.pkl')
    model_ansambel = joblib.load('models/ensemble_model_ispa.pkl')
    le_JenisKelamin = joblib.load('models/le_jk.pkl')
    le_target = joblib.load('models/le_target.pkl')
except Exception as e:
    print(f"Gagal memuat model: {e}")

# Schema Input
class DataPasien(BaseModel):
    JenisKelamin: Literal["Laki-laki", "Perempuan"]
    Umur: int
    BatukKering: int
    BatukBerdahak: int
    Demam: int
    Pilek: int
    HidungTersumbat: int
    SesakNapas: int
    NyeriTenggorokan: int
    SakitKepala: int
    MualMuntah: int
    NyeriDada: int
    SuaraSerak: int
    NafsuMakanMenurun: int
    HilangPenciuman: int
    NyeriSaatMenelan: int

@app.post("/predict")
def prediksi_ispa(pasien: DataPasien):
    try:
        # 1. Konversi input ke dictionary
        input_data = pasien.model_dump()
        
        # 2. Mapping nilai JenisKelamin dari format manusia ke format model ('L' atau 'P')
        mapping_jk = {"Laki-laki": "L", "Perempuan": "P"}
        input_data['JenisKelamin'] = mapping_jk[input_data['JenisKelamin']]
        
        # 3. Buat DataFrame
        df_input = pd.DataFrame([input_data])
        
        # 4. Renaming: Sesuaikan nama kolom agar sama persis dengan yang diharapkan model
        # Sesuaikan 'key' dengan nama di class Pydantic, 'value' dengan nama di dataset training Anda
        mapping_kolom = {
            'JenisKelamin': 'Jenis Kelamin',
            'BatukKering': 'Batuk Kering',
            'BatukBerdahak': 'Batuk Berdahak',
            'HidungTersumbat': 'Hidung Tersumbat',
            'SesakNapas': 'Sesak Napas',
            'NyeriTenggorokan': 'Nyeri Tenggorokan',
            'SakitKepala': 'Sakit Kepala',
            'MualMuntah': 'Mual Muntah',
            'NyeriDada': 'Nyeri Dada',
            'SuaraSerak': 'Suara Serak',
            'NafsuMakanMenurun': 'Nafsu Makan Menurun',
            'HilangPenciuman': 'Hilang Penciuman',
            'NyeriSaatMenelan': 'Nyeri Saat Menelan'
        }
        df_input.rename(columns=mapping_kolom, inplace=True)
        
        # 5. Transformasi LabelEncoder menggunakan nama kolom yang sudah di-rename
        df_input['Jenis Kelamin'] = le_JenisKelamin.transform(df_input['Jenis Kelamin'])
        
        # 6. Preprocessing (Scaling/Encoding fitur lainnya)
        fitur_siap = preprocessor.transform(df_input)
        
        # 7. Prediksi
        prediksi_angka = model_ansambel.predict(fitur_siap)[0]
        probabilitas = model_ansambel.predict_proba(fitur_siap)[0]
        
        # 8. Hasil
        hasil_label = le_target.inverse_transform([prediksi_angka])[0]
        
        return {
            "Prediksi_Risiko": hasil_label,
            "Probabilitas_Tinggi": float(probabilitas[1]),
            "Probabilitas_Rendah": float(probabilitas[0])
        }
        
    except Exception as e:
        # Menampilkan detail error di response agar mudah di-debug
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)