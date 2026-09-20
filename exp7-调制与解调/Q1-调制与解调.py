import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


sep = 1e-4
fs = 1/sep
t = np.arange(-0.5, 0.5, sep)
N = len(t)
f_mod = 200
f_n = 100

# Raw Signal
raw = np.exp(-0.2*t)*np.sinc(100*t/np.pi)
spec_raw = np.fft.fft(raw)/N
omega = np.fft.fftfreq(N, sep)
spec_raw = np.fft.fftshift(spec_raw)
omega = np.fft.fftshift(omega)

ax: list[list[Axes]]
fig, ax = plt.subplots(2, 2)
ax[0][0].plot(omega, np.abs(spec_raw))
ax[0][0].set_xlim([-2000, 2000])

# Modulation Signal
mod = (signal.square(2*np.pi*f_mod*t, 0.5) + 1) / 2
spec_mod = np.fft.fft(mod)/N
spec_mod = np.fft.fftshift(spec_mod)
ax[0][1].plot(omega, np.abs(spec_mod))
ax[0][1].set_xlim([-2000, 2000])

# Modulated Signal
modulated = raw*mod
spec_modulated = np.fft.fft(modulated)/N
spec_modulated = np.fft.fftshift(spec_modulated)
ax[1][0].plot(omega, np.abs(spec_modulated))
ax[1][0].set_xlim([-2000, 2000])

# Demodulated Signal
b, a = signal.butter(6, f_n / (fs/2), "low")
demodulated = signal.lfilter(b, a, modulated)
spec_demodulated = np.fft.fft(demodulated)/N
spec_demodulated = np.fft.fftshift(spec_demodulated)
ax[1][1].plot(omega, np.abs(spec_demodulated))
ax[1][1].set_xlim([-2000, 2000])

plt.show(block=False)
plt.pause(1e-2)

plt.figure()
plt.plot(t, raw, label="Raw signal")
plt.plot(t, demodulated, label="Demodulated signal")
plt.legend()
plt.show()
