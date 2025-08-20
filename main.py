import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset sederhana
data = {
    "x": np.arange(1, 11),
    "y": np.random.randint(10, 50, 10)
}

df = pd.DataFrame(data)
print(df)

# Plot grafik
plt.plot(df["x"], df["y"], marker="o")
plt.title("Contoh Grafik")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
