Class1_model 比较了model在intensity最大最小比值从100:1 到 1000:1 的表现
Final_model 提取了model中600:1的成果 并保存了model在my_model.h5中

在demonstration中 通过手动替换my_model文件 可以展示model 在具体情况下的预测表现，demonstration.py展示了原本的光谱图与最终预测出的光谱图的区别 并展示了pred的area value

Class1_model 在最后可视化了model在不同比例下的absolute error（pred-true） 和  relative error(pred-true)/true的 avg mean median std max min 值


Generation file是原先生成数据到excel中使用的



训练数据是利用多个高斯峰拟合出的合成峰 合成函数在final_version的Generate_comparision中



使用vscode远程连接服务器
Docker 环境下 
使用 Dockerfile 编译环境
sudo docker build -t my-jupyter-notebook-gpu .

启动
sudo docker run --gpus all -it --rm -p 8888:8888 -v $(pwd):/workspace my-jupyter-notebook-gpu

浏览器打开后复制terminal中的token并login即可进入
