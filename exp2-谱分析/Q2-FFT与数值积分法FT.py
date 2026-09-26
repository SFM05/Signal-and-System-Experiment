r'''
要求分别用数值积分和FFT计算
\[ f(t) = \cos(\frac{\pi t}{2}) (H(t+1) - H(t-1)) \]
的频谱，并画出其幅度频谱和相位频谱。 
'''
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def f(t):
    return np.cos(np.pi*t/2) * (np.heaviside(t+1, 0.5)-np.heaviside(t-1, 0.5))


def FT_int(f, omega):
    result, _ = scipy.integrate.quad(lambda t: f(t) * np.exp(-1j * omega * t),
                                     -np.inf, np.inf, complex_func=True)
    return result


freq_ft = np.linspace(-10, 10, 1000)
omega = freq_ft * 2*np.pi
ft_result = np.empty_like(freq_ft, dtype=np.complex64)

for i in range(len(omega)):
    ft_result[i] = FT_int(f, omega[i])

dt = 1e-3
t = np.arange(-2, 2, dt)
y = f(t)
fft_result = np.fft.fft(y) * dt
freq_fft = np.fft.fftfreq(len(t), dt)
fft_result = np.fft.fftshift(fft_result)
freq_fft = np.fft.fftshift(freq_fft)

fft_result *= np.exp(1j * (2*np.pi * freq_fft) * (-10))

ax: list[Axes]
_, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(freq_ft, np.abs(ft_result), label='Integral method')
stemcontainer = ax[0].stem(freq_fft, np.abs(fft_result), label='FFT method',
                           linefmt='g', basefmt=' ')
stemcontainer.markerline.set_markerfacecolor('w')

ax[1].plot(freq_ft, np.angle(ft_result), label='Integral method')
stemcontainer = ax[1].stem(freq_fft, np.angle(fft_result), label='FFT method',
                           linefmt='g', basefmt=' ')
stemcontainer.markerline.set_markerfacecolor('w')

for axs in ax:
    axs.legend()
    axs.set_xlim([-10, 10])
plt.show()
