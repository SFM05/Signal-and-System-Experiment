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
omega, H = signal.freqs(b, a)

ax: list[Axes]
fig, ax = plt.subplots(2, 1)
ax[0].plot(omega, np.abs(H))
ax[1].plot(omega, np.angle(H))
plt.show(block=False)
plt.pause(1e-2)


omega = np.linspace(-np.pi, np.pi, 500)
H = transferFunction(np.exp(1j*omega))

ax: list[Axes]
fig, ax = plt.subplots(2, 1)
ax[0].plot(omega, np.abs(H))
ax[1].plot(omega, np.angle(H))
plt.show()
