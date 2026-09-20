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
t = np.linspace(0, 10, 1000)
e = np.exp(-2*t)
t, respond, _ = signal.lsim(sys, e, t)

plt.plot(t, respond)
plt.show(block=False)
plt.pause(2e-2)

s = sympy.symbols("s")
t, tau = sympy.symbols("t tau", real=True)
H = (s+3)/(s**2+2*s+1)
h = sympy.inverse_laplace_transform(H, s, t)
e = sympy.exp(-2*t)*sympy.Heaviside(t)

r = sympy.integrate(h.subs(t, tau) * e.subs(t, t-tau), (tau, 0, t))
r = sympy.simplify(r)
sympy.plot(r, (t, 0, 10))
