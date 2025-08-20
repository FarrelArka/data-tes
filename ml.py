import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error
import tkinter as tk
from tkinter import simpledialog, messagebox

# === 1. Cek semua CSV di folder data/ ===
data_folder = "data"
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

if not csv_files:
    raise FileNotFoundError("Tidak ada file CSV di folder 'data/'.")

# === 2. Pop-up pilihan file ===
root = tk.Tk()
root.withdraw()
file_choice = simpledialog.askstring(
    "Pilih Dataset",
    f"File CSV tersedia:\n" + "\n".join(csv_files) + "\n\nKetik nama file yang mau dipakai:"
)

if not file_choice.endswith(".csv"):
    file_choice += ".csv"

if file_choice not in csv_files:
    messagebox.showerror("Error", f"File '{file_choice}' tidak ditemukan!")
    exit()


file_path = os.path.join(data_folder, file_choice)

# === 3. Baca CSV ===
df = pd.read_csv(file_path)

# === 4. Deteksi target otomatis ===
target_keywords = ["target", "label", "kelas", "class", "sentiment", "y"]
target_col = None

for col in df.columns:
    if col.lower() in target_keywords:
        target_col = col
        break

if target_col is None:
    target_col = df.columns[-1]  # default: kolom terakhir

# === 5. Pisahkan fitur & target ===
X = df.drop(columns=[target_col])
y = df[target_col]

# Encode kategori
for col in X.select_dtypes(include=['object']).columns:
    X[col] = LabelEncoder().fit_transform(X[col])

is_classification = False
if y.dtype == 'object':
    y = LabelEncoder().fit_transform(y)
    is_classification = True
elif len(y.unique()) < 10:
    is_classification = True

# === 6. Train & Evaluasi ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

if is_classification:
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    result = f"Dataset: {file_choice}\nMode: Klasifikasi\nTarget: {target_col}\nAkurasi: {score:.2f}"
else:
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    result = f"Dataset: {file_choice}\nMode: Regresi\nTarget: {target_col}\nMSE: {mse:.2f}"

# === 7. Tampilkan hasil ===
messagebox.showinfo("Hasil Machine Learning", result)
