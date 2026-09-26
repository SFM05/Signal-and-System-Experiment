r'''
已知下列传递函数，请分别画出其直角坐标系下的幅频曲线和相频曲线
(1) \( H(s) = \frac{2s}{s^2 + \sqrt{2}s + 1} \)
(2) 不调用函数，\( H(z) = \frac{(1 + z^{-1})^2}{1 + 0.61z^{-2}} \)
'''
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def transferFunction(z): return (1 - z**(-1))**2 / (1 + 0.61 * z**(-2))


b = [2]
a = [1, np.sqrt(2), 1]
f = np.logspace(-3, 3, 100)
_, H = signal.freqs(b, a,worN=f * 2*np.pi)

ax: list[Axes]
fig, ax = plt.subplots(2, 1)
ax[0].loglog(f, np.abs(H))
ax[0].set_title("Amplitude vs Frequency")
ax[0].set_xlabel(r"f/Hz")
ax[0].set_ylabel("Amplitude")

ax[1].semilogx(f, np.angle(H))
ax[1].set_title("Phase vs Frequency")
ax[0].set_xlabel(r"f/Hz")
ax[1].set_ylabel("Phase/rad")

plt.show(block=False)
plt.pause(1e-2)


omega = np.linspace(-np.pi, np.pi, 500)
H = transferFunction(np.exp(1j*omega))

ax: list[Axes]
fig, ax = plt.subplots(2, 1)
ax[0].plot(omega, np.abs(H))
ax[0].set_title("Amplitude vs Frequency")
ax[0].set_xlabel(r"Normalized frequency/ $\times f_s/2\pi$")
ax[0].set_ylabel("Amplitude")

ax[1].plot(omega, np.angle(H))
ax[1].set_title("Phase vs Frequency")
ax[1].set_xlabel(r"Normalized frequency/ $\times f_s/2\pi$")
ax[1].set_ylabel("Phase/rad")

plt.show()
