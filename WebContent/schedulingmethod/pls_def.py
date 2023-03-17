# 局部搜索策略
# 使用neh规则生成一个染色体
import numpy as np
import copy
import matplotlib.pyplot as plt
from initial_def import initial
from fitness_def import fitness
from decoding_def import decoding, decoding_


def pls(pop, pop_et, N, M, P, D, A, B, Ma):
    # 去除h个基因，并以此放回
    # 依次去除1个基因，并放回，循环至没有改进
    pop_dc = []
    ET_penalty_insert_min = 0
    # dc方法
    pop_best_copy_1 = []
    pop_best_copy_1 = pop_best_copy_1 + pop[0:N]
    pop_best_copy_2 = []
    pop_best_copy_2 = pop_best_copy_2 + pop[N:2 * N]
    POP_mu = []  # 变异产生的贡献向量
    h = np.random.randint(low=0, high=N)
    # 随意去除h个基因
    pop_best_h_1 = []  # 去除的h个基因
    pop_best_h_2 = []
    for h_in in range(h):
        ran = np.random.randint(low=0, high=len(pop_best_copy_1))
        pop_best_h_1.append(copy.deepcopy(pop_best_copy_1[ran]))
        pop_best_h_2.append(copy.deepcopy(pop_best_copy_2[ran]))
        del pop_best_copy_1[ran]
        del pop_best_copy_2[ran]
    # 重新插入
    for pop_insert_n in range(len(pop_best_h_1)):  # 对于每一个需要插入的任务
        POP_insert = []  # 对于这个插入的任务所产生的所有基因
        for pos in range(1 + len(pop_best_copy_1)):  # 把基因插入到每一个位置上
            for ma in Ma[pop_best_h_1[pop_insert_n] - 1]:
                POP_insert.append(
                    copy.deepcopy(pop_best_copy_1[:pos] + [pop_best_h_1[pop_insert_n]] + pop_best_copy_1[pos:]
                                  + pop_best_copy_2[:pos] + [ma] + pop_best_copy_2[pos:]))
        # 选出这个任务插入的最佳位置
        # 解码
        S, E, O = decoding(POP_insert, N, M, P, D, A, B)
        # 适应度
        Fit_insert, ET_penalty_insert = fitness(A, B, S, E, D)
        ET_penalty_insert_min = min(ET_penalty_insert)
        # 适应度最小的基因
        pop_best_copy_1 = POP_insert[Fit_insert.index(max(Fit_insert))][0:int(len(POP_insert[0]) / 2)]
        pop_best_copy_2 = POP_insert[Fit_insert.index(max(Fit_insert))][
                          int(len(POP_insert[0]) / 2):len(POP_insert[0])]
    if pop_et > ET_penalty_insert_min:
        pop_dc = pop_dc + pop_best_copy_1 + pop_best_copy_2
    else:
        pop_dc = pop
        # 解码
    S, E, O = decoding([pop_dc], N, M, P, D, A, B)
    # 适应度
    Fit_insert, ET_penalty_insert = fitness(A, B, S, E, D)
    # print(Fit_insert, ET_penalty_insert)

    # insertimprovement
    pop_insert = []  # 得出的结果
    # 解码
    S, E, O = decoding([pop_dc], N, M, P, D, A, B)
    # 适应度
    Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)
    pop_insert_1 = []
    pop_insert_2 = []
    pop_insert_1 = pop_insert_1 + pop_dc[:int(len(pop_dc) / 2)]
    pop_insert_2 = pop_insert_2 + pop_dc[int(len(pop_dc) / 2):]
    pop_dc_number = 0  # 去除的基因从第零个开始,用它对N求余
    con = 0  # 记录连续多少次优化没有效果
    while con < N:  # 去除哪个位置的基因 连续n个基因没有优化则停止
        Fit_insert_b = []
        ET_penalty_insert_b = []
        Fit_insert_b = Fit_insert_b + Fit_insert_a  # insert之前的适应度
        Fit_insert_a[:] = []
        ET_penalty_insert_a[:] = []

        pop_dc_num = pop_dc_number % N  # 去除并重新插入的基因
        # print('dijige', pop_dc_num)
        pop_insert_n = pop_insert_1[pop_dc_num]  # 去除1个基因
        del pop_insert_1[pop_dc_num]
        del pop_insert_2[pop_dc_num]
        # 重新插入
        POP_insert = []  # 对于这个插入的任务所产生的所有基因
        for pos in range(1 + len(pop_insert_1)):  # 把基因插入到每一个位置上
            for ma in Ma[pop_insert_n - 1]:
                POP_insert.append(
                    copy.deepcopy(pop_insert_1[:pos] + [pop_insert_n] + pop_insert_1[pos:]
                                  + pop_insert_2[:pos] + [ma] + pop_insert_2[pos:]))
        # 选出这个任务插入的最佳位置
        # 解码
        S, E, O = decoding(POP_insert, N, M, P, D, A, B)
        # 适应度
        Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)  # insert之后的适应度
        # 适应度最小的基因
        pop_insert_1 = POP_insert[Fit_insert_a.index(max(Fit_insert_a))][0:int(len(POP_insert[0]) / 2)]
        pop_insert_2 = POP_insert[Fit_insert_a.index(max(Fit_insert_a))][
                       int(len(POP_insert[0]) / 2):len(POP_insert[0])]
        # 解码
        S, E, O = decoding([pop_insert_1 + pop_insert_2], N, M, P, D, A, B)
        # 适应度
        Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)
        # print(Fit_insert_a, ET_penalty_insert_a)
        if Fit_insert_a[0] == Fit_insert_b[0]:
            con += 1  # 移动这一个位置的基因没有任何的效果
        else:
            con = 0
        pop_dc_number += 1  # 去除哪个位置的基因
    return pop_insert_1 + pop_insert_2, Fit_insert_a[0], ET_penalty_insert_a[0]


def dc(pop, pop_et, N, M, P, D, A, B, Ma):
    ET_penalty_insert_min = 0
    pop_dc = []
    # dc方法
    pop_best_copy_1 = []
    pop_best_copy_1 = pop_best_copy_1 + pop[0:N]
    pop_best_copy_2 = []
    pop_best_copy_2 = pop_best_copy_2 + pop[N:2 * N]
    POP_mu = []  # 变异产生的贡献向量
    h = np.random.randint(low=1, high=N)
    # 随意去除h个基因
    pop_best_h_1 = []  # 去除的h个基因
    pop_best_h_2 = []
    for h_in in range(h):
        ran = np.random.randint(low=0, high=len(pop_best_copy_1))
        pop_best_h_1.append(copy.deepcopy(pop_best_copy_1[ran]))
        pop_best_h_2.append(copy.deepcopy(pop_best_copy_2[ran]))
        del pop_best_copy_1[ran]
        del pop_best_copy_2[ran]
    # 重新插入
    for pop_insert_n in range(len(pop_best_h_1)):  # 对于每一个需要插入的任务
        POP_insert = []  # 对于这个插入的任务所产生的所有基因
        for pos in range(1 + len(pop_best_copy_1)):  # 把基因插入到每一个位置上
            for ma in Ma[pop_best_h_1[pop_insert_n] - 1]:
                POP_insert.append(
                    copy.deepcopy(pop_best_copy_1[:pos] + [pop_best_h_1[pop_insert_n]] + pop_best_copy_1[pos:]
                                  + pop_best_copy_2[:pos] + [ma] + pop_best_copy_2[pos:]))
        # 选出这个任务插入的最佳位置
        # 解码
        S, E, O = decoding(POP_insert, N, M, P, D, A, B)
        # 适应度
        Fit_insert, ET_penalty_insert = fitness(A, B, S, E, D)
        ET_penalty_insert_min = min(ET_penalty_insert)
        # 适应度最小的基因
        pop_best_copy_1 = POP_insert[Fit_insert.index(max(Fit_insert))][0:int(len(POP_insert[0]) / 2)]
        pop_best_copy_2 = POP_insert[Fit_insert.index(max(Fit_insert))][
                          int(len(POP_insert[0]) / 2):len(POP_insert[0])]
    if pop_et >= ET_penalty_insert_min:
        pop_dc = pop_dc + pop_best_copy_1 + pop_best_copy_2
    else:
        pop_dc = pop
    # 解码
    S, E, O = decoding([pop_dc], N, M, P, D, A, B)
    # 适应度
    Fit_insert, ET_penalty_insert = fitness(A, B, S, E, D)
    # print(Fit_insert, ET_penalty_insert)

    return pop_dc, Fit_insert[0], ET_penalty_insert[0]


def insertimprovement(pop, N, M, P, D, A, B, Ma):
    pop_insert = []  # 得出的结果
    # 解码
    S, E, O = decoding([pop], N, M, P, D, A, B)
    # 适应度
    Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)
    pop_insert_1 = []
    pop_insert_2 = []
    pop_insert_1 = pop_insert_1 + pop[:int(len(pop) / 2)]
    pop_insert_2 = pop_insert_2 + pop[int(len(pop) / 2):]
    pop_dc_number = 0  # 去除的基因从第零个开始,用它对N求余
    con = 0  # 记录连续多少次优化没有效果
    while con < N:  # 去除哪个位置的基因 连续n个基因没有优化则停止
        Fit_insert_b = []
        ET_penalty_insert_b = []
        Fit_insert_b = Fit_insert_b + Fit_insert_a  # insert之前的适应度
        Fit_insert_a[:] = []
        ET_penalty_insert_a[:] = []

        pop_dc_num = pop_dc_number % N  # 去除并重新插入的基因
        print('dijige', pop_dc_num)
        pop_insert_n = pop_insert_1[pop_dc_num]  # 去除1个基因
        del pop_insert_1[pop_dc_num]
        del pop_insert_2[pop_dc_num]
        # 重新插入
        POP_insert = []  # 对于这个插入的任务所产生的所有基因
        for pos in range(1 + len(pop_insert_1)):  # 把基因插入到每一个位置上
            for ma in Ma[pop_insert_n - 1]:
                POP_insert.append(
                    copy.deepcopy(pop_insert_1[:pos] + [pop_insert_n] + pop_insert_1[pos:]
                                  + pop_insert_2[:pos] + [ma] + pop_insert_2[pos:]))
        # 选出这个任务插入的最佳位置
        # 解码
        S, E, O = decoding(POP_insert, N, M, P, D, A, B)
        # 适应度
        Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)  # insert之后的适应度
        # 适应度最小的基因
        pop_insert_1 = POP_insert[Fit_insert_a.index(max(Fit_insert_a))][0:int(len(POP_insert[0]) / 2)]
        pop_insert_2 = POP_insert[Fit_insert_a.index(max(Fit_insert_a))][
                       int(len(POP_insert[0]) / 2):len(POP_insert[0])]
        # 解码
        S, E, O = decoding([pop_insert_1 + pop_insert_2], N, M, P, D, A, B)
        # 适应度
        Fit_insert_a, ET_penalty_insert_a = fitness(A, B, S, E, D)
        print(Fit_insert_a, ET_penalty_insert_a)
        if Fit_insert_a[0] == Fit_insert_b[0]:
            con += 1  # 移动这一个位置的基因没有任何的效果
        else:
            con = 0
        pop_dc_number += 1  # 去除哪个位置的基因
    return pop_insert_1 + pop_insert_2, Fit_insert_a[0], ET_penalty_insert_a[0]
