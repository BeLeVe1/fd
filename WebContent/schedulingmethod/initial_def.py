import numpy as np
import random
import copy
import numpy
from decoding_def import decoding
from fitness_def import fitness


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


def initial_ran(M, N, Ma, Manum, POP_SIZE, D, P, A, B):
    POP = []  # 第一段：车辆的作业顺序,第二段：车辆的作业月台
    for popsize in range(POP_SIZE):  # 生成POPSIZE个随机种群
        pop = np.zeros(2 * N, dtype=np.int)
        # 染色体的第一段：车辆的作业顺序
        Nh = list(range(1, N + 1))  # 自然数序列1,2,...
        random.shuffle(Nh)  # 打乱后
        for h in range(N):  # 第h个作业的车辆 任务h
            pop[h] = Nh[h]  # 染色体的第一段：车辆的作业顺序
            # 染色体的第二段：车辆的作业月台
            ran = random.randint(1, Manum[pop[h] - 1])  # 1~Manum之间的随机自然数
            # pop[h] 作业的车辆id Manum[pop[h]-1] 第h个任务对应的车辆可以使用的月台数量
            pop[h + N] = Ma[pop[h] - 1][ran - 1]  # 每个车辆可以选择的月台
        pop = pop.tolist()
        POP.append(pop)

    return POP  # 初始化种群



# M 机器数
# N 工件数
# Ma 每个零件可以使用的机器
# Manum 每个零件可以使用的机器数量
# POP_SIZE 种群数量
def initial(M, N, Ma, Manum, POP_SIZE, D, P, A, B):
    POP = []  # 第一段：车辆的作业顺序,第二段：车辆的作业月台

    # 使用fcfs先到先开始法则生成一个染色体
    # 按照开始作业时间进行排序
    pop = np.zeros(2 * N, dtype=np.int)
    D_s = []  # 每一项作业的开始时间
    for d in D:
        D_s.append(d[0])
    N_num = []  # 每一项作业
    for r in range(N):
        N_num.append(r + 1)
    pop_left, D_s_sorted = sort_s(N_num, D_s)  # 按照开始时间顺序排序的作业编号
    O = np.zeros(M, dtype=np.int)  # 记录月台完成上一个作业的时间

    for h in range(N):  # 第h个作业的车辆 任务h
        # 染色体的第一段
        pop[h] = pop_left[h]
        # 染色体的第二段
        finish_time = []  # 车辆在可以使用的月台上的加工时间
        for ma in Ma[pop[h] - 1]:  # 车辆可以使用的月台
            # 车辆在可以使用的月台上的加工时间 P[pop[h]-1][ma]
            # 几个月台 完成作业的时间，哪里可以最快完成作业就去哪里
            finish_time.append(copy.deepcopy(max(O[ma - 1], D_s_sorted[h]) + P[pop[h] - 1][ma - 1]))
        finish_time_min_pos = finish_time.index(min(finish_time))  # 在第几个月台上最早完成作业
        finish_time_min_ma = Ma[pop[h] - 1][finish_time_min_pos]  # 在哪个月台上最早完成作业
        pop[N + h] = finish_time_min_ma
        O[finish_time_min_ma - 1] = max(O[finish_time_min_ma - 1], D_s_sorted[h]) + P[pop[h] - 1][
            finish_time_min_ma - 1]
    pop = pop.tolist()
    POP.append(pop)

    # # 使用neh规则生成一个染色体
    # pop_neh_initial = []
    # for n in range(N):  # 所有车辆
    #     pop_neh_initial.append(copy.deepcopy(n + 1))
    # pop_p_max = []
    # # 　　每个车辆最长作业时间
    # for n in range(N):
    #     p_n = 0
    #     for manum in range(Manum[n]):
    #         if p_n < P[n][Ma[n][manum] - 1]:
    #             p_n = P[n][Ma[n][manum] - 1]
    #     pop_p_max.append(copy.deepcopy(p_n))
    # disp = zip(pop_neh_initial, pop_p_max)
    # Disp = dict(disp)
    # A_disp = sorted(Disp.items(), key=lambda item: item[1])
    # Disp_sorted = dict(A_disp)
    # # print(Disp_sorted)
    # pop_neh_1 = []  # 生成的基因
    # pop_neh_2 = []
    # for j, (k, v) in enumerate(Disp_sorted.items()):  # enumerate获得索引和值的方法
    #     pop_neh_insert = []
    #     for pos in range(len(pop_neh_1) + 1):
    #         for ma in Ma[k - 1]:
    #             pop_neh_insert.append(
    #                 pop_neh_1[:pos] + [k] + pop_neh_1[pos:] + pop_neh_2[:pos] + [ma] + pop_neh_2[pos:])
    #     # 选出这个任务插入的最佳位置
    #     # 解码
    #     # S 车辆任务开始作业的时间
    #     # E 车辆任务结束作业的时间
    #     # O 月台占用的时间
    #     S, E, O = decoding(pop_neh_insert, N, M, P, D, A, B)
    #     # 适应度
    #     Fit_neh_insert, ET_penalty_neh_insert = fitness(A, B, S, E, D)
    #     pop_neh_1 = pop_neh_insert[Fit_neh_insert.index(max(Fit_neh_insert))][:int(len(pop_neh_insert[0]) / 2)]
    #     pop_neh_2 = pop_neh_insert[Fit_neh_insert.index(max(Fit_neh_insert))][int(len(pop_neh_insert[0]) / 2):]
    # POP.append(pop_neh_1 + pop_neh_2)

    for popsize in range(POP_SIZE - 1):  # 生成POPSIZE个随机种群
        pop = np.zeros(2 * N, dtype=np.int)
        # 染色体的第一段：车辆的作业顺序
        Nh = list(range(1, N + 1))  # 自然数序列1,2,...
        random.shuffle(Nh)  # 打乱后
        for h in range(N):  # 第h个作业的车辆 任务h
            pop[h] = Nh[h]  # 染色体的第一段：车辆的作业顺序
            # 染色体的第二段：车辆的作业月台
            ran = random.randint(1, Manum[pop[h] - 1])  # 1~Manum之间的随机自然数
            # pop[h] 作业的车辆id Manum[pop[h]-1] 第h个任务对应的车辆可以使用的月台数量
            pop[h + N] = Ma[pop[h] - 1][ran - 1]  # 每个车辆可以选择的月台
        pop = pop.tolist()
        POP.append(pop)

    return POP  # 初始化种群


def reinitial_insert(POP, N, Ma, Manum):
    POP_reinitial = []
    # 对len(POP)个个体进行随机插入
    for pop_reinitial_in in POP[0:len(POP)]:
        pop_neh = pop_insert_1(pop_reinitial_in, N, Ma, Manum)
        POP_reinitial.append(copy.deepcopy(pop_neh))
    return POP_reinitial


# 对一个个体进行随机插入
def pop_insert_1(pop_reinitial_neh, N, Ma, Manum):
    pop_neh_copy_1 = copy.deepcopy(pop_reinitial_neh[0:N])
    pop_neh_copy_2 = copy.deepcopy(pop_reinitial_neh[N:2 * N])
    h = np.random.randint(low=0, high=N)
    # 随意去除h个基因
    pop_h_1 = []  # 去除的h个基因
    pop_h_2 = []
    for h_in in range(h):
        ran = np.random.randint(low=0, high=len(pop_neh_copy_1))
        pop_h_1.append(copy.deepcopy(pop_neh_copy_1[ran]))
        pop_h_2.append(copy.deepcopy(pop_neh_copy_2[ran]))
        del pop_neh_copy_1[ran]
        del pop_neh_copy_2[ran]
    # 重新随机插入
    for pop_insert_n in range(len(pop_h_1)):  # 对于每一个需要插入的任务
        ran_pos = np.random.randint(low=0, high=len(pop_neh_copy_1) + 1)  # 所有可以插入的位置
        pop_neh_copy_1.insert(ran_pos, pop_h_1[pop_insert_n])
        # pop_best_copy_2.insert(ran_pos, pop_best_h_2[pop_insert_n])
        pop_neh_copy_2.insert(ran_pos, Ma[pop_h_1[pop_insert_n] - 1][
            numpy.random.randint(low=0, high=Manum[pop_h_1[pop_insert_n] - 1])])
    return pop_neh_copy_1 + pop_neh_copy_2

def reinitial_swap(POP, N):
    POP_reinitial = []
    # 对len(POP)个个体进行随机swap
    for pop_reinitial_in in POP[0:len(POP)]:
        pop_swap = pop_swap_1(pop_reinitial_in, N)
        POP_reinitial.append(copy.deepcopy(pop_swap))
    return POP_reinitial

def pop_swap_1(pop_swap, N):
    pop_swap_copy_1 = copy.deepcopy(pop_swap[0:N])
    pop_swap_copy_2 = copy.deepcopy(pop_swap[N:2 * N])
    ran1 = np.random.randint(low=0, high=len(pop_swap_copy_1))
    ran2 = np.random.randint(low=0, high=len(pop_swap_copy_1))
    while ran2 == ran1:  # ran2不可以等于ran1
        ran2 = np.random.randint(low=0, high=len(pop_swap_copy_1))
    pop_best_copy_1_reverse = pop_swap_copy_1[ran1:ran2]
    pop_best_copy_1_reverse.reverse()
    pop_best_copy_2_reverse = pop_swap_copy_2[ran1:ran2]
    pop_best_copy_2_reverse.reverse()
    pop_swap_copy_1[ran1:ran2] = pop_best_copy_1_reverse
    pop_swap_copy_2[ran1:ran2] = pop_best_copy_2_reverse
    return pop_swap_copy_1 + pop_swap_copy_2

def initial_group(M, N, Ma, Manum, POP_SIZE, D, P, A, B):
    POP = []  # 第一段：车辆的作业顺序,第二段：车辆的作业月台
    # 使用fcfs先到先开始法则生成一个染色体
    # 按照开始作业时间进行排序
    pop_fcfs = np.zeros(2 * N, dtype=np.int)
    D_s = []  # 每一项作业的开始时间
    for d in D:
        D_s.append(d[0])
    N_num = []  # 每一项作业
    for r in range(N):
        N_num.append(r + 1)
    pop_left, D_s_sorted = sort_s(N_num, D_s)  # 按照开始时间顺序排序的作业编号
    O = np.zeros(M, dtype=np.int)  # 记录月台完成上一个作业的时间

    for h in range(N):  # 第h个作业的车辆 任务h
        # 染色体的第一段
        pop_fcfs[h] = pop_left[h]
        # 染色体的第二段
        finish_time = []  # 车辆在可以使用的月台上的加工时间
        for ma in Ma[pop_fcfs[h] - 1]:  # 车辆可以使用的月台
            # 车辆在可以使用的月台上的加工时间 P[pop[h]-1][ma]
            # 几个月台 完成作业的时间，哪里可以最快完成作业就去哪里
            finish_time.append(copy.deepcopy(max(O[ma - 1], D_s_sorted[h]) + P[pop_fcfs[h] - 1][ma - 1]))
        finish_time_min_pos = finish_time.index(min(finish_time))  # 在第几个月台上最早完成作业
        finish_time_min_ma = Ma[pop_fcfs[h] - 1][finish_time_min_pos]  # 在哪个月台上最早完成作业
        pop_fcfs[N + h] = finish_time_min_ma
        O[finish_time_min_ma - 1] = max(O[finish_time_min_ma - 1], D_s_sorted[h]) + P[pop_fcfs[h] - 1][
            finish_time_min_ma - 1]
    pop_fcfs = pop_fcfs.tolist()
    POP.append(pop_fcfs)

    # 使用neh规则生成一个染色体
    pop_neh_initial = []
    for n in range(N):  # 所有车辆
        pop_neh_initial.append(copy.deepcopy(n + 1))
    pop_p_max = []
    # 　　每个车辆最长作业时间
    for n in range(N):
        p_n = 0
        for manum in range(Manum[n]):
            if p_n < P[n][Ma[n][manum] - 1]:
                p_n = P[n][Ma[n][manum] - 1]
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
        for pos in range(len(pop_neh_1) + 1):
            for ma in Ma[k - 1]:
                pop_neh_insert.append(
                    pop_neh_1[:pos] + [k] + pop_neh_1[pos:] + pop_neh_2[:pos] + [ma] + pop_neh_2[pos:])
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
    POP.append(pop_neh_1 + pop_neh_2)

    for popsize in range(int((POP_SIZE - 4) / 2)):  # 生成POPSIZE个随机种群
        pop = np.zeros(2 * N, dtype=np.int)
        # 染色体的第一段：车辆的作业顺序
        Nh = list(range(1, N + 1))  # 自然数序列1,2,...
        random.shuffle(Nh)  # 打乱后
        for h in range(N):  # 第h个作业的车辆 任务h
            pop[h] = Nh[h]  # 染色体的第一段：车辆的作业顺序
            # 染色体的第二段：车辆的作业月台
            ran = random.randint(1, Manum[pop[h] - 1])  # 1~Manum之间的随机自然数
            # pop[h] 作业的车辆id Manum[pop[h]-1] 第h个任务对应的车辆可以使用的月台数量
            pop[h + N] = Ma[pop[h] - 1][ran - 1]  # 每个车辆可以选择的月台
        pop = pop.tolist()
        POP.append(pop)
    POP.append(pop_fcfs)
    POP.append(pop_neh_1 + pop_neh_2)
    for popsize in range(int((POP_SIZE - 4) / 2)):  # 生成POPSIZE个随机种群
        pop = np.zeros(2 * N, dtype=np.int)
        # 染色体的第一段：车辆的作业顺序
        Nh = list(range(1, N + 1))  # 自然数序列1,2,...
        random.shuffle(Nh)  # 打乱后
        for h in range(N):  # 第h个作业的车辆 任务h
            pop[h] = Nh[h]  # 染色体的第一段：车辆的作业顺序
            # 染色体的第二段：车辆的作业月台
            ran = random.randint(1, Manum[pop[h] - 1])  # 1~Manum之间的随机自然数
            # pop[h] 作业的车辆id Manum[pop[h]-1] 第h个任务对应的车辆可以使用的月台数量
            pop[h + N] = Ma[pop[h] - 1][ran - 1]  # 每个车辆可以选择的月台
        pop = pop.tolist()
        POP.append(pop)
    return POP  # 初始化种群
