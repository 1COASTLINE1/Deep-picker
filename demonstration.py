import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk
import tensorflow as tf

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
    ax.plot(x, y, label='Original', color='blue')
    ax.set_title('Gaussian Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # 使用模型进行预测
    y_input = y.reshape(1, 100, 1)  # 调整输入形状
    y_pred_classification, y_pred_regression = model.predict(y_input)
    print(y_pred_regression)
    
    # 生成预测的高斯曲线
    y_pred = np.zeros_like(x)
    for A, cen in zip(y_pred_regression[0], centers):
        y_pred += gaussian(x, A, cen, sigma)
    
    ax.plot(x, y_pred, label='Predicted', color='red')
    ax.legend()
    canvas.draw()
    
    # 更新预测值显示框
    for i in range(5):
        pred_entries[i].config(state='normal')
        pred_entries[i].delete(0, tk.END)
        pred_entries[i].insert(0, f"{y_pred_regression[0][i]:.2f}")
        pred_entries[i].config(state='readonly')
    
    # 绘制绝对残差图
    residuals = np.abs(np.array(areas) - y_pred_regression[0])
    ax_residuals.clear()
    bars = ax_residuals.bar(centers, residuals, color='green')
    ax_residuals.set_title('Absolute Residuals')
    ax_residuals.set_xlabel('Centers')
    ax_residuals.set_ylabel('Absolute Residuals')
    ax_residuals.set_xticks(centers)
    
    # 添加标签
    for bar, residual in zip(bars, residuals):
        height = bar.get_height()
        ax_residuals.text(bar.get_x() + bar.get_width() / 2, height, f'{residual:.2f}', ha='center', va='bottom')
    
    canvas_residuals.draw()

# 创建主窗口
root = tk.Tk()
root.title("Gaussian Plotter")

# 设置窗口关闭事件
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# 创建一个Canvas和Scrollbar
main_canvas = tk.Canvas(root)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))

# 创建一个Frame放置在Canvas中
main_frame = ttk.Frame(main_canvas)
main_canvas.create_window((0, 0), window=main_frame, anchor='nw')

# 上方图形区域
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 添加导航工具栏
toolbar_frame = ttk.Frame(main_frame)
toolbar_frame.pack(side=tk.TOP, fill=tk.X)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()

# 中间输入框区域
frame = ttk.Frame(main_frame)
frame.pack(side=tk.TOP, fill=tk.X)

# 提示标签
label = ttk.Label(frame, text="Please enter values between 0 and 600", font=("Helvetica", 22))
label.grid(row=0, columnspan=10, pady=20)

# 画图按钮
button = tk.Button(frame, text="Plot", command=plot_gaussians, width=15, font=("Helvetica", 18))
button.grid(row=1, columnspan=10, padx=15, pady=10)

# 中心位置和初始 sigma
centers = [20, 30, 40, 60, 70]
sigma = 8
noise_level = 1/300 

# 创建输入框和预测值显示框
area_entries = []
pred_entries = []
for i in range(5):
    label = ttk.Label(frame, text=f"Area {i+1}:", font=("Helvetica", 18))
    label.grid(row=3, column=i*2, padx=(10, 5), pady=10, sticky=tk.E)
    entry = ttk.Entry(frame, font=("Helvetica", 18))  # 调整宽度
    entry.grid(row=3, column=i*2+1, padx=(5, 10), pady=10, sticky=tk.W+tk.E)  # 调整间距
    area_entries.append(entry)
    
    pred_label = ttk.Label(frame, text=f"Pred {i+1}:", font=("Helvetica", 18))
    pred_label.grid(row=4, column=i*2, padx=(10, 5), pady=10, sticky=tk.E)
    pred_entry = ttk.Entry(frame, font=("Helvetica", 18), state='readonly')  # 调整宽度
    pred_entry.grid(row=4, column=i*2+1, padx=(5, 10), pady=10, sticky=tk.W+tk.E)  # 调整间距
    pred_entries.append(pred_entry)

# 设置行和列的权重，使其在窗口调整大小时能够调整大小
for i in range(10):
    frame.columnconfigure(i, weight=1)
frame.columnconfigure(10, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)

# 创建下方残差图的区域
fig_residuals, ax_residuals = plt.subplots()
canvas_residuals = FigureCanvasTkAgg(fig_residuals, master=main_frame)
canvas_residuals.draw()
canvas_residuals.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 加载模型
model = tf.keras.models.load_model('my_model.h5')

# 运行主循环
root.mainloop()