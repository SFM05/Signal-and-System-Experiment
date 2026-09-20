r'''
对于高斯序列
\[
x(k) = \begin{cases}
    e^{-\frac{(k - p)^2}{q}} \quad 0 \le k \le 15
    0 \quad \mathrm{otherwise}
\end{cases}
\]
（1）固定参数p=8，改变q分别等于 2,4,8，观察时域和频域特性，了解q对时域幅度特性的影响。 
（2）固定q=8，改变 p，使p分别等于 8,13,14，观察p对信号序列的时域及频域特性的影响。注意p等于多少时会发生明显的泄漏现象，混叠是否也随之出现？
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def f(k: np.ndarray, p, q) -> np.ndarray:
    result = np.zeros_like(k, dtype=np.float64)
    idx = (k >= 0) & (k <= 15)
    result[idx] = np.exp(- (k[idx]-p)**2/q)
    return result


k = np.arange(-100, 100)
x1 = f(k, p=8, q=2)
x2 = f(k, p=8, q=4)
x3 = f(k, p=8, q=8)

spec1 = np.fft.fftshift(np.fft.fft(x1))
spec2 = np.fft.fftshift(np.fft.fft(x2))
spec3 = np.fft.fftshift(np.fft.fft(x3))
freq = np.fft.fftshift(np.fft.fftfreq(len(k)) * 2*np.pi)

ax: list[Axes]
fig, ax = plt.subplots(3, 1)
ax[0].stem(k, x1, "C0-", label="p=2", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].stem(k, x2, "C1-", label="p=4", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].stem(k, x3, "C2-", label="p=8", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].axhline(0, color='k', linewidth=0.6)
ax[0].set_xlim([0, 15])
ax[0].legend()

ax[1].plot(freq, np.abs(spec1), label="p=2")
ax[1].plot(freq, np.abs(spec2), label="p=4")
ax[1].plot(freq, np.abs(spec3), label="p=8")
ax[1].legend()

ax[2].plot(freq, (np.angle(spec1)), label="p=2")
ax[2].plot(freq, (np.angle(spec2)), label="p=4")
ax[2].plot(freq, (np.angle(spec3)), label="p=8")
ax[2].legend()

plt.show(block=False)
plt.pause(1e-2)


x1 = f(k, p=8, q=8)
x2 = f(k, p=13, q=8)
x3 = f(k, p=14, q=8)
spec1 = np.fft.fftshift(np.fft.fft(x1))
spec2 = np.fft.fftshift(np.fft.fft(x2))
spec3 = np.fft.fftshift(np.fft.fft(x3))
freq = np.fft.fftshift(np.fft.fftfreq(len(k)) * 2*np.pi)

fig, ax = plt.subplots(3, 1)
ax[0].stem(k, x1, "C0-", label="q=8", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].stem(k, x2, "C1-", label="q=13", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].stem(k, x3, "C2-", label="q=14", basefmt=' ').markerline.set_markerfacecolor("w")
ax[0].axhline(0, color='k', linewidth=0.6)
ax[0].set_xlim([0, 15])
ax[0].legend()

ax[1].plot(freq, np.abs(spec1), label="q=8")
ax[1].plot(freq, np.abs(spec2), label="q=13")
ax[1].plot(freq, np.abs(spec3), label="q=14")
ax[1].legend()

ax[2].plot(freq, (np.angle(spec1)), label="q=8")
ax[2].plot(freq, (np.angle(spec2)), label="q=13")
ax[2].plot(freq, (np.angle(spec3)), label="q=14")
ax[2].legend()

plt.show()
