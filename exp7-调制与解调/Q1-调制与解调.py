r'''
将信号\(f(t) = e^{-0.2t} \mathrm{Sa}(100t) H(t) \)用脉冲幅度调制，并解调，显示出解调后的波形。建议在 [0,0.5]范围内观察信号的时域波形，步长0.0001，脉冲信号的频率为200Hz，滤波器的截止频率100Hz。观察输出波形和输入波形的区别，并试着用信号与系统的相关理论解释。 
要求：
1、分别绘制：原始基带信号频谱、脉冲载波信号频谱、PAM调制后信号频谱，对比三者频谱特征变化。
2、在同一张图内绘制原始信号、解调的信号，直观对比时域波形差异。
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.axes import Axes

import matplotlib
matplotlib.rcParams.update({"lines.linewidth": 1,
                            "figure.constrained_layout.use": True})


dt = 1e-4
fs = 1/dt
t = np.arange(-0.5, 0.5, dt)
N = len(t)
f_mod = 200
f_n = 100

ax: list[list[Axes]]
fig, ax = plt.subplots(2, 2, figsize=(10, 6))

# Raw Signal
raw = np.exp(-0.2*t)*np.sinc(100*t/np.pi)
spec_raw = np.fft.fft(raw)/N
omega = np.fft.fftfreq(N, dt)
spec_raw = np.fft.fftshift(spec_raw)
omega = np.fft.fftshift(omega)
ax[0][0].plot(omega, np.abs(spec_raw))
ax[0][0].set_title("Raw Signal")


# Modulation Signal
mod = (signal.square(2*np.pi*f_mod*t, 0.5) + 1) / 2
spec_mod = np.fft.fft(mod)/N
spec_mod = np.fft.fftshift(spec_mod)
ax[0][1].plot(omega, np.abs(spec_mod))
ax[0][1].set_title("Modulation Signal")

# Modulated Signal
modulated = raw*mod
spec_modulated = np.fft.fft(modulated)/N
spec_modulated = np.fft.fftshift(spec_modulated)
ax[1][0].plot(omega, np.abs(spec_modulated))
ax[1][0].set_title("Modulated Signal")

# Demodulated Signal
b, a = signal.butter(6, f_n / (fs/2), "low")
# demodulated = signal.lfilter(b, a, modulated) # 单一滤波
demodulated = signal.filtfilt(b, a, modulated) # 双向零相位滤波
spec_demodulated = np.fft.fft(demodulated)/N
spec_demodulated = np.fft.fftshift(spec_demodulated)
ax[1][1].plot(omega, np.abs(spec_demodulated))
ax[1][1].set_title("Demodulated Signal")

axs: Axes
for axs in ax.flatten():
    axs.set_xlabel("f/Hz")
    axs.set_ylabel("Amplitude")
    axs.set_xlim([-2000, 2000])

plt.show(block=False)
plt.pause(1e-2)

plt.figure()
plt.plot(t, raw, label="Raw signal")
plt.plot(t, demodulated, label="Demodulated signal")
plt.title("Signals")
plt.xlabel("t/s")
plt.ylabel("y")
plt.legend()
plt.show()
