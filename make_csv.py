import os
import pandas as pd

# Buat folder data jika belum ada
os.makedirs("data", exist_ok=True)

# === File 1: data1.csv (ada target) ===
df1 = pd.DataFrame({
    "umur": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "pendapatan": [3.5, 4.2, 5.1, 6.3, 7.8, 8.5, 9.1, 10.2, 11.3, 12.5],
    "target": ["A", "B", "A", "B", "A", "B", "A", "B", "A", "B"]
})
df1.to_csv("data/data1.csv", index=False)

# === File 2: data2.csv (numerik tanpa target) ===
df2 = pd.DataFrame({
    "tinggi": [150, 160, 170, 180, 190, 200, 175, 165, 185, 155],
    "berat": [50, 55, 65, 75, 85, 95, 70, 60, 80, 52],
    "usia": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
})
df2.to_csv("data/data2.csv", index=False)

# === File 3: data3.csv (kategori semua, tanpa target) ===
df3 = pd.DataFrame({
    "warna": ["merah", "biru", "hijau", "merah", "biru", "hijau", "kuning", "hitam", "putih", "coklat"],
    "buah": ["apel", "jeruk", "apel", "anggur", "jeruk", "apel", "pisang", "melon", "apel", "anggur"]
})
df3.to_csv("data/data3.csv", index=False)

"✅ 3 file CSV berhasil dibuat di folder data/"
