r'''
卷积积分有一种简单的数值积分算法，将卷积积分近似为卷积和，从而可以近似计算其结果。一般可以采用等步长取样间隔，近似公式为
\[
f_1 * f_2 = \int_{-\infty}^{+\infty} f_1(\tau)f_2(t - \tau) dt
          = \lim_{t \to 0} \Delta t \sum f_1(k\Delta t) f_2(t - k\Delta t)
\]
按照上面的公式，分别使用数值积分方法和离散近似方法，求两个函数的积分。并作用于下面几个函数：
(1) \( f_1 = H(-t+1) + 2H(t-1) \, f_2 = e^{-t-1} H(t+1) \)
(2) \( f_2 = \sin t H(t) \, f_2 = H(t+1) \)
(3) \( 2H(t) - H(t-1) \, f_2 = \sin(\pi t) (H(t) - H(t-1)) \)
'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from scipy.integrate import quad_vec

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def conv_approx(f1, f2, step, t: np.ndarray[int],
                bound=[-100, 100]) -> np.ndarray[int]:
    tau = np.arange(bound[0], bound[1], step)
    x1 = f1(tau).reshape((1, -1))
    x2 = np.zeros((len(tau), len(t)))
    for i in range(0, len(tau)):
        x2[i, :] = f2(t-tau[i])

    result: np.ndarray[tuple[int, int]]
    result = step * x1@x2
    return result.flatten()


def conv_int(f1, f2, t,
             bound1=[-np.inf, np.inf], bound2=[-np.inf, np.inf]):
    def f(tau): return f1(tau)*f2(t-tau)
    left = np.maximum(bound1[0], np.min(t-bound2[1]))
    right = np.minimum(bound1[1], np.max(t-bound2[0]))
    result = quad_vec(f, left, right)
    return result[0]


def f1(t): return np.heaviside(-t+1, 1) + 2*np.heaviside(t-1, 1)  # [-inf, inf]


def f2(t):  # [-1, inf]
    t = np.array(t)
    result = np.zeros_like(t)
    idx = t > -1
    result[idx] = np.exp(-t[idx]-1)
    return result


def f3(t): return np.sin(t)*np.heaviside(t, 1)  # [0, inf]
def f4(t): return np.heaviside(t+1, 1)  # [-1, inf]
def f5(t): return 2*np.heaviside(t, 1) - np.heaviside(t-1, 1)  # [0, inf]


def f6(t): return np.sin(np.pi*t) * \
    (np.heaviside(t, 1)-np.heaviside(t-1, 1))  # [0, 1]


def y1(t): return 1+(1-np.exp(-t))*np.heaviside(t, 1)
def y2(t): return (1 - np.cos(t + 1)) * np.heaviside(t + 1, 1)


def y3(t):
    result = np.zeros_like(t)
    idx = (t > 0) & (t < 1)
    result[idx] = 2/np.pi * (1-np.cos(np.pi*t[idx]))
    idx = (t >= 1) & (t < 2)
    result[idx] = 1/np.pi * (3-np.cos(np.pi*t[idx]))
    idx = t >= 2
    result[idx] = 2/np.pi
    return result


ax: list[Axes]
_, ax = plt.subplots(3, 1, figsize=(8, 8))

t = np.linspace(-1, 5, 150)

y_approx1 = conv_approx(f1, f2, 0.1, t)
y_approx2 = conv_approx(f1, f2, 0.01, t)
y_int = conv_int(f1, f2, t, [-np.inf, np.inf], [-1, np.inf])
y_theory = y1(t)


ax[0].plot(t, y_approx1, label="step=0.1")
ax[0].plot(t, y_approx2, label="step=0.01")
ax[0].plot(t, y_int, label="integrate")
ax[0].plot(t, y_theory, label="theory")
ax[0].legend()
ax[0].set_xlabel("t")
ax[0].set_ylabel("y")
ax[0].set_title("$f_1*f_2$")

y_approx1 = conv_approx(f3, f4, 0.1, t)
y_approx2 = conv_approx(f3, f4, 0.01, t)
y_int = conv_int(f3, f4, t, [0, np.inf], [-1, np.inf])
y_theory = y2(t)

ax[1].plot(t, y_approx1, label="step=0.1")
ax[1].plot(t, y_approx2, label="step=0.01")
ax[1].plot(t, y_int, label="integrate")
ax[1].plot(t, y_theory, label="theory")
ax[1].legend()
ax[1].set_xlabel("t")
ax[1].set_ylabel("y")
ax[1].set_title("$f_3*f_4$")

y_approx1 = conv_approx(f5, f6, 0.1, t)
y_approx2 = conv_approx(f5, f6, 0.01, t)
y_int = conv_int(f5, f6, t, [0, np.inf], [0, 1])
y_theory = y3(t)

ax[2].plot(t, y_approx1, label="step=0.1")
ax[2].plot(t, y_approx2, label="step=0.01")
ax[2].plot(t, y_int, label="integrate")
ax[2].plot(t, y_theory, label="theory")
ax[2].legend()
ax[2].set_xlabel("t")
ax[2].set_ylabel("y")
ax[2].set_title("$f_5*f_6$")

plt.show()
