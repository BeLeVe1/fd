import numpy as np
import copy
from decoding_def import decoding, decoding_
from fitness_def import fitness
from gantt_def import gantt

# （1）将每个工件在所有机器上的加工时间求和；对求和后的值进行从大到小排序；
# （2）首先选择第一个工件（加工时间最长的），用第二个工件插入到第一个工件的前后两个位置，计算fitness，小的被保存；
# （3）将上一步保存的序列固定位置，使用下一个工件插入到之前的工件中，并比较得出最小的fitness并保存；
# （4）重复上一步，得出最终结果。
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

pop_neh_initial = []
for n in range(N):  # 所有车辆
    pop_neh_initial.append(copy.deepcopy(n + 1))
pop_neh = []
pop_neh_fit = 0
pop_neh_penalty = 0
pop_p_max = []
# 　　每个车辆最长作业时间
for n in range(N):
    p_n = 0
    for manum in range(Manum[n]):
        if p_n < P[n][Ma[n][manum]-1]:
            p_n = P[n][Ma[n][manum]-1]
    pop_p_max.append(copy.deepcopy(p_n))
disp = zip(pop_neh_initial, pop_p_max)
Disp = dict(disp)
A_disp = sorted(Disp.items(), key=lambda item: item[1])
Disp_sorted = dict(A_disp)
# print(Disp_sorted)
pop_neh_1 = []  # 生成的基因
pop_neh_2 = []
for j, (k, v) in enumerate(Disp_sorted.items()):  # enumerate获得索引和值的方法
    pop_neh_insert = []
    for pos in range(len(pop_neh_1)+1):
        for ma in Ma[k-1]:
            pop_neh_insert.append(pop_neh_1[:pos] + [k] + pop_neh_1[pos:] + pop_neh_2[:pos] + [ma] + pop_neh_2[pos:])
    # 选出这个任务插入的最佳位置
    # 解码
    # S 车辆任务开始作业的时间
    # E 车辆任务结束作业的时间
    # O 月台占用的时间
    S, E, O = decoding(pop_neh_insert, N, M, P, D, A, B)
    # 适应度
    Fit_neh_insert, ET_penalty_neh_insert = fitness(A, B, S, E, D)
    pop_neh_1 = pop_neh_insert[Fit_neh_insert.index(max(Fit_neh_insert))][:int(len(pop_neh_insert[0]) / 2)]
    pop_neh_2 = pop_neh_insert[Fit_neh_insert.index(max(Fit_neh_insert))][int(len(pop_neh_insert[0]) / 2):]
    pop_neh_fit = max(Fit_neh_insert)
    pop_neh_penalty = min(ET_penalty_neh_insert)
pop_neh = pop_neh_1 + pop_neh_2
print('pop_neh', pop_neh)

# 解码
# S 车辆任务开始作业的时间
# E 车辆任务结束作业的时间
# O 月台占用的时间
S, E, O = decoding_(pop_neh, N, M, P, D, A, B)

print('Fit', pop_neh_fit)
print('ET_penalty', pop_neh_penalty)

# 甘特图
MS = pop_neh[N:2 * N]  # 对应的机器号 M1=1,M2=2,…
# 各工序加工时间 P
# 各工序开始时间 S
J = pop_neh[0:N]  # 工件号 J1=1,J2=2
gantt(MS, P, S, J)



