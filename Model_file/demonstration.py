import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# 高斯函数
def gaussian(x, A, cen, sigma):
    ln2 = np.log(2)
    PI = np.pi
    amplitude = A  # 振幅乘以浓度
    return (amplitude * np.sqrt(4 * ln2) / (sigma * np.sqrt(PI))) * np.exp(-4 * ln2 * (x - cen)**2 / (sigma**2))

# 画图函数
def plot_gaussians():
    areas = [float(entry.get()) for entry in area_entries]
    x = np.linspace(0, 99, 100)
    y = np.zeros_like(x)
    
    for A, cen in zip(areas, centers):
        y += gaussian(x, A, cen, sigma)
    
    ax.clear()
    ax.plot(x, y)
    ax.set_title('Gaussian Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    canvas.draw()

# 创建主窗口
root = tk.Tk()
root.title("Gaussian Plotter")

# 上方图形区域
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 下方输入框区域
frame = ttk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X)

# 提示标签
label = ttk.Label(frame, text="请输入0-600的值")
label.pack(side=tk.TOP)

# 中心位置和初始 sigma
centers = [20, 30, 40, 60, 70]
sigma = 8
noise_level = 1/300 

# 创建输入框
area_entries = []
for i in range(5):
    label = ttk.Label(frame, text=f"Area {i+1}:")
    label.pack(side=tk.LEFT)
    entry = ttk.Entry(frame, width=10)
    entry.pack(side=tk.LEFT)
    area_entries.append(entry)

# 画图按钮
button = ttk.Button(frame, text="Plot", command=plot_gaussians)
button.pack(side=tk.LEFT)

# 运行主循环
root.mainloop()
