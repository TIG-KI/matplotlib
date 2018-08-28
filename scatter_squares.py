"""绘制散点图并设置其样式"""
import matplotlib.pyplot as plt
# plt.scatter(2, 4)
# pylint: disable=no-member

#自动计算数据
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

"""
    表示数据点的颜色可以直接指定名称，也可以传入rgb颜色参数
    plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
    edgecolors='none', s=40)
    使用颜色映射（colormap）颜色渐变
"""
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
    edgecolors='none', s=40)

#设置图标标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()