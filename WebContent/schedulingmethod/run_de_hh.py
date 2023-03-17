import numpy as np
import copy
import matplotlib.pyplot as plt

from action_choose_def import action_choose
from initial_def import initial, reinitial_swap, reinitial_insert, initial_ran
from fitness_def import fitness, et_getfit
from decoding_def import decoding, decoding_
from crossover_def import crossover_pox, crossover_ppx, crossover_bin
from pls_def import pls, dc, insertimprovement
from select_def import select, select_sa
from mutation_def import mutation_neh_best, mutation_2, mutation_3, mutation_swap_best, mutation_swap_rand, \
    mutation_insert_best_rand, mutation_insert_rand_rand, mutation_rand_pox
from gantt_def import gantt
import time
import math
from individual_density_def import individual_density
from vnd_def import NEII, NEIS, NEEI, NEES, NEIGS, NESIGS

# 8
Lbn = [1, 5, 1, 5, 2, 5, 1, 3, 3, 5, 3, 1, 1, 2, 5, 1, 2, 1, 5, 3, 3, 2, 1, 3, 1, 1, 1, 2, 1, 5, 5, 4, 5, 5, 2, 2, 5, 1, 4, 5, 5, 3, 2, 3, 1, 3, 2, 4, 2, 4]
Lbm = [[1], [2], [3], [4], [5], [1, 2], [2, 3], [3, 4], [4, 5], [1, 2, 3, 4, 5]]
A = [1, 1, 1, 1, 1, 1, 1, 5, 1, 5, 5, 1, 1, 5, 1, 1, 1, 5, 1, 1, 1, 5, 1, 5, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1]
B = [2, 2, 2, 2, 2, 2, 2, 10, 2, 10, 10, 2, 2, 10, 2, 2, 2, 10, 2, 2, 2, 10, 2, 10, 2, 2, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2]
P = [[46, 999, 999, 999, 999, 75, 999, 999, 999, 48], [999, 999, 999, 999, 79, 999, 999, 999, 48, 83], [53, 999, 999, 999, 999, 21, 999, 999, 999, 50], [999, 999, 999, 999, 60, 999, 999, 999, 57, 51], [999, 17, 999, 999, 999, 23, 57, 999, 999, 94], [999, 999, 999, 999, 80, 999, 999, 999, 52, 64], [87, 999, 999, 999, 999, 36, 999, 999, 999, 84], [999, 999, 83, 999, 999, 999, 17, 53, 999, 79], [999, 999, 46, 999, 999, 999, 47, 53, 999, 44], [999, 999, 999, 999, 43, 999, 999, 999, 46, 81], [999, 999, 33, 999, 999, 999, 35, 13, 999, 50], [50, 999, 999, 999, 999, 66, 999, 999, 999, 32], [72, 999, 999, 999, 999, 85, 999, 999, 999, 85], [999, 73, 999, 999, 999, 36, 20, 999, 999, 68], [999, 999, 999, 999, 43, 999, 999, 999, 77, 65], [37, 999, 999, 999, 999, 99, 999, 999, 999, 50], [999, 32, 999, 999, 999, 70, 58, 999, 999, 50], [21, 999, 999, 999, 999, 13, 999, 999, 999, 75], [999, 999, 999, 999, 57, 999, 999, 999, 33, 31], [999, 999, 64, 999, 999, 999, 28, 32, 999, 15], [999, 999, 16, 999, 999, 999, 11, 57, 999, 39], [999, 40, 999, 999, 999, 28, 65, 999, 999, 97], [66, 999, 999, 999, 999, 77, 999, 999, 999, 92], [999, 999, 62, 999, 999, 999, 54, 41, 999, 76], [19, 999, 999, 999, 999, 90, 999, 999, 999, 10], [39, 999, 999, 999, 999, 13, 999, 999, 999, 26], [33, 999, 999, 999, 999, 13, 999, 999, 999, 79], [999, 59, 999, 999, 999, 38, 30, 999, 999, 71], [93, 999, 999, 999, 999, 83, 999, 999, 999, 66], [999, 999, 999, 999, 34, 999, 999, 999, 15, 43], [999, 999, 999, 999, 30, 999, 999, 999, 86, 77], [999, 999, 999, 86, 999, 999, 999, 54, 61, 26], [999, 999, 999, 999, 85, 999, 999, 999, 70, 12], [999, 999, 999, 999, 75, 999, 999, 999, 40, 90], [999, 13, 999, 999, 999, 72, 22, 999, 999, 34], [999, 50, 999, 999, 999, 100, 76, 999, 999, 15], [999, 999, 999, 999, 70, 999, 999, 999, 58, 77], [31, 999, 999, 999, 999, 11, 999, 999, 999, 18], [999, 999, 999, 28, 999, 999, 999, 44, 90, 34], [999, 999, 999, 999, 92, 999, 999, 999, 24, 26], [999, 999, 999, 999, 40, 999, 999, 999, 71, 24], [999, 999, 15, 999, 999, 999, 37, 96, 999, 48], [999, 52, 999, 999, 999, 80, 40, 999, 999, 20], [999, 999, 28, 999, 999, 999, 92, 85, 999, 10], [17, 999, 999, 999, 999, 98, 999, 999, 999, 64], [999, 999, 93, 999, 999, 999, 64, 21, 999, 61], [999, 55, 999, 999, 999, 63, 61, 999, 999, 37], [999, 999, 999, 64, 999, 999, 999, 63, 72, 83], [999, 92, 999, 999, 999, 23, 91, 999, 999, 54], [999, 999, 999, 59, 999, 999, 999, 27, 17, 20]]
D = [[95, 192], [102, 157], [89, 110], [34, 113], [322, 369], [251, 329], [57, 154], [26, 84], [120, 164], [125, 235], [88, 124], [266, 335], [75, 177], [235, 299], [198, 270], [8, 93], [316, 364], [83, 98], [291, 327], [112, 190], [32, 67], [291, 401], [63, 132], [267, 332], [211, 223], [249, 279], [79, 181], [141, 196], [320, 396], [312, 344], [290, 340], [135, 175], [170, 228], [166, 209], [61, 129], [267, 329], [140, 210], [122, 157], [67, 168], [74, 183], [192, 227], [121, 246], [267, 315], [84, 190], [152, 230], [23, 92], [116, 181], [34, 138], [276, 312], [284, 348]]
# 1
Lbn = [3, 2, 5, 2, 4, 4, 4, 4, 2, 3, 4, 5, 5, 4, 5, 2, 5, 5, 4, 5, 4, 3, 1, 2, 4, 1, 4, 3, 3, 5, 3, 1, 2, 1, 1, 5, 2, 5,
       2, 2, 1, 4, 2, 5, 5, 1, 5, 5, 1, 1]
Lbm = [[1], [2], [3], [4], [5], [1, 2], [2, 3], [3, 4], [4, 5], [1, 2, 3, 4, 5]]
A = [5, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 5, 5, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 5, 1, 1, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
B = [10, 2, 2, 2, 2, 2, 2, 10, 10, 2, 2, 10, 10, 2, 2, 2, 10, 2, 2, 2, 2, 2, 2, 10, 2, 10, 2, 2, 10, 2, 2, 2, 2, 2, 2,
     10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
P = [[999, 999, 95, 999, 999, 999, 20, 97, 999, 31], [999, 21, 999, 999, 999, 70, 67, 999, 999, 13],
     [999, 999, 999, 999, 94, 999, 999, 999, 72, 55], [999, 93, 999, 999, 999, 65, 37, 999, 999, 63],
     [999, 999, 999, 46, 999, 999, 999, 52, 34, 78], [999, 999, 999, 47, 999, 999, 999, 24, 97, 13],
     [999, 999, 999, 89, 999, 999, 999, 45, 16, 96], [999, 999, 999, 57, 999, 999, 999, 41, 50, 84],
     [999, 16, 999, 999, 999, 54, 71, 999, 999, 18], [999, 999, 45, 999, 999, 999, 79, 55, 999, 80],
     [999, 999, 999, 44, 999, 999, 999, 33, 39, 28], [999, 999, 999, 999, 51, 999, 999, 999, 55, 37],
     [999, 999, 999, 999, 56, 999, 999, 999, 23, 13], [999, 999, 999, 16, 999, 999, 999, 45, 85, 70],
     [999, 999, 999, 999, 93, 999, 999, 999, 94, 95], [999, 21, 999, 999, 999, 41, 61, 999, 999, 58],
     [999, 999, 999, 999, 25, 999, 999, 999, 100, 77], [999, 999, 999, 999, 44, 999, 999, 999, 58, 94],
     [999, 999, 999, 78, 999, 999, 999, 69, 99, 76], [999, 999, 999, 999, 51, 999, 999, 999, 42, 99],
     [999, 999, 999, 97, 999, 999, 999, 31, 74, 95], [999, 999, 85, 999, 999, 999, 24, 95, 999, 24],
     [45, 999, 999, 999, 999, 63, 999, 999, 999, 53], [999, 35, 999, 999, 999, 18, 37, 999, 999, 65],
     [999, 999, 999, 22, 999, 999, 999, 96, 29, 65], [47, 999, 999, 999, 999, 54, 999, 999, 999, 36],
     [999, 999, 999, 63, 999, 999, 999, 66, 51, 11], [999, 999, 16, 999, 999, 999, 30, 34, 999, 76],
     [999, 999, 66, 999, 999, 999, 87, 60, 999, 31], [999, 999, 999, 999, 79, 999, 999, 999, 93, 42],
     [999, 999, 37, 999, 999, 999, 89, 95, 999, 80], [20, 999, 999, 999, 999, 32, 999, 999, 999, 92],
     [999, 94, 999, 999, 999, 92, 36, 999, 999, 62], [61, 999, 999, 999, 999, 84, 999, 999, 999, 88],
     [40, 999, 999, 999, 999, 32, 999, 999, 999, 35], [999, 999, 999, 999, 51, 999, 999, 999, 15, 66],
     [999, 42, 999, 999, 999, 45, 55, 999, 999, 100], [999, 999, 999, 999, 42, 999, 999, 999, 10, 92],
     [999, 18, 999, 999, 999, 33, 10, 999, 999, 65], [999, 51, 999, 999, 999, 69, 21, 999, 999, 37],
     [10, 999, 999, 999, 999, 32, 999, 999, 999, 93], [999, 999, 999, 20, 999, 999, 999, 66, 38, 82],
     [999, 82, 999, 999, 999, 31, 46, 999, 999, 25], [999, 999, 999, 999, 89, 999, 999, 999, 50, 38],
     [999, 999, 999, 999, 85, 999, 999, 999, 86, 45], [56, 999, 999, 999, 999, 77, 999, 999, 999, 92],
     [999, 999, 999, 999, 79, 999, 999, 999, 88, 58], [999, 999, 999, 999, 82, 999, 999, 999, 63, 52],
     [19, 999, 999, 999, 999, 36, 999, 999, 999, 83], [91, 999, 999, 999, 999, 51, 999, 999, 999, 32]]
D = [[233, 293], [64, 105], [373, 466], [307, 401], [234, 313], [122, 214], [40, 138], [321, 413], [141, 182],
     [59, 109], [134, 179], [260, 308], [299, 333], [379, 409], [56, 161], [388, 422], [260, 346], [373, 438],
     [252, 356], [307, 398], [278, 389], [134, 208], [227, 299], [186, 231], [237, 294], [62, 124], [128, 145],
     [101, 149], [154, 190], [165, 234], [166, 246], [48, 133], [308, 404], [215, 279], [268, 315], [155, 232],
     [320, 387], [331, 397], [387, 415], [189, 259], [265, 295], [61, 158], [186, 234], [105, 189], [118, 212],
     [254, 351], [99, 170], [50, 123], [349, 412], [203, 287]]

M = len(Lbm)  # 机器数
N = len(Lbn)  # 工件数
Ma = [[] for _ in range(N)]  # 每个零件可以使用的机器
Manum = np.zeros(N, dtype=np.int)  # 每个零件可以使用的机器数量
for n1 in range(N):  # 对于每个工件，计算Ma
    lbn = Lbn[n1]  # 这个工件在哪个类别的机器上加工
    for m in range(M):  # 每一个机器
        lbm = Lbm[m]  # lbm 机器m可以加工的类别
        i = 0
        lbmnum = len(Lbm[m])
        for l in range(lbmnum):  # 对于机器的每一个类别
            if lbm[i] == lbn:
                Ma[n1].append(m + 1)
                Manum[n1] += 1
                break
            i += 1

# 10个月台

gen = 100  # 迭代次数
POP_SIZE = 50  # 种群数量
pm = 0.6
pc = 0.8
d = 45  # 滑动时间窗
for g_gen in range(10):
    print(g_gen)
    time_start = time.time()
    POP = []
    Fit_POP = []
    ET_penalty_POP = []

    fit_max = []  # 储存算法跑出来的每一代的最优解的fitness
    pop_best = []  # 储存每一代的最优解
    et_min = []  # 储存每一代最小的惩罚值

    # 初始化种群
    POP_new = initial(M, N, Ma, Manum, POP_SIZE, D, P, A, B)
    # 解码
    # S 车辆任务开始作业的时间
    # E 车辆任务结束作业的时间
    # O 月台占用的时间
    S, E, O = decoding(POP_new, N, M, P, D, A, B)
    # 适应度
    Fit_POP_new, ET_penalty_POP_new = fitness(A, B, S, E, D)
    # print(Fit)

    # 找出最大的fitness
    maxre_f = copy.deepcopy(max(Fit_POP_new))
    h = Fit_POP_new.index(maxre_f)
    maxre_p = copy.deepcopy(POP_new[h])
    minre_et = copy.deepcopy(ET_penalty_POP_new[h])
    fit_max.append(maxre_f)
    pop_best.append(maxre_p)
    et_min.append(minre_et)
    # print(minre_et)

    # 记录最近d次的action
    action_list = []
    # 记录最近d次的reward
    reward_list = []
    # 记录最近d次的
    # 有几个action
    action_num = 6
    g = 0
    while g < gen and minre_et != 0:
        # print(g)
        action_choice = action_choose(action_num, action_list, reward_list)

        POP[:] = []
        POP = POP + POP_new
        POP_new[:] = []

        Fit_POP[:] = []
        Fit_POP = Fit_POP + Fit_POP_new
        Fit_POP_new[:] = []

        ET_penalty_POP[:] = []
        ET_penalty_POP = ET_penalty_POP + ET_penalty_POP_new
        ET_penalty_POP_new[:] = []
        # 变异
        if action_choice == 0 or action_choice == 3:
            # 对所有个体进行随机swap，效果比较好，940左右在200代左右停下，多样性还可以
            POP_mutation = mutation_swap_rand(POP, POP, N, pm)
        if action_choice == 1 or action_choice == 4:
            # 随机3个做pox，效果比较好，950左右300代左右停下
            POP_mutation = mutation_rand_pox(POP, POP, N, pm)
        if action_choice == 2 or action_choice == 5:
            # 对最优个体进行随机插入，有点用，作用不大，1100左右500代一直进化速度较慢
            # POP_mutation = mutation_insert_best_rand(pop_best[fit_max.index(max(fit_max))], POP, N, Ma, Manum)

            # 对随机个体进行随机插入，基本没有什么用
            POP_mutation = mutation_insert_rand_rand(POP, POP, N, Ma, Manum, pm)
            # 对最优个体进行swap，基本没有效果
            # POP_mutation = mutation_swap_best(pop_best[fit_max.index(max(fit_max))], POP, N)
            # POP_mutation = mutation_neh_best(maxre_p, POP, N, M, P, D, A, B, Ma)
        # 交叉
        if action_choice <= 2:
            POP_crossover = crossover_pox(POP, POP_mutation, N, pc)
        else:
            POP_crossover = crossover_ppx(POP, POP_mutation, N, pc)
        # 解码
        S, E, O = decoding(POP_crossover, N, M, P, D, A, B)
        # 适应度
        Fit_crossover, ET_penalty_crossover = fitness(A, B, S, E, D)
        # 贪婪选择
        POP_new, Fit_POP_new, ET_penalty_POP_new = select(POP, POP_crossover, Fit_POP, ET_penalty_POP, Fit_crossover,
                                                          ET_penalty_crossover)
        # 找出最大的fitness
        maxre_f = copy.deepcopy(max(Fit_POP_new))
        h = Fit_POP_new.index(maxre_f)
        maxre_p = copy.deepcopy(POP_new[h])
        minre_et = copy.deepcopy(ET_penalty_POP_new[h])
        # 更新动作
        if len(action_list) < d:  # 时间窗大小为d
            action_list.append(copy.deepcopy(action_choice))
        else:
            action_list.pop(0)
            action_list.append(copy.deepcopy(action_choice))
        # print('action列表', action_list)

        if len(reward_list) < d:  # 时间窗大小为d
            reward_list.append(copy.deepcopy((np.mean(Fit_POP_new) - np.mean(Fit_POP))))
        else:
            reward_list.pop(0)
            reward_list.append(copy.deepcopy((np.mean(Fit_POP_new) - np.mean(Fit_POP))))
        # print('reward 列表', reward_list)

        # 记录当前最优解
        pop_best.append(maxre_p)
        et_min.append(minre_et)
        fit_max.append(maxre_f)

        # print(ET_penalty_POP_new)
        # print(minre_et)
        g += 1
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
    # # 绘图
    maxre_f = max(fit_max)
    h = fit_max.index(maxre_f)
    minre_et = copy.deepcopy(et_min[h])
    print('fit', maxre_f)
    print('et', minre_et)
    print('pop', pop_best[h])
    print('fit_max', fit_max)
    print('et_min', et_min)
    print('')

    # # 绘制迭代gen代最优个体fitness散点图
    # plt.figure()
    # x = range(len(fit_max))
    # y = fit_max
    # plt.scatter(x, y)
    # plt.title("fitness figure")
    # plt.xlabel("iteration")
    # plt.ylabel("fitness value")
    # plt.xticks(np.arange(0, len(fit_max), int(gen/10)), np.arange(0, len(fit_max), int(gen/10)))  # 替换x坐标
    # plt.show()
    #
    # # 绘制迭代gen代最优个体et_min散点图
    # plt.figure()
    # x = range(len(et_min))
    # y = et_min
    # plt.scatter(x, y)
    # plt.title("E/T penalty figure")
    # plt.xlabel("iteration")
    # plt.ylabel("penalty value")
    # plt.xticks(np.arange(0, len(et_min), int(gen/10)), np.arange(0, len(et_min), int(gen/10))) # 替换x坐标
    # plt.show()
    #
    # # 最优调度方案 绘制甘特图
    # gantt(pop_best[h], P, N, M, P, D, A, B)
