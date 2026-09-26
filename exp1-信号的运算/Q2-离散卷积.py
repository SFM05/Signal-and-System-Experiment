r'''
编写一个计算两个离散序列的卷积和的程序，并用其计算下列卷积和。
f1(k) = {1,1,1,1}, f2(k) = {1,0.5,0.25,0.125,0.0625}
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def conv(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    lena = len(a)
    lenb = len(b)
    result = np.zeros(lena+lenb-1)

    for i in range(0, lena+lenb-1):
        # Requires: 0 <= j <= lena-1
        #           0 <= i-j <= lenb-1
        for j in range(max(0, i-lenb+1), min(lena, i+1)):
            result[i] += a[j]*b[i-j]

    return result


x1 = [1, 1, 1, 1]
x2 = [1, 0.5, 0.25, 0.125, 0.0625]

result = conv(x1, x2)
print(result)

ax: list[Axes]
_, ax = plt.subplots(3, 1, figsize=(8, 8))

container = ax[0].stem(x1, basefmt=" ")
container.markerline.set_markerfacecolor('w')
ax[0].set_title(r"$x_1$")

container = ax[1].stem(np.arange(-len(x2)+1, 1), list(reversed(x2)),
                       basefmt=" ")
container.markerline.set_markerfacecolor('w')
ax[1].set_title(r"$x_2$")

container = ax[2].stem(result, basefmt=" ")
container.markerline.set_markerfacecolor('w')
ax[2].set_title(r"$x_1 * x_2$")

for axs in ax:
    axs.axhline(0, color='k', lw=0.6)
    axs.set_xlabel("t")
    axs.set_ylabel("y")
    axs.set_xlim([-4.5, 7.5])

plt.show()
