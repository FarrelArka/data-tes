---

````markdown
# 📊 Auto CSV Analyzer (Mahoraga Style)

Tool Python ini otomatis membaca semua file `.csv` dalam folder `data/`, lalu memberi opsi ke user untuk memilih dataset mana yang mau dianalisis.  
Analisis menyesuaikan **100% isi CSV** (adaptif), termasuk info data, statistik, dan visualisasi sederhana.

---

## 🚀 Instalasi

### 1. Install Python
Pastikan sudah install **Python 3.8+**  
Cek versi dengan:
```bash
python --version
````

atau

```bash
python3 --version
```

### 2. Clone / Download Project

```bash
git clone https://github.com/username/auto-csv-analyzer.git
cd auto-csv-analyzer
```

> Kalau tidak pakai git, cukup download ZIP lalu ekstrak.

### 3. Buat Virtual Environment (opsional tapi disarankan)

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Isi `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn
```

---

## 📂 Struktur Folder

```
auto-csv-analyzer/
│
├── data/                # simpan semua file CSV di sini
│   ├── data1.csv
│   ├── data2.csv
│   └── data3.csv
│
├── analyzer.py          # script utama
├── requirements.txt
└── README.md
```

---

## ▶️ Cara Menjalankan

1. Simpan file `.csv` ke folder `data/`
2. Jalankan script:

   ```bash
   python analyzer.py
   ```
3. Program akan otomatis menampilkan daftar file CSV:

   ```
   === Daftar Dataset ===
   [1] data1.csv
   [2] data2.csv
   [3] data3.csv
   Pilih dataset (nomor / nama file .csv): 
   ```
4. Pilih dataset → hasil analisis akan muncul:

   * 5 baris pertama data
   * Info dataset
   * Statistik deskriptif
   * Visualisasi grafik:

     * Scatterplot otomatis (jika ada >1 kolom numerik)
     * Distribusi target (jika ada kolom target/label)

---

## 📊 Contoh Output

**Terminal**

```
=== Data Asli ===
   usia  penghasilan  target
0    21        2000       0
1    35        5000       1
2    42        7000       1
...
```

**Visualisasi**

* Scatterplot antar kolom numerik
* Grafik distribusi target/label (jika ada)

---

## ⚡ Catatan

* Jika dataset **tidak punya kolom target/label**, sistem otomatis menampilkan distribusi kolom numerik pertama.
* Bisa handle **banyak file CSV** tanpa perlu edit kode.
* Support semua tipe data (numerik & kategorikal).

---

## 📌 Lisensi

Bebas dipakai, dimodifikasi, atau dikembangkan.

```

---

👉 cover by me
```
