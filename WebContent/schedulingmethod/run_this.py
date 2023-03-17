def dss(Lbn, Lbm, A, B, D, P):
    import numpy as np
    import copy
    import matplotlib.pyplot as plt
    import pymysql
    import random

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
    # gen = 100  # 迭代次数
    # POP_SIZE = 50  # 种群数量
    # pm = 0.6
    # pc = 0.8
    # d = 45  # 滑动时间窗
    # ps_vnd = 0.2  # 变邻域下降参数
    # 20个月台
    gen = 100  # 迭代次数
    POP_SIZE = 50  # 种群数量
    pm = 0.6
    pc = 0.8
    d = 45  # 滑动时间窗
    ps_vnd = 0.2  # 变邻域下降参数
    Stime = []
    Etime = []
    for g_gen in range(1):
        print("算法开始运行",g_gen)
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
            POP_new, Fit_POP_new, ET_penalty_POP_new = select(POP, POP_crossover, Fit_POP, ET_penalty_POP,
                                                              Fit_crossover,
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

            # 对 个个体进行局部搜索
            Ps = ps_vnd * (g / 100) ** 2
            POP_VND_SIZE = int(POP_SIZE * Ps)  # 进行局部搜索的个体数量，随机选择个体进行局部搜索
            # print('POP_VND_SIZE', POP_VND_SIZE)
            # 找出最大的fitness
            # maxre_f = copy.deepcopy(max(Fit_POP_new))
            # h = copy.deepcopy(Fit_POP_new.index(maxre_f))
            # maxre_p = copy.deepcopy(POP_new[h])
            # minre_et = copy.deepcopy(ET_penalty_POP_new[h])
            # print('pls前', minre_et)
            # print(ET_penalty_POP_new)
            for vnd_i in range(POP_VND_SIZE):
                ran_vnd = np.random.randint(low=0, high=len(POP_new))
                pop_vnd = copy.deepcopy(POP_new[ran_vnd])
                et_pop_vnd = ET_penalty_POP_new[ran_vnd]
                # NE.II，NE.IS，NE.EI，NE.ES，NE.IGS和NE.SIGS 按照这个顺序探索
                stop_vnd = False
                k_vnd = 1
                while not stop_vnd:
                    if k_vnd == 1:
                        # print('k_vnd == 1')
                        pop_vnd_re, et_vnd_re = NEII(pop_vnd, N, M, P, D, A, B)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 2:
                        # print('k_vnd == 2')
                        pop_vnd_re, et_vnd_re = NEIS(pop_vnd, N, M, P, D, A, B)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 3:
                        # print('k_vnd == 3')
                        pop_vnd_re, et_vnd_re = NEEI(pop_vnd, N, M, P, D, A, B, Ma)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 4:
                        # print('k_vnd == 4')
                        pop_vnd_re, et_vnd_re = NEES(pop_vnd, N, M, P, D, A, B, Ma)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 5:
                        # print('k_vnd == 5')
                        rj = 5
                        pop_vnd_re, et_vnd_re = NEIGS(pop_vnd, et_pop_vnd, rj, N, M, P, D, A, B, Ma)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 6:
                        # print('k_vnd == 6')
                        rjs = 1
                        pop_vnd_re, et_vnd_re = NESIGS(pop_vnd, et_pop_vnd, rjs, N, M, P, D, A, B, Ma)
                        if et_vnd_re < ET_penalty_POP_new[ran_vnd]:  # 有改进
                            k_vnd = 1
                        else:  # 没有改进
                            k_vnd += 1
                        POP_new[ran_vnd] = copy.deepcopy(pop_vnd_re)
                        ET_penalty_POP_new[ran_vnd] = et_vnd_re
                        Fit_POP_new[ran_vnd] = et_getfit(et_vnd_re)
                        pop_vnd = copy.deepcopy(pop_vnd_re)
                        et_pop_vnd = et_vnd_re
                    if k_vnd == 7:
                        # print('stop')
                        stop_vnd = True
            maxre_f = copy.deepcopy(max(Fit_POP_new))
            h = copy.deepcopy(Fit_POP_new.index(maxre_f))
            maxre_p = copy.deepcopy(POP_new[h])
            minre_et = copy.deepcopy(ET_penalty_POP_new[h])
            # print('pls后', minre_et)
            if minre_et <= min(et_min):  # 记录当前最优解
                pop_best.append(maxre_p)
                et_min.append(minre_et)
                fit_max.append(maxre_f)
            else:
                pop_best.append(copy.deepcopy(pop_best[et_min.index(min(et_min))]))
                fit_max.append(copy.deepcopy(fit_max[et_min.index(min(et_min))]))
                et_min.append(copy.deepcopy(et_min[et_min.index(min(et_min))]))
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
        S, E, O = decoding([pop_best[h]], N, M, P, D, A, B)
        print('Stime', S[0])
        print('Etime', E[0])
        print('s,e', S[0], E[0])

        print('')
        #
        # 绘制迭代gen代最优个体fitness散点图
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
    print('跑完了')
    return S[0], E[0],pop_best[h]
