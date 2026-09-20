r'''
已知z域函数
\[
F(z) = \frac{z^2-z}{(z-1)^3}
\]
求其反变换。
'''
import lcapy as lc
from lcapy.discretetime import z

F = (z**2-z) / (z-1)**3
f = F.IZT()
print(f)