r'''
描述下列系统，并求出极零点。
(1) \( r' + r = e \)
(2) \( r' = 10e' + 10e \)
(3) \( r'' - 5r' = 10e \)
'''
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})

ax: list[Axes]
fig, ax = plt.subplots(1, 3, figsize=(12, 4))

b = [1]
a = [1, 1]
z, p, k = signal.tf2zpk(b, a)
ax[0].plot(z.real, z.imag, 'o', label='zeros')
ax[0].plot(p.real, p.imag, 'x', label='poles')

b = [10, 10]
a = [1]
z, p, k = signal.tf2zpk(b, a)
ax[1].plot(z.real, z.imag, 'o', label='zeros')
ax[1].plot(p.real, p.imag, 'x', label='poles')

b = [10]
a = [1, -5]
z, p, k = signal.tf2zpk(b, a)
ax[2].plot(z.real, z.imag, 'o', label='zeros')
ax[2].plot(p.real, p.imag, 'x', label='poles')

for axs in ax:
    axs.axhline(0, color='k', lw=0.5)
    axs.axvline(0, color='k', lw=0.5)
    axs.legend()
    axs.set_xlabel("Re")
    axs.set_ylabel("Im")
    axs.axis('square')
    axs.set_xlim([-6, 6])
    axs.set_ylim([-6, 6])

plt.show()
