r'''
已知信号\( \mathrm{Sa}(10πt) \)，通过不同时间间隔\(T_s\)取样，画出频谱，并分析取样率和信号频率关系。
要求： 
（1）以\(T_s = 0.5\)取样，画幅度频谱 
（2）以\(T_s = 0.2\)取样，画幅度频谱 
（3）以\(T_s = 0.01\)取样，画幅度频谱 
（4）总结结果，讨论取样率和信号频率关系 
'''
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})

ax: list[list[Axes]]
fig, ax = plt.subplots(2, 2, figsize=(10, 6))

t_sym = sp.symbols("t", real=True)
freq_sym = sp.symbols("f", real=True)
# Here $\sinc x = \frac{\sin x}{x}$ in `sympy`
# Rather than $\sinc x = \frac{\sin\pi x}{\pi x}$ in `numpy`
f_sym = sp.sinc(10*sp.pi * t_sym)

spec_sym = sp.fourier_transform(f_sym, t_sym, freq_sym)
spec_sym = sp.simplify(spec_sym)

F = sp.lambdify(freq_sym, spec_sym, "numpy")
freq = np.linspace(-10, 10, 1000)
ax[0][0].plot(freq, np.abs(F(freq)))
ax[0][0].set_title("Full Spectrum")


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
ax[0][1].set_title("Spectrum when $T_s=0.5$s")


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
ax[1][0].set_title("Spectrum when $T_s=0.2$s")


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
ax[1][1].set_title("Spectrum when $T_s=0.01$s")


axs: Axes
for axs in ax.flatten():
    axs.set_ylim([-0.1, 0.6])
    axs.set_xlim([-10, 10])
    axs.set_xlabel("f/Hz")
    axs.set_ylabel("Amplitude")

plt.show()
