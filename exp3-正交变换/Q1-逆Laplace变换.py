r'''
一个连续系统的系统函数是
\[
H(s) = \frac{1}{(s+0.1)(s_0.2)}
\]
利用拉普拉斯变换求解信号\( f(t) = e^{-0.2t} \)通过这个系统的零状态响应。
'''
import sympy
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})

s, t = sympy.symbols("s t")
H = 1/((s+0.1)*(s+0.2))

e = sympy.exp(-0.2*t)
E, _, _ = sympy.laplace_transform(e, t, s)

R_zs = E * H
r_zs = sympy.inverse_laplace_transform(R_zs, s, t)
r_zs = sympy.simplify(r_zs)

sympy.plot(r_zs, (t, -5, 100),
           xlabel="t", ylabel="y")
