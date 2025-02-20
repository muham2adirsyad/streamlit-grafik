import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Menggunakan gaya OriginLab
plt.style.use("ggplot")

# Judul aplikasi
st.title("Grafik Profesional Setara OriginLab")

# Pilihan jenis grafik
chart_type = st.selectbox("Pilih jenis grafik", ["Sin", "Cos", "Tan", "Exponential", "Gaussian"])

# Input rentang X dari pengguna
x_min = st.number_input("Masukkan nilai minimum X", value=0.0, step=0.1)
x_max = st.number_input("Masukkan nilai maksimum X", value=10.0, step=0.1)
num_points = st.slider("Jumlah titik data", 50, 1000, 200)

# Generate data
x = np.linspace(x_min, x_max, num_points)

if chart_type == "Sin":
    y = np.sin(x)
    title = "Grafik Sinus"
elif chart_type == "Cos":
    y = np.cos(x)
    title = "Grafik Cosinus"
elif chart_type == "Tan":
    y = np.tan(x)
    y[np.abs(y) > 10] = np.nan  # Hindari nilai ekstrem
    title = "Grafik Tangen"
elif chart_type == "Exponential":
    y = np.exp(x / np.max(x))
    title = "Grafik Eksponensial"
elif chart_type == "Gaussian":
    mu, sigma = np.mean(x), np.std(x)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    title = "Grafik Gaussian (Distribusi Normal)"

# Plot grafik
fig, ax = plt.subplots(figsize=(8, 5), dpi=150)
ax.plot(x, y, label=title, color="blue", linewidth=2)
ax.set_xlabel("X-Axis", fontsize=12, fontweight="bold")
ax.set_ylabel("Y-Axis", fontsize=12, fontweight="bold")
ax.set_title(title, fontsize=14, fontweight="bold")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)

# Tampilkan di Streamlit
st.pyplot(fig)
