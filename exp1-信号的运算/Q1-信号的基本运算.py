r'''
已知信号\(f(t) = (t+1)[H(t+1)−H(t−1)]\)。请编写程序实现以下运算并画出波形：\(f(t−2)H(t−2)\) 
'''

import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def f(t): return (t + 1) * (np.heaviside(t+1, 1)-np.heaviside(t-1, 1))


t = np.linspace(0, 4, 2000)
y = f(t-2)*np.heaviside(t-2, 1)

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y")
plt.show()
