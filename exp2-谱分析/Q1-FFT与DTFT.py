r'''
已知离散时间序列 x(k) = {1,2,3,4,5,6,6,5,4,3,2,1} 
（1）通过DTFT的定义计算频谱（频率间隔 0.1）。 
（2）使用FFT计算频谱。 
（3）将上面两个结果展示在同一幅画面中，验证FFT就是DTFT的采样。
'''
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


def DTFT(x: np.ndarray, omega: np.ndarray) -> np.ndarray:
    k = np.arange(0, len(x)).reshape(1, -1)
    x = x.reshape(1, -1)
    omega = omega.reshape(-1, 1)
    result = x @ np.exp(-1j * omega @ k).T
    return result.flatten()


x = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])

omega_dtft = np.arange(-np.pi, np.pi, 0.01)
dtft_result = DTFT(x, omega_dtft)

fft_result = np.fft.fft(x)
omega_fft = np.fft.fftfreq(len(x)) * 2*np.pi
fft_result = np.fft.fftshift(fft_result)
omega_fft = np.fft.fftshift(omega_fft)


plt.plot(omega_dtft, abs(dtft_result))
stemcontainer = plt.stem(omega_fft, abs(fft_result),
                         linefmt="g", markerfmt="o", basefmt=' ')
stemcontainer.markerline.set_markerfacecolor('w')

plt.gca().axhline(0, color='k', lw=0.6)
plt.show()
