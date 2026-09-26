r'''
系统传递函数形式为\( H(p) = \frac{p+3}{p^2+2p+1} \)，激励为\( e(t) = e^{-2t}H(t) \)。要求先用现有函数求零状态响应，再用卷积积分运算求零状态响应。 
'''
from scipy import signal
import sympy
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def conv_sym(f, g, t: sympy.Symbol):
    tau = sympy.symbols("tau", real=True)
    f_tau = f.subs(t, tau)
    g_tau_shifted = g.subs(t, t-tau)
    return sympy.integrate(f_tau*g_tau_shifted, (tau, 0, t))


b = [1, 3]
a = [1, 2, 1]
sys = signal.TransferFunction(b, a)
dt = 1e-2
t = np.arange(0, 10, dt)
e = np.exp(-2*t)
_, response, _ = signal.lsim(sys, e, t)

plt.plot(t, response, label="System method")

_, h = signal.impulse(sys, T=t)
# plt.plot(t, h, label="h")
response = np.convolve(e, h)*dt
plt.plot(t, response[:len(t)], label="Conv")

plt.legend()
plt.xlabel("t/s")
plt.ylabel("r")
plt.show()
