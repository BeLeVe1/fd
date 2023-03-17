import numpy
import numpy as np
import copy

from crossover_def import crossover_ppx, crossover_pox
from decoding_def import decoding
from fitness_def import fitness


# POP
# F 缩放因子
# N 工件数
# M 机器数
# Ma 每个车辆可以停靠的月台
# Fit_POP_new 适应度
def mutation_rand_pox(POP, POP_num, N, pm):
    CROSSOVER_RATE = 0.5
    # 对随机三个个体进行pox操作
    POP_mu = []  # 变异产生的贡献向量
    for _ in range(len(POP_num)):  # 共产生len(POP)个个体
        # 产生三个不同个体
        ran1 = np.random.randint(low=0, high=len(POP))
        pop1 = copy.deepcopy(POP[ran1])
        ran2 = np.random.randint(low=0, high=len(POP))
        while ran2 == ran1:  # ran2不可以等于ran1
            ran2 = np.random.randint(low=0, high=len(POP))
        ran3 = np.random.randint(low=0, high=len(POP))
        while ran3 == ran1 or ran3 == ran2:
            ran3 = np.random.randint(low=0, high=len(POP))
        pop2 = copy.deepcopy(POP[ran2])
        pop3 = copy.deepcopy(POP[ran3])
        if np.random.rand() < pm:
            pop1_2_list = crossover_pox([pop1], [pop2], N, 1)
            pop1_2 = pop1_2_list[0]
        else:
            pop1_2 = copy.deepcopy(pop1)
        if np.random.rand() < pm:
            pop1_2_3_list = crossover_pox([pop1_2], [pop3], N, 1)
            pop1_2_3 = pop1_2_3_list[0]
        else:
            pop1_2_3 = copy.deepcopy(pop1_2)
        POP_mu.append(copy.deepcopy(pop1_2_3))
    return POP_mu

def mutation_neh_best(pop_best, POP, N, M, P, D, A, B, Ma):
    # 1 对一个个体进行局部搜索NEH
    pop_best_copy_1 = []
    pop_best_copy_1 = pop_best_copy_1 + pop_best[0:N]
    pop_best_copy_2 = []
    pop_best_copy_2 = pop_best_copy_2 + pop_best[N:2 * N]
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
        # 适应度最小的基因
        pop_best_copy_1 = POP_insert[Fit_insert.index(max(Fit_insert))][0:int(len(POP_insert[0]) / 2)]
        pop_best_copy_2 = POP_insert[Fit_insert.index(max(Fit_insert))][
                          int(len(POP_insert[0]) / 2):len(POP_insert[0])]
    for i in range(len(POP)):
        POP_mu.append(pop_best_copy_1 + pop_best_copy_2)
    return POP_mu


def mutation_insert_best_rand(pop_best, POP, N, Ma, Manum):
    POP_mu = []  # 变异产生的贡献向量
    for _ in range(len(POP)):  # 共产生len(POP)个贡献向量,随机选择10个个体变异后个体中的一个
        # 1 对一个个体进行随机插入
        pop_best_copy_1 = copy.deepcopy(pop_best[0:N])
        pop_best_copy_2 = copy.deepcopy(pop_best[N:2 * N])
        h = np.random.randint(low=0, high=N)

        # 随意去除h个基因
        pop_best_h_1 = []  # 去除的h个基因
        # pop_best_h_2 = []
        # 随意去除h个基因
        for h_in in range(h):
            ran = np.random.randint(low=0, high=len(pop_best_copy_1))
            pop_best_h_1.append(copy.deepcopy(pop_best_copy_1[ran]))
            # pop_best_h_2.append(copy.deepcopy(pop_best_copy_2[ran]))
            del pop_best_copy_1[ran]
            del pop_best_copy_2[ran]
        # 重新随机插入
        for pop_insert_n in range(len(pop_best_h_1)):  # 对于每一个需要插入的任务
            ran_pos = np.random.randint(low=0, high=len(pop_best_copy_1) + 1)  # 所有可以插入的位置
            pop_best_copy_1.insert(ran_pos, pop_best_h_1[pop_insert_n])
            # pop_best_copy_2.insert(ran_pos, pop_best_h_2[pop_insert_n])
            pop_best_copy_2.insert(ran_pos, Ma[pop_best_h_1[pop_insert_n]-1][numpy.random.randint(low=0, high=Manum[pop_best_h_1[pop_insert_n]-1])])
        POP_mu.append(copy.deepcopy(pop_best_copy_1 + pop_best_copy_2))
    return POP_mu


def mutation_insert_rand_rand(POP_n, POP, N, Ma, Manum, pm):
    POP_mu = []  # 变异产生的贡献向量
    # 对随机个体进行随机插入
    for _ in range(len(POP_n)):
        pop_rand = POP[numpy.random.randint(low=0, high=len(POP))]
        if np.random.rand() < pm:
            pop_rand_copy_1 = copy.deepcopy(pop_rand[0:N])
            pop_rand_copy_2 = copy.deepcopy(pop_rand[N:2 * N])
            h = np.random.randint(low=0, high=N)
            # 随意去除h个基因
            pop_rand_h_1 = []  # 去除的h个基因
            # pop_rand_h_2 = []
            # 随意去除h个基因
            for h_in in range(h):
                ran = np.random.randint(low=0, high=len(pop_rand_copy_1))
                pop_rand_h_1.append(copy.deepcopy(pop_rand_copy_1[ran]))
                # pop_rand_h_2.append(copy.deepcopy(pop_rand_copy_2[ran]))
                del pop_rand_copy_1[ran]
                del pop_rand_copy_2[ran]
            # 重新随机插入
            for pop_insert_n in range(len(pop_rand_h_1)):  # 对于每一个需要插入的任务
                ran_pos = np.random.randint(low=0, high=len(pop_rand_copy_1) + 1)  # 所有可以插入的位置
                pop_rand_copy_1.insert(ran_pos, pop_rand_h_1[pop_insert_n])
                # pop_rand_copy_2.insert(ran_pos, pop_rand_h_2[pop_insert_n])
                pop_rand_copy_2.insert(ran_pos, Ma[pop_rand_h_1[pop_insert_n] - 1][
                    numpy.random.randint(low=0, high=Manum[pop_rand_h_1[pop_insert_n] - 1])])
            POP_mu.append(copy.deepcopy(pop_rand_copy_1 + pop_rand_copy_2))
        else:
            POP_mu.append(copy.deepcopy(pop_rand))
    return POP_mu


def mutation_swap_best(pop_best, POP, N):
    POP_mu = []  # 变异产生的贡献向量
    for i in range(len(POP)):  # 共产生len(POP)个贡献向量
        pop_best_copy_1 = []
        pop_best_copy_1 = pop_best_copy_1 + pop_best[0:N]
        pop_best_copy_2 = []
        pop_best_copy_2 = pop_best_copy_2 + pop_best[N:2 * N]
        # 做swap
        ran1 = np.random.randint(low=0, high=len(pop_best_copy_1))
        ran2 = np.random.randint(low=0, high=len(pop_best_copy_1))
        while ran2 == ran1:  # ran2不可以等于ran1
            ran2 = np.random.randint(low=0, high=len(pop_best_copy_1))
        pop_best_copy_1_reverse = pop_best_copy_1[ran1:ran2]
        pop_best_copy_1_reverse.reverse()
        pop_best_copy_2_reverse = pop_best_copy_2[ran1:ran2]
        pop_best_copy_2_reverse.reverse()
        pop_best_copy_1[ran1:ran2] = pop_best_copy_1_reverse
        pop_best_copy_2[ran1:ran2] = pop_best_copy_2_reverse
        POP_mu.append(copy.deepcopy(pop_best_copy_1 + pop_best_copy_2))
    return POP_mu


def mutation_swap_rand(POP, POP_mu_best, N, pm):
    POP_mu = []  # 变异产生的贡献向量
    pop_best_copy_1 = []
    pop_best_copy_2 = []
    for pop_num in range(len(POP)):
        pop = POP_mu_best[np.random.randint(low=0, high=len(POP_mu_best))]  # 随机选择一个pop
        if np.random.randn() < pm:
            pop_best_copy_1[:] = []
            pop_best_copy_1 = pop_best_copy_1 + pop[0:N]
            pop_best_copy_2[:] = []
            pop_best_copy_2 = pop_best_copy_2 + pop[N:2 * N]
            ran1 = np.random.randint(low=0, high=len(pop_best_copy_1))
            ran2 = np.random.randint(low=0, high=len(pop_best_copy_1))
            while ran2 == ran1:  # ran2不可以等于ran1
                ran2 = np.random.randint(low=0, high=len(pop_best_copy_1))
            pop_best_copy_1_reverse = pop_best_copy_1[ran1:ran2]
            pop_best_copy_1_reverse.reverse()
            pop_best_copy_2_reverse = pop_best_copy_2[ran1:ran2]
            pop_best_copy_2_reverse.reverse()
            pop_best_copy_1[ran1:ran2] = pop_best_copy_1_reverse
            pop_best_copy_2[ran1:ran2] = pop_best_copy_2_reverse
            POP_mu.append(copy.deepcopy(pop_best_copy_1 + pop_best_copy_2))
        else:
            POP_mu.append(copy.deepcopy(pop))
    return POP_mu


def mutation_2(POP, N, Fit_POP_new):
    # 有点效果，但是不是很好
    # 2 swap操作
    print('mu_2')
    POP_mu = []  # 变异产生的贡献向量
    for pop_i in range(len(POP)):  # 共产生len(POP)个贡献向量
        # 产生三个不同的随机个体
        ran1 = np.random.randint(low=0, high=len(POP))
        while ran1 == pop_i:  # ran1不可以等于i
            ran1 = np.random.randint(low=0, high=len(POP))
        ran2 = np.random.randint(low=0, high=len(POP))
        while ran2 == pop_i or ran2 == ran1:  # ran2不可以等于i、ran1
            ran2 = np.random.randint(low=0, high=len(POP))
        ran3 = np.random.randint(low=0, high=len(POP))
        while ran3 == pop_i or ran3 == ran1 or ran3 == ran2:  # ran3不可以等于i、ran1、ran2
            ran3 = np.random.randint(low=0, high=len(POP))
        ran1_fit = Fit_POP_new[ran1]
        ran2_fit = Fit_POP_new[ran2]
        ran3_fit = Fit_POP_new[ran3]
        # 令a为三个随机个体中的最优解
        if ran1_fit >= ran2_fit and ran1_fit >= ran3_fit:
            a = POP[ran1]
            b = POP[ran2]
            c = POP[ran3]
        if ran2_fit >= ran1_fit and ran2_fit >= ran3_fit:
            a = POP[ran2]
            b = POP[ran1]
            c = POP[ran3]
        if ran3_fit >= ran1_fit and ran3_fit >= ran2_fit:
            a = POP[ran3]
            b = POP[ran1]
            c = POP[ran2]
        b_c = []  # 变异产生的贡献向量
        for n in range(N):  # 对于个体的第一段每一个基因
            if b[n] != c[n]:
                b_c.append(copy.deepcopy(b[n]))
            else:
                b_c.append(0)
        for n in range(N):
            if b_c[n] != 0 and np.random.rand() <= 0.3:  # 考虑将b_c[n]与b_c[n]之间的基因swap
                swap_point1 = a.index(a[n])
                swap_point2 = a.index(b_c[n])
                if swap_point1 > swap_point2:
                    swap_point1, swap_point2 = swap_point2, swap_point1
                p1 = a[swap_point1:swap_point2]
                p1.reverse()
                a[swap_point1:swap_point2] = p1
                p2 = a[swap_point1 + N:swap_point2 + N]
                p2.reverse()
                a[swap_point1 + N:swap_point2 + N] = p2
            # 效果不好
            # elif b_c[n] != 0:  # 插入
            #     a_insert = copy.deepcopy(a[n])
            #     a_insert_2 = copy.deepcopy(a[n+N])
            #     b_c_insert = b_c[n]  # 在a中把a_insert插入到b_c_insert之后的位置
            #     if a_insert != b_c_insert:
            #         del a[n]
            #         del a[n + N - 1]
            #         a.insert(a.index(b_c_insert) + 1, a_insert)
            #         a.insert(a.index(b_c_insert) + 1 + N + 1, a_insert_2)
        POP_mu.append(copy.deepcopy(a))
    return POP_mu


def mutation_3(POP, N, M, Fit_POP_new, F):
    print('mu_3')
    # 没有效果
    POP_mu = []  # 变异产生的贡献向量
    for pop_i in range(len(POP)):  # 共产生len(POP)个贡献向量
        # 产生三个不同的随机个体
        ran1 = np.random.randint(low=0, high=len(POP))
        while ran1 == pop_i:  # ran1不可以等于i
            ran1 = np.random.randint(low=0, high=len(POP))
        ran2 = np.random.randint(low=0, high=len(POP))
        while ran2 == pop_i or ran2 == ran1:  # ran2不可以等于i、ran1
            ran2 = np.random.randint(low=0, high=len(POP))
        ran3 = np.random.randint(low=0, high=len(POP))
        while ran3 == pop_i or ran3 == ran1 or ran3 == ran2:  # ran3不可以等于i、ran1、ran2
            ran3 = np.random.randint(low=0, high=len(POP))
        ran1_fit = Fit_POP_new[ran1]
        ran2_fit = Fit_POP_new[ran2]
        ran3_fit = Fit_POP_new[ran3]
        # 令a为三个随机个体中的最优解
        if ran1_fit >= ran2_fit and ran1_fit >= ran3_fit:
            a = POP[ran1]
            b = POP[ran2]
            c = POP[ran3]
        if ran2_fit >= ran1_fit and ran2_fit >= ran3_fit:
            a = POP[ran2]
            b = POP[ran1]
            c = POP[ran3]
        if ran3_fit >= ran1_fit and ran3_fit >= ran2_fit:
            a = POP[ran3]
            b = POP[ran1]
            c = POP[ran2]
        # 对于第一段基因
        # 求b与c的差
        # 和a做加和
        pop_mu_i = []  # 变异产生的贡献向量
        for n in range(N):  # 对于个体的第一段每一个基因
            b_c = b[n] - c[n]
            # F 控制差分变异放大的突变尺度因子
            b_c_derta = 0
            if np.random.rand() <= F:
                b_c_derta = b_c
            pop_mu_i.append((a[n] + b_c_derta + N) % N + 1)
        # 对于第二段基因
        for n in range(N):  # 对于个体的第一段每一个基因
            b_c = b[n + N] - c[n + N]
            # F 控制差分变异放大的突变尺度因子
            b_c_derta = 0
            if np.random.rand() <= F:
                b_c_derta = b_c
            pop_mu_i.append((a[n + N] + b_c_derta + M) % M + 1)
        POP_mu.append(copy.deepcopy(pop_mu_i))
    return POP_mu


# 连续变异，不可取
def mutation_rand_1(POP, F, N, Ma):
    # rand/1变异操作
    POP_mu = []  # 变异产生的贡献向量
    for pop_i in range(len(POP)):  # 共产生len(POP)个贡献向量
        ran1 = np.random.randint(low=0, high=len(POP))
        while ran1 == pop_i:  # ran1不可以等于i
            ran1 = np.random.randint(low=0, high=len(POP))
        ran2 = np.random.randint(low=0, high=len(POP))
        while ran2 == pop_i or ran2 == ran1:  # ran2不可以等于i、ran1
            ran2 = np.random.randint(low=0, high=len(POP))
        ran3 = np.random.randint(low=0, high=len(POP))
        while ran3 == pop_i or ran3 == ran1 or ran3 == ran2:  # ran3不可以等于i、ran1、ran2
            ran3 = np.random.randint(low=0, high=len(POP))
        pop_mu_i = []  # 变异产生的贡献向量
        for n in range(2 * N):
            pop_mu_i_n = round(POP[ran1][n] + F * (POP[ran2][n] - POP[ran3][n]))  # 取整
            pop_mu_i.append(copy.deepcopy(pop_mu_i_n))
        # 对非法解pop_mu_i进行调整
        # 对染色体的第一部分进行调增
        pop_mu_i_standerd = {}  # 字典 1:0, 2:0, ..., M:0
        for n in range(N):
            pop_mu_i_standerd[n + 1] = 0
        # 针对染色体的第一段（车辆编号）使合法
        # 使车辆编号在1,...,N范围内
        for n in range(N):  # 针对染色体的第一段
            if not 1 <= pop_mu_i[n] <= N:
                pop_mu_i[n] = np.random.randint(low=1, high=N + 1)  # 左闭右开区间 1-N之间任意数
        # 车辆编号去重
        for n in range(N):  # 针对染色体的第一段
            pop_mu_i_standerd[pop_mu_i[n]] += 1  # 计数，每一个车辆出现了几次
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
                pos_1 = pop_mu_i.index(n_ilegal_1 + 1)
                pop_mu_i[pos_1] = n_ilegal_2 + 1
                pop_mu_i_standerd[n_ilegal_1 + 1] -= 1  # 车辆出现的次数-1
                pop_mu_i_standerd[n_ilegal_2 + 1] += 1  # 车辆出现的次数-1

        # 对染色体的第二部分进行调整
        for n in range(N):
            if pop_mu_i[n + N] not in Ma[pop_mu_i[n] - 1]:
                pop_mu_i[n + N] = Ma[pop_mu_i[n] - 1][np.random.randint(low=0, high=len(Ma[pop_mu_i[n] - 1]))]
        POP_mu.append(pop_mu_i)
    return POP_mu


# 离散变异策略，不可取
def mutation_best_1(POP, F, N, Ma, pop_best):
    # DE/best/1操作
    POP_mu = []  # 变异产生的贡献向量
    for pop_i in range(len(POP)):  # 共产生len(POP)个贡献向量
        ran1 = np.random.randint(low=0, high=len(POP))
        while ran1 == pop_i:  # ran1不可以等于i
            ran1 = np.random.randint(low=0, high=len(POP))
        ran2 = np.random.randint(low=0, high=len(POP))
        while ran2 == pop_i or ran2 == ran1:  # ran2不可以等于i、ran1
            ran2 = np.random.randint(low=0, high=len(POP))
        pop_mu_i = []  # 变异产生的贡献向量
        for n in range(2 * N):
            pop_mu_i_n = round(pop_best[n] + F * (POP[ran1][n] - POP[ran2][n]))  # 取整
            pop_mu_i.append(copy.deepcopy(pop_mu_i_n))
        # 对非法解pop_mu_i进行调整
        # 对染色体的第一部分进行调增
        pop_mu_i_standerd = {}  # 字典 1:0, 2:0, ..., M:0
        for n in range(N):
            pop_mu_i_standerd[n + 1] = 0
        # 针对染色体的第一段（车辆编号）使合法
        # 使车辆编号在1,...,N范围内
        for n in range(N):  # 针对染色体的第一段
            if not 1 <= pop_mu_i[n] <= N:
                pop_mu_i[n] = np.random.randint(low=1, high=N + 1)  # 左闭右开区间 1-N之间任意数
        # 车辆编号去重
        for n in range(N):  # 针对染色体的第一段
            pop_mu_i_standerd[pop_mu_i[n]] += 1  # 计数，每一个车辆出现了几次
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
                pos_1 = pop_mu_i.index(n_ilegal_1 + 1)
                pop_mu_i[pos_1] = n_ilegal_2 + 1
                pop_mu_i_standerd[n_ilegal_1 + 1] -= 1  # 车辆出现的次数-1
                pop_mu_i_standerd[n_ilegal_2 + 1] += 1  # 车辆出现的次数-1

        # 对染色体的第二部分进行调整
        for n in range(N):
            if pop_mu_i[n + N] not in Ma[pop_mu_i[n] - 1]:
                pop_mu_i[n + N] = Ma[pop_mu_i[n] - 1][np.random.randint(low=0, high=len(Ma[pop_mu_i[n] - 1]))]
        POP_mu.append(pop_mu_i)

    return POP_mu
