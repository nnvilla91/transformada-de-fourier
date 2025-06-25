# Fourtier simulación

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Configuración base
Fs = 1000  # Frecuencia de muestreo (Hz)
T = 1 / Fs
t = np.arange(0, 1, T)  # Tiempo de 0 a 1 segundo

# 1. Pulso rectangular
rect = np.zeros(len(t))
rect[100:400] = 1  # Pulso de 0.1s a 0.4s

# 2. Escalón unitario
step = np.ones(len(t))
step[:250] = 0  # Escalón en el medio

# 3. Señal senoidal
f = 50  # Frecuencia de la señal (Hz)
sine = np.sin(2 * np.pi * f * t)

# ---- Función para graficar señal y su transformada de Fourier ----
def graficar_fft(signal, titulo):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, T)[:N//2]  # Frecuencias positivas
    plt.figure(figsize=(12, 4))

    # Dominio del tiempo
    plt.subplot(1, 2, 1)
    plt.plot(t, signal)
    plt.title(f'{titulo} - Tiempo')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')

    # Dominio de la frecuencia
    plt.subplot(1, 2, 2)
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.title(f'{titulo} - Frecuencia')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.tight_layout()
    plt.show()

# Llamadas a función para cada señal
graficar_fft(rect, "Pulso rectangular")
graficar_fft(step, "Escalón unitario")
graficar_fft(sine, "Señal senoidal")


