import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})

ax: list[list[Axes]]
fig, ax = plt.subplots(2, 2)

t_sym = sp.symbols("t", real=True)
freq_sym = sp.symbols("f", real=True)
# Here $\sinc x = \frac{\sin x}{x}$ in `sympy`
# Rather than $\sinc x = \frac{\sin\pi x}{\pi x}$ in `numpy`
f_sym = sp.sinc(10*sp.pi * t_sym)

spec_sym = sp.fourier_transform(f_sym, t_sym, freq_sym)
spec_sym = sp.simplify(spec_sym)
print(spec_sym)

F = sp.lambdify(freq_sym, spec_sym, "numpy")
freq = np.linspace(-10, 10, 1000)
ax[0][0].plot(freq, np.abs(F(freq)))
ax[0][0].set_ylim([-0.1, 0.6])
ax[0][0].set_xlim([-10, 10])


Ts = 0.5
fs = 1/Ts
t = np.arange(-100, 100, Ts)
N = len(t)
f = np.sinc(10*t)

spec1 = np.fft.fft(f)*Ts
freq = np.fft.fftfreq(N, Ts)
spec1 = np.fft.fftshift(spec1)
freq = np.fft.fftshift(freq)
ax[0][1].plot(freq, np.abs(spec1))
ax[0][1].set_ylim([-0.1, 0.6])
ax[0][1].set_xlim([-10, 10])


Ts = 0.2
fs = 1/Ts
t = np.arange(-100, 100, Ts)
N = len(t)
f = np.sinc(10*t)

spec2 = np.fft.fft(f)*Ts
freq = np.fft.fftfreq(N, Ts)
spec2 = np.fft.fftshift(spec2)
freq = np.fft.fftshift(freq)
ax[1][0].plot(freq, np.abs(spec2))
ax[1][0].set_ylim([-0.1, 0.6])
ax[1][0].set_xlim([-10, 10])


Ts = 0.01
fs = 1/Ts
t = np.arange(-100, 100, Ts)
N = len(t)
f = np.sinc(10*t)

spec3 = np.fft.fft(f)*Ts
freq = np.fft.fftfreq(N, Ts)
spec3 = np.fft.fftshift(spec3)
freq = np.fft.fftshift(freq)
ax[1][1].plot(freq, np.abs(spec3))
ax[1][1].set_ylim([-0.1, 0.6])
ax[1][1].set_xlim([-10, 10])


plt.show()
