import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np

# === 1. Scan folder data ===
folder = "data"
files = [f for f in os.listdir(folder) if f.endswith(".csv")]

if not files:
    print("⚠️ Tidak ada file CSV di folder 'data'")
    exit()

print("=== Daftar Dataset Tersedia ===")
for i, f in enumerate(files, 1):
    print(f"{i}. {f}")

# Pilih file
choice = int(input("Pilih dataset (angka): "))
file_path = os.path.join(folder, files[choice-1])

# === 2. Load dataset ===
df = pd.read_csv(file_path)
print(f"\n=== Dataset Dipilih: {files[choice-1]} ===")
print(df.head())

# === 3. Info & Statistik ===
print("\nInfo:")
print(df.info())
print("\nStatistik Deskriptif:")
print(df.describe(include="all"))


# === 4. Visualisasi Satu Grafik Saja ===
num_cols = df.select_dtypes(include=np.number).columns.tolist()

target_col = None
for col in df.columns:
    if "target" in col.lower() or "label" in col.lower():
        target_col = col
        break

plt.figure(figsize=(6,4))

if target_col:
    print(f"\n🎯 Terdeteksi target kolom: {target_col}")

    if df[target_col].dtype == "object" or df[target_col].nunique() <= 10:
        sns.countplot(x=target_col, data=df, palette="Set2")
        plt.title(f"Distribusi Target: {target_col}")
    else:
        sns.histplot(df[target_col], bins=20, kde=True, color="skyblue")
        plt.title(f"Distribusi Target: {target_col}")

else:
    print("\nℹ️ Tidak ada kolom target/label terdeteksi → menampilkan distribusi fitur numerik pertama.")
    if len(num_cols) > 0:
        sns.histplot(df[num_cols[0]], bins=20, kde=True, color="orange")
        plt.title(f"Distribusi {num_cols[0]}")

plt.show()
