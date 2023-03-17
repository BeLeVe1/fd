import numpy as np
import copy
from fitness_def import fitness
from gantt_def import gantt
Lbn = [3, 2, 1, 3, 3, 1, 3, 1, 2, 3, 3, 2, 1, 3, 2, 3, 1, 2, 1, 2, 2, 1, 1, 3, 3, 3, 2, 1, 3, 3, 2, 2, 3, 1, 3, 2, 2, 2, 2, 3, 3, 2, 1, 1, 2, 2, 3, 3, 1, 3]
Lbm = [[1], [2], [3], [1, 2], [2, 3], [1, 3]]
A = [2, 6, 8, 6, 10, 4, 8, 2, 10, 8, 10, 10, 4, 6, 6, 6, 6, 6, 4, 8, 6, 2, 4, 10, 8, 8, 6, 6, 2, 2, 10, 4, 10, 4, 10, 8, 4, 2, 4, 6, 8, 4, 6, 8, 4, 8, 2, 2, 2, 6]
B = [1, 3, 4, 3, 5, 2, 4, 1, 5, 4, 5, 5, 2, 3, 3, 3, 3, 3, 2, 4, 3, 1, 2, 5, 4, 4, 3, 3, 1, 1, 5, 2, 5, 2, 5, 4, 2, 1, 2, 3, 4, 2, 3, 4, 2, 4, 1, 1, 1, 3]
P = [[999, 999, 76, 999, 93, 81], [999, 66, 999, 77, 94, 999], [71, 999, 999, 56, 999, 29], [999, 999, 54, 999, 79, 58], [999, 999, 84, 999, 58, 26], [11, 999, 999, 81, 999, 85], [999, 999, 41, 999, 38, 24], [97, 999, 999, 15, 999, 16], [999, 98, 999, 2, 60, 999], [999, 999, 35, 999, 60, 41], [999, 999, 84, 999, 20, 71], [999, 66, 999, 78, 14, 999], [100, 999, 999, 24, 999, 64], [999, 999, 22, 999, 94, 14], [999, 45, 999, 29, 89, 999], [999, 999, 9, 999, 48, 4], [77, 999, 999, 27, 999, 35], [999, 84, 999, 81, 65, 999], [90, 999, 999, 25, 999, 4], [999, 13, 999, 88, 47, 999], [999, 46, 999, 34, 18, 999], [87, 999, 999, 43, 999, 33], [77, 999, 999, 93, 999, 12], [999, 999, 76, 999, 50, 70], [999, 999, 67, 999, 72, 40], [999, 999, 84, 999, 35, 81], [999, 10, 999, 74, 67, 999], [38, 999, 999, 40, 999, 91], [999, 999, 55, 999, 49, 81], [999, 999, 34, 999, 100, 97], [999, 48, 999, 59, 81, 999], [999, 96, 999, 42, 31, 999], [999, 999, 58, 999, 75, 53], [2, 999, 999, 91, 999, 11], [999, 999, 91, 999, 73, 79], [999, 30, 999, 83, 100, 999], [999, 97, 999, 66, 48, 999], [999, 84, 999, 6, 71, 999], [999, 7, 999, 92, 10, 999], [999, 999, 77, 999, 44, 31], [999, 999, 94, 999, 46, 36], [999, 87, 999, 42, 32, 999], [92, 999, 999, 34, 999, 88], [45, 999, 999, 47, 999, 54], [999, 55, 999, 82, 60, 999], [999, 70, 999, 43, 86, 999], [999, 999, 49, 999, 63, 78], [999, 999, 60, 999, 38, 80], [76, 999, 999, 26, 999, 10], [999, 999, 55, 999, 66, 14]]
D = [[78, 187], [169, 278], [228, 354], [185, 296], [105, 127], [306, 344], [69, 130], [289, 394], [162, 240], [103, 148], [257, 295], [387, 460], [91, 230], [371, 436], [42, 180], [268, 269], [442, 467], [291, 354], [238, 352], [293, 451], [257, 320], [27, 190], [213, 337], [322, 335], [423, 431], [40, 174], [19, 43], [336, 376], [148, 216], [286, 339], [227, 268], [408, 476], [47, 194], [95, 124], [73, 105], [21, 61], [285, 343], [102, 234], [130, 284], [280, 284], [34, 221], [85, 173], [4, 73], [326, 336], [10, 71], [357, 362], [54, 100], [152, 196], [109, 224], [187, 208]]

M = 0  # 机器数
N = 0  # 工件数
for n in Lbn:
    N += 1
for m in Lbm:
    M += 1

Lbmnum = np.zeros(M, dtype=np.int)  # 机器的类别数量
i = 0
for lbm in Lbm:
    for lbmm in lbm:  # 机器的类别数量的计算
        Lbmnum[i] += 1
    i += 1

Ma = []  # 每个零件可以使用的机器
for n in range(N):
    Ma.append([])
Manum = np.zeros(N, dtype=np.int)  # 每个零件可以使用的机器数量
for n1 in range(N):  # 对于每个工件，计算Ma
    lbn = Lbn[n1]  # 这个工件在哪个类别的机器上加工
    for m in range(M):  # 每一个机器
        lbm = Lbm[m]  # lbm 机器m可以加工的类别
        i = 0
        lbmnum = Lbmnum[m]
        for l in range(lbmnum):  # 对于机器的每一个类别
            if lbm[i] == lbn:
                Ma[n1].append(m + 1)
                Manum[n1] += 1
                break
            i += 1


def sort_s(N_num, D_s):
    # 排序
    disp = zip(N_num, D_s)
    Disp = dict(disp)
    A = sorted(Disp.items(), key=lambda item: item[1])
    D = dict(A)
    pop = []
    D_s_sorted = []
    for j, (k, v) in enumerate(D.items()):  # enumerate获得索引和值的方法
        pop.append(k)
        D_s_sorted.append(v)
    return pop, D_s_sorted


POP = []
#  染色体生成

D_s = []  # 每一项作业的开始时间
for d in D:
    D_s.append(d[0])
N_num = []  # 每一项作业
for r in range(N):
    N_num.append(r+1)
pop_left, D_s_sorted = sort_s(N_num, D_s)  # 按照开始时间顺序排序的作业编号

pop = np.zeros(2 * N, dtype=np.int)
O = np.zeros(M, dtype=np.int)  # 记录月台完成上一个作业的时间
e = []  # 车辆结束作业时间
s = []  # 车辆开始作业时间
for n1 in range(N):
    e.append([])
    s.append([])

for h in range(N):  # 第h个作业的车辆 任务h
    # 染色体的第一段
    pop[h] = pop_left[h]
    # 染色体的第二段
    finish_time = []  # 车辆在可以使用的月台上的加工时间
    for ma in Ma[pop[h] - 1]:  # 车辆可以使用的月台
        # 车辆在可以使用的月台上的加工时间 P[pop[h]-1][ma]
        # 几个月台 完成作业的时间，哪里可以最快完成作业就去哪里
        finish_time.append(copy.deepcopy(max(O[ma - 1], D_s_sorted[h]) + P[pop[h] - 1][ma-1]))
    finish_time_min_pos = finish_time.index(min(finish_time))  # 在第几个月台上最早完成作业
    finish_time_min_ma = Ma[pop[h] - 1][finish_time_min_pos]  # 在哪个月台上最早完成作业
    pop[N+h] = finish_time_min_ma
    s[pop[h]-1] = max(O[finish_time_min_ma - 1], D_s_sorted[h])
    e[pop[h]-1] = s[pop[h]-1] + P[pop[h] - 1][finish_time_min_ma-1]
    O[finish_time_min_ma - 1] = e[pop[h]-1]

S = []
S.append(s)
E = []
E.append(e)
Fit, ET_penalty = fitness(A, B, S, E, D)
print('fit', Fit[0])
print('penalty', ET_penalty[0])
MS = pop[N:2 * N]  # 对应的机器号 M1=1,M2=2,…
# 各工序加工时间 P
# 各工序开始时间 S
J = pop[0:N]  # 工件号 J1=1,J2=2
gantt(MS, P, s, J)

# 随机生成第二段
# for pop_size in range(50):
#     pop = np.zeros(2 * N, dtype=np.int)
#     for h in range(N):  # 第h个作业的车辆 任务h
#         # 染色体的第一段
#         pop[h] = pop_left[h]
#         # 染色体的第二段：车辆的作业月台
#         ran = random.randint(1, Manum[pop[h] - 1])  # 1~Manum之间的随机自然数
#         # pop[h] 作业的车辆id Manum[pop[h]-1] 第h个任务对应的车辆可以使用的月台数量
#         pop[h + N] = Ma[pop[h] - 1][ran - 1]  # 每个车辆可以选择的月台
#     pop = pop.tolist()
#     POP.append(pop)
# S,E,O = decoding(POP, N, M, P, D, A, B)
# Fit, ET_penalty = fitness(A, B, S, E, D)
#
# fit_max = []  # 储存每一代的最优解的fitness
# pop_best = []  # 储存每一代的最优解
# et_min = []  # 储存每一代最小的惩罚值
# maxre_f = copy.deepcopy(max(Fit))
# h = Fit.index(maxre_f)
# maxre_p = copy.deepcopy(POP[h])
# minre_et = copy.deepcopy(ET_penalty[h])
# fit_max.append(maxre_f)
# pop_best.append(maxre_p)
# et_min.append(minre_et)
#
# print('fit_max', fit_max)
# print('et_min', et_min)
# print('pop_best', pop_best)
#
# S, E, O = decoding_(maxre_p, N, M, P, D, A, B)
# MS = maxre_p[N:2 * N]  # 对应的机器号 M1=1,M2=2,…
# # 各工序加工时间 P
# # 各工序开始时间 S
# J = maxre_p[0:N]  # 工件号 J1=1,J2=2
# gantt(MS, P, S, J)
