import numpy as np
import copy


# POP 父个体
# POP_mutation 变异个体
# CROSSOVER_RATE 交叉率
# N 工件数

def crossover_pox(POP, POP_mutation, N, pc):
    CROSSOVER_RATE = 0.5
    POP_crossover = []
    for i in range(len(POP)):  # 对于每一个种群
        pop_crssover_1 = []  # 染色体第一段
        pop_crssover_2 = []  # 染色体第二段
        pop = POP[i]  # 原个体
        pop_mu = POP_mutation[i]  # 变异个体
        if np.random.rand() < pc:
            for n in range(N):  # 取变异个体中的基因
                if np.random.rand() <= CROSSOVER_RATE and pop_mu[n] not in pop_crssover_1:
                    pop_crssover_1.append(copy.deepcopy(pop_mu[n]))
                    pop_crssover_2.append(copy.deepcopy(pop_mu[n + N]))
                else:
                    pop_crssover_1.append(0)
                    pop_crssover_2.append(0)
            # 取原个体中的基因,先删除已经取得的变异个体中的基因，之后按照顺序填入
            pop_copy = []
            pop_copy = pop_copy + pop[0:N]
            pop_2_copy = []
            pop_2_copy = pop_2_copy + pop[N:2*N]
            for pop_in in pop_crssover_1:
                if pop_in != 0:
                    del pop_2_copy[pop_copy.index(pop_in)]
                    del pop_copy[pop_copy.index(pop_in)]
            for n in range(len(pop_copy)):
                pop_crssover_1[pop_crssover_1.index(0)] = pop_copy[n]
                pop_crssover_2[pop_crssover_2.index(0)] = pop_2_copy[n]
            POP_crossover.append(copy.deepcopy(pop_crssover_1 + pop_crssover_2))
        else:
            POP_crossover.append(copy.deepcopy(pop_mu))
    return POP_crossover


def crossover_ppx(POP, POP_mutation, N, pc):
    # 优先级保存交叉
    POP_crossover = []
    for i in range(len(POP)):  # 对于每一个种群
        pop_crssover_1 = []
        pop_crssover_2 = []
        # 父个体
        pop_1 = copy.deepcopy(POP[i][:N])
        pop_2 = copy.deepcopy(POP[i][N:])
        # 变异个体
        pop_mu_1 = copy.deepcopy(POP_mutation[i][:N])
        pop_mu_2 = copy.deepcopy(POP_mutation[i][N:])
        if np.random.rand() < pc:
            ran_table = []  # 随机表
            for n in range(N):  # 随机表生成
                ran_table.append(copy.deepcopy(np.random.randint(low=0, high=2)))  # 取值只能为0， 1
            for n in range(N):
                if ran_table[n] == 0:
                    pop_crssover_1.append(copy.deepcopy(pop_1[0]))
                    pop_crssover_2.append(copy.deepcopy(pop_2[0]))
                    # 删除父个体中对应的基因
                    pop_mu_2.pop(pop_mu_1.index(pop_1[0]))
                    pop_mu_1.pop(pop_mu_1.index(pop_1[0]))
                    pop_1.pop(0)
                    pop_2.pop(0)
                else:
                    pop_crssover_1.append(copy.deepcopy(pop_mu_1[0]))
                    pop_crssover_2.append(copy.deepcopy(pop_mu_2[0]))
                    # 删除父个体中对应的基因
                    pop_2.pop(pop_1.index(pop_mu_1[0]))
                    pop_1.pop(pop_1.index(pop_mu_1[0]))
                    pop_mu_1.pop(0)
                    pop_mu_2.pop(0)
            POP_crossover.append(copy.deepcopy(pop_crssover_1 + pop_crssover_2))
        else:
            POP_crossover.append(copy.deepcopy(pop_mu_1 + pop_mu_2))
    return POP_crossover


def crossover_bin(POP, POP_mutation, CROSSOVER_RATE, N):
    # 二项交叉
    POP_crossover = []
    for i in range(len(POP)):  # 对于每一个种群
        pop_crssover_1 = []
        pop_crssover_2 = []
        pop = POP[i]  # 父个体
        pop_mu = POP_mutation[i]  # 变异个体
        for n in range(N):
            if np.random.rand() <= CROSSOVER_RATE or n == np.random.randint(low=0,
                                                                            high=N):  # np.random.rand() 取值范围是[0,1)
                pop_crssover_1.append(copy.deepcopy(pop_mu[n]))
                pop_crssover_2.append(copy.deepcopy(pop_mu[n + N]))
            else:
                pop_crssover_1.append(copy.deepcopy(pop[n]))
                pop_crssover_2.append(copy.deepcopy(pop[n + N]))

        # 对非法进行修正
        # 对染色体的第一部分进行调整
        pop_mu_i_standerd = {}  # 字典 1:0, 2:0, ..., M:0
        for n in range(N):
            pop_mu_i_standerd[n + 1] = 0
        # 针对染色体的第一段（车辆编号）使合法
        # 车辆编号去重
        for n in range(N):  # 针对染色体的第一段
            pop_mu_i_standerd[pop_crssover_1[n]] += 1  # 计数，每一个车辆出现了几次
        cycle = True
        while cycle == True:
            for n_ilegal_1 in range(N):
                if pop_mu_i_standerd[n_ilegal_1 + 1] > 1:
                    break
            for n_ilegal_2 in range(N):
                if pop_mu_i_standerd[n_ilegal_2 + 1] < 1:
                    break
            if n_ilegal_1 == N - 1 and n_ilegal_2 == N - 1:  # 结束循环
                cycle = False
            else:
                # 此时n为车辆出现次数大于1的 车辆编码-1
                pos_1 = pop_crssover_1.index(n_ilegal_1 + 1)
                pop_crssover_1[pos_1] = n_ilegal_2 + 1
                pop_mu_i_standerd[n_ilegal_1 + 1] -= 1  # 车辆出现的次数-1
                pop_mu_i_standerd[n_ilegal_2 + 1] += 1  # 车辆出现的次数-1
                # 对染色体的第二部分进行调整
                pop_crssover_2[pos_1] = pop_mu[pop_mu.index(pop_crssover_1[pos_1]) + N]
        POP_crossover.append(copy.deepcopy(pop_crssover_1 + pop_crssover_2))
    return POP_crossover


def crossover_exp(POP, POP_mutation, CROSSOVER_RATE, N):
    # 指数交叉,定义起点l与长度L
    POP_crossover = []
    for i in range(len(POP)):  # 对于每一个种群
        pop = POP[i]  # 原个体
        pop_1 = pop[0: N]  # 原个体第一段
        pop_mu = POP_mutation[i]  # 变异个体
        pop_mu_1 = pop_mu[0: N]  # 变异个体第一段
        l = np.random.randint(low=0, high=N)  # 交叉的起点 0,...,N-1，1,...,l为原个体
        l_copy = copy.deepcopy(l)
        l2 = copy.deepcopy(l)  # 交叉的终点 l到l2之间为变异个体
        while l2 < N:
            if np.random.rand() <= CROSSOVER_RATE:  # np.random.rand() 取值范围是[0,1),取变异个体区间内
                l2 += 1
            else:
                break
        fragment1 = pop_1[l:l2]
        fragment2 = pop_mu_1[l:l2]
        del pop_1[l:l2]
        child = []
        for pos in pop_1:
            if pos in fragment2:
                pos = fragment1[fragment2.index(pos)]
                while pos in fragment2:
                    pos = fragment1[fragment2.index(pos)]
                child.append(pos)
                continue
            child.append(pos)
        for i in range(0, len(fragment2)):
            child.insert(l_copy, fragment2[i])
            l_copy += 1
        # 对于子代基因的第二部分
        for n in range(N):
            if l <= n < l2:
                child.append(pop_mu[n + N])
            else:
                child.append(pop[pop.index(child[n]) + N])
        POP_crossover.append(child)

    # def crossover_exp(POP, POP_mutation, CROSSOVER_RATE, N):
    #     # 指数交叉,定义起点l与长度L
    #     POP_crossover = []
    #     for i in range(len(POP)):  # 对于每一个种群
    #         pop_crssover_1 = []
    #         pop_crssover_2 = []
    #         pop = POP[i]  # 父个体
    #         pop_mu = POP_mutation[i]  # 变异个体
    #         l = np.random.randint(low=0, high=N)  # 交叉的起点 0,...,N-1，1,...,l为原个体
    # n = 0
    # while n < l:  # 取原个体
    #     pop_crssover_1.append(copy.deepcopy(pop[n]))
    #     pop_crssover_2.append(copy.deepcopy(pop[n+N]))
    #     n += 1
    # while n < N:
    #     if np.random.rand() <= CROSSOVER_RATE:  # np.random.rand() 取值范围是[0,1),取变异个体区间内
    #         pop_crssover_1.append(copy.deepcopy(pop_mu[n]))
    #         pop_crssover_2.append(copy.deepcopy(pop_mu[n+N]))
    #         n += 1
    #     else:
    #         break
    # # 取原个体
    # while n < N:
    #     pop_crssover_1.append(copy.deepcopy(pop[n]))
    #     pop_crssover_2.append(copy.deepcopy(pop[n+N]))
    #     n += 1
    #
    # # 对非法进行修正
    # # 对染色体的第一部分进行调整
    # pop_mu_i_standerd = {}  # 字典 1:0, 2:0, ..., M:0
    # for n in range(N):
    #     pop_mu_i_standerd[n + 1] = 0
    # # 针对染色体的第一段（车辆编号）使合法
    # # 车辆编号去重
    # for n in range(N):  # 针对染色体的第一段
    #     pop_mu_i_standerd[pop_crssover_1[n]] += 1  # 计数，每一个车辆出现了几次
    # cycle = True
    # while cycle == True:
    #     for n_ilegal_1 in range(N):
    #         if pop_mu_i_standerd[n_ilegal_1 + 1] > 1:
    #             break
    #     for n_ilegal_2 in range(N):
    #         if pop_mu_i_standerd[n_ilegal_2 + 1] < 1:
    #             break
    #     if n_ilegal_1 == N - 1 and n_ilegal_2 == N - 1:  # 结束循环
    #         cycle = False
    #     else:
    #         # 此时n为车辆出现次数大于1的 车辆编码-1
    #         pos_1 = pop_crssover_1.index(n_ilegal_1 + 1)
    #         pop_crssover_1[pos_1] = n_ilegal_2 + 1
    #         pop_mu_i_standerd[n_ilegal_1 + 1] -= 1  # 车辆出现的次数-1
    #         pop_mu_i_standerd[n_ilegal_2 + 1] += 1  # 车辆出现的次数-1
    #         # 对染色体的第二部分进行调整
    #         pop_crssover_2[pos_1] = pop_mu[pop_mu.index(pop_crssover_1[pos_1]) + N]
    # POP_crossover.append(copy.deepcopy(pop_crssover_1 + pop_crssover_2))
    return POP_crossover
