# Q_min Q的最小值
# Q_max
# t 迭代代数
# t_max 最大迭代代数
def Q(Q_min, Q_max, t, t_max):
    Q_res = Q_min + (Q_max - Q_min) * (t / t_max) ** 3.5
    return Q_res

# Q_min = 5
# Q_max = 18
# t_max = 150
# t_list = []
# for i in range(151):
#     t_list.append(i)
# Q_list = []
# for t_in in t_list:
#     Q_list.append(Q(Q_min, Q_max, t_in, t_max))
# import matplotlib.pyplot as plt
# # 绘制迭代gen代最优个体fitness散点图
# plt.figure()
# plt.scatter(t_list, Q_list)
# plt.show()