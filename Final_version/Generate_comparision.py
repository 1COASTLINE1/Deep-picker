import numpy as np
import itertools

def gaussian(x, A, cen, sigma):
    ln2 = np.log(2)
    PI = np.pi
    amplitude = A  # 振幅乘以浓度
    return (amplitude * np.sqrt(4 * ln2) / (sigma * np.sqrt(PI))) * np.exp(-4 * ln2 * (x - cen)**2 / (sigma**2))



def generate_data(centers, areas,sigma,noise_level,x_size=100):
    X_data = []
    y_classification = []
    y_regression = []
    
    # 生成所有可能的area组合
    area_combinations = list(itertools.product(areas, repeat=len(centers)))

    for area_comb in area_combinations:
        # 创建一个长度为x_size的全零数组作为基础的Ydata
        y_base = np.zeros(x_size)
        # 记录area作为回归任务的参数
        y_reg = []
        
        # 创建一个长度为x_size的全零数组作为基础的Xdata
        x_base = np.zeros(x_size)

        # 对于每个center和对应的area
        for center, area in zip(centers, area_comb):
            # 如果area不为0，将center位置的Ydata值设为1
            if area != 0:
                if center - 1 < 0:
                    y_base[center] = 1
                else:
                    y_base[center-1] = 1
            y_reg.append(area)
            
            # 使用gaussian函数生成y值
            y_gaussian = gaussian(np.arange(x_size), area, center, sigma) 
            y_gaussian += np.random.normal(0, noise_level, x_size)
            # 将生成的y值加到x_base上
            x_base += y_gaussian

        # 将基础的Ydata添加到Ydata列表中
        y_classification.append(y_base.tolist())
        # 记录area作为回归任务的参数
        y_regression.append(y_reg)

        # X_data是一系列的索引值，从0到x_size-1
        X_data.append(x_base.tolist())

    return np.array(X_data), np.array(y_classification), np.array(y_regression)

centers = [20, 30, 40, 60]
areas = [0, 1, 20, 50, 80, 100]
sigma = 8
noise_level = 1/300
x_size = 100

X_data, y_classification, y_regression = generate_data(centers, areas, sigma, noise_level, x_size)

print("X_data shape:", X_data.shape)
print("y_classification shape:", y_classification.shape)
print("y_regression shape:", y_regression.shape)

# Output:
print("y_regression",y_regression[0])


