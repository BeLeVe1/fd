import copy
import random

import numpy as np

from decoding_def import decoding
from fitness_def import fitness, fitness_et


# 获取一个p染色体上的某个机器的job与job在pop上的所在位置
# pop
# ran_m_ne 机器编号
# N job数量
def get_job_pos(pop_ne, ran_m_ne, N):
    ran_m_ne_getjob = []  # 该机器上的所有作业
    ran_m_ne_job_getpos = []  # 该机器上的所有作业在染色体上的位置
    for job_ne_n in range(N):
        if pop_ne[job_ne_n + N] == ran_m_ne:
            ran_m_ne_getjob.append(pop_ne[job_ne_n])
            ran_m_ne_job_getpos.append(job_ne_n)
    return ran_m_ne_getjob, ran_m_ne_job_getpos


# 计算每一个机器的延迟成本
def get_m_et_all(M, N, P, D, A, B, pop_ne):
    ET_ne_m_all_list = []
    for m_ne in range(1, M + 1):  # m_neii = 1, 2, M
        ran_m_ne_job, ran_m_ne_job_pos = get_job_pos(pop_ne, m_ne, N)
        # 得到机器上的job组合
        # 得到他的pop
        pop_ne_choose_m = ran_m_ne_job + [m_ne for _ in range(len(ran_m_ne_job))]
        # 解码
        # S 车辆任务开始作业的时间
        # E 车辆任务结束作业的时间
        # O 月台占用的时间
        S, E, O = decoding([pop_ne_choose_m], N, M, P, D, A, B)
        et_ne_m = fitness_et(A, B, S, E, D)
        ET_ne_m_all_list.append(copy.deepcopy(et_ne_m[0]))
    return ET_ne_m_all_list


# 选择具有延迟成本的机器
def NE_choosem(pop_ne, N, M, P, D, A, B):
    # 计算每一个机器的et
    ET_ne_m_all = get_m_et_all(M, N, P, D, A, B, pop_ne)
    # 随意选择一个具有延迟成本的机器ran_m_ne
    status = True
    M_list = [m_+1 for m_ in range(M)]
    ran_m_ne = 0
    while status:
        if len(M_list) > 0:
            ran_m_ne = random.choice(M_list)  # 选择的进行插入的机器
            M_list.remove(ran_m_ne)
            if ET_ne_m_all[ran_m_ne - 1] != 0:
                status = False
        else:
            M_list = [m_ + 1 for m_ in range(M)]
            ran_m_ne = random.choice(M_list)  # 随机选择一个
            status = False
    ran_m_ne_job, ran_m_ne_job_pos = get_job_pos(pop_ne, ran_m_ne, N)
    et_ne = copy.deepcopy(ET_ne_m_all[ran_m_ne - 1])
    # print(ran_m_ne)
    # print(ET_ne_m_all)
    return ran_m_ne, ran_m_ne_job, ran_m_ne_job_pos, et_ne


# 由机器1（机器2）的部分pop，重新插回，得到完整的pop
# m_job_pos 插回的位置
# pop_ini_total 最初的pop
# pop_frg 机器1机器2的pop
def get_total_pop(m_job_pos, pop_ini_total, pop_frg, N):
    pos_total = copy.deepcopy(m_job_pos)
    pos_total.sort()
    pop_get_total_return = copy.deepcopy(pop_ini_total)
    for pos_i in range(len(pos_total)):  # 对于每一个位置，按顺序插回
        pop_get_total_return[pos_total[pos_i]] = pop_frg[pos_i]
        pop_get_total_return[pos_total[pos_i] + N] = pop_frg[pos_i + int(len(pop_frg) / 2)]
    return pop_get_total_return


# ok
# 内部插入 BI最佳改进策略：分析邻域结构所有可能的解，返回最佳的
def NEII(pop_neii, N, M, P, D, A, B):
    # ran_m_neii选择的具有惩罚的机器
    # ran_m_neii_job该机器上的所有作业
    # ran_m_neii_job_pos该机器上的所有job在pop上的位置
    # ran_m_neii_et该机器的et
    ran_m_neii, ran_m_neii_job, ran_m_neii_job_pos, ran_m_neii_et = NE_choosem(pop_neii, N, M, P, D, A, B)
    # pop_ran_m_neii = ran_m_neii_job + [ran_m_neii for _ in range(len(ran_m_neii_job))]  # 只包含该机器的作业的pop
    POP_ran_m_neii_list = [
        copy.deepcopy(ran_m_neii_job + [ran_m_neii for _ in range(len(ran_m_neii_job))])]  # 插入产生的所有个体的集合
    for job_neii_insert_n in range(len(ran_m_neii_job)):  # 对于该机器上的第job_neii_insert_n个个体，对于每一个job
        ran_m_neii_job_copy = copy.deepcopy(ran_m_neii_job)
        del ran_m_neii_job_copy[job_neii_insert_n]  # 删除进行插入的job
        # 删除的job的位置pos job_neii_insert_n
        # 插入的job是 ran_m_neii_job[job_neii_insert_n]
        for pos_insert in range(len(ran_m_neii_job)):  # 对于每一个可以插入的位置
            pop_insert_ = ran_m_neii_job_copy[:pos_insert] + [ran_m_neii_job[job_neii_insert_n]] + ran_m_neii_job_copy[
                                                                                                   pos_insert:] + [
                              ran_m_neii for _ in range(len(ran_m_neii_job))]
            if pop_insert_ not in POP_ran_m_neii_list:
                POP_ran_m_neii_list.append(pop_insert_)
    S, E, O = decoding(POP_ran_m_neii_list, N, M, P, D, A, B)
    ET_ran_m_neii_list = fitness_et(A, B, S, E, D)  # 计算产生得所有得个体得et
    pop_neii_return_frg = POP_ran_m_neii_list[ET_ran_m_neii_list.index(min(ET_ran_m_neii_list))]
    # 返回的pop
    pop_neii_return = get_total_pop(ran_m_neii_job_pos, pop_neii, pop_neii_return_frg, N)
    S, E, O = decoding([pop_neii_return], N, M, P, D, A, B)
    et_neii_return_l = fitness_et(A, B, S, E, D)
    return pop_neii_return, et_neii_return_l[0]


# ok
# NEIS内部交换 FI首次改进：随机顺序进行分析，返回第一个导致改进的
def NEIS(pop_neis, N, M, P, D, A, B):
    # ran_m_ne选择的具有惩罚的机器
    # ran_m_ne_job该机器上的所有作业
    # ran_m_ne_job_pos该机器上的所有job在pop上的位置
    # ran_m_ne_et该机器的et
    ran_m_neis, ran_m_neis_job, ran_m_neis_job_pos, ran_m_neis_et = NE_choosem(pop_neis, N, M, P, D, A, B)
    status = True
    pop_neis_return_frg = []  # 该机器上的所有job的pop
    pop_neis_m_initial = copy.deepcopy(
        ran_m_neis_job + [ran_m_neis for _ in range(len(ran_m_neis_job))])  # 现在的机器上的所有job的pop个体
    if len(ran_m_neis_job) < 2:  # 该机器的job只有1，没有改进的空间
        pop_neis_return_frg = pop_neis_m_initial
    else:  # 该机器的job有2个以上，可能存在改进空间
        # 可能产生的所有的位置交换的list
        swap_neis_pro_list = []
        for swap_pos_1 in range(len(ran_m_neis_job)):
            for swap_pos_2 in range(len(ran_m_neis_job)):
                if swap_pos_2 > swap_pos_1:
                    swap_neis_pro_list.append(copy.deepcopy([swap_pos_1, swap_pos_2]))
        while status:  # 首次改进策略，改进了status变为Flase跳出循环
            # 机器中的两个位置的job进行交换
            job_swap_pos_list = swap_neis_pro_list[np.random.randint(low=0, high=len(swap_neis_pro_list))]
            swap_neis_pro_list.remove(job_swap_pos_list)
            job_swap_pos_1 = job_swap_pos_list[0]  # 第几个job进行swap
            job_swap_pos_2 = job_swap_pos_list[1]
            pop_neis_swap = copy.deepcopy(pop_neis_m_initial)  # swap之后的pop
            # 进行swap
            pop_neis_swap[job_swap_pos_1], pop_neis_swap[job_swap_pos_2] = pop_neis_swap[job_swap_pos_2], pop_neis_swap[
                job_swap_pos_1]
            # 计算进行完swap的个体的et
            S, E, O = decoding([pop_neis_swap], N, M, P, D, A, B)
            ET_pop_neis_swap = fitness_et(A, B, S, E, D)
            if ET_pop_neis_swap[0] < ran_m_neis_et:  # 进行swap之后的个体比之前的更好
                # print(ET_pop_neis_swap[0])
                # print(ran_m_neis_et)
                status = False
                # print('有改进')
                pop_neis_return_frg = copy.deepcopy(pop_neis_swap)
            else:  # 进行swap之后的个体没有原始解好
                if len(swap_neis_pro_list) == 0:  # 已经探索完所有的组合了
                    # print('无改进')
                    status = False
                    pop_neis_return_frg = pop_neis_m_initial  # 返回原来的解
                # 否则继续探索
    # 返回的pop
    pop_neis_return = get_total_pop(ran_m_neis_job_pos, pop_neis, pop_neis_return_frg, N)
    S, E, O = decoding([pop_neis_return], N, M, P, D, A, B)
    et_neis_return_l = fitness_et(A, B, S, E, D)
    return pop_neis_return, et_neis_return_l[0]


# ok
# NEEI 外部插入 BI 最佳改进
def NEEI(pop_neei, N, M, P, D, A, B, Ma):
    ET_neei_m_all = get_m_et_all(M, N, P, D, A, B, pop_neei)  # 所有机器的et的list
    # 选择一台有延迟的机器
    # ran_m_neii选择的具有惩罚的机器
    # ran_m_neii_job该机器上的所有作业
    # ran_m_neii_job_pos该机器上的所有job在pop上的位置
    # ran_m_neii_et该机器的et
    ran_m_neei_1, ran_m_neei_job_1, ran_m_neei_job_pos_1, ran_m_neei_et_1 = NE_choosem(pop_neei, N, M, P, D, A, B)
    # 除选择的第一台机器之外的其他机器列表
    L_neei = [m_neei+1 for m_neei in range(M)]
    L_neei.remove(ran_m_neei_1)
    # 随意选择一个不同的机器
    ran_m_neei_2 = L_neei[np.random.randint(low=0, high=len(L_neei))]
    L_neei.remove(ran_m_neei_2)
    # 机器2上的所有作业
    # 机器2上的所有作业在染色体上的位置
    ran_m_neei_job_2, ran_m_neei_job_pos_2 = get_job_pos(pop_neei, ran_m_neei_2, N)
    pop_neei_return_frg = []  # 产生的最优的机器1、2的pop
    improvement = False
    # 最佳改进
    while not improvement:  # 没有改进
        # 从机器1中选择job insert到机器2中
        pop_insert_list = []  # insert产生的pop个体种群
        for job_from_m1_pos in range(len(ran_m_neei_job_1)):  # 对于机器1上的每一个作业，插入到机器2上
            # 判断该作业能否被插入到机器2上去
            if ran_m_neei_2 in Ma[ran_m_neei_job_1[job_from_m1_pos] - 1]:  # 能在机器2上加工，则将pop加入到list当中去
                # 从第一个机器上选择的job是 ran_m_neei_job_1[job_from_m1_pos]
                # 机器1上的所有job
                job_insert_neei_1 = copy.deepcopy(ran_m_neei_job_1)
                del job_insert_neei_1[job_from_m1_pos]  # 删除机器1上的要插入的job
                # 机器1的pop机器段
                machine_insert_neei_1 = [ran_m_neei_1 for _ in range(len(ran_m_neei_job_1) - 1)]
                # 机器2上的所有job
                job_insert_neei_2 = copy.deepcopy(ran_m_neei_job_2)
                # 对于机器2上的每一个位置进行插入
                for pos_m2_neei in range(len(job_insert_neei_2) + 1):
                    job_insert_neei_2_copy = copy.deepcopy(job_insert_neei_2)
                    # 机器2的pop的机器段
                    machine_neei_2_copy = [ran_m_neei_2 for _ in range(len(ran_m_neei_job_2))]
                    # 将job插入机器2
                    job_insert_neei_2_copy.insert(pos_m2_neei, ran_m_neei_job_1[job_from_m1_pos])
                    machine_neei_2_copy.insert(pos_m2_neei, ran_m_neei_1)
                    pop_insert_list.append(copy.deepcopy(
                        job_insert_neei_1 + job_insert_neei_2_copy + machine_insert_neei_1 + machine_neei_2_copy))
        if len(pop_insert_list) != 0:
            # 完成了机器1上的每一个job对机器2上的插入
            S, E, O = decoding(pop_insert_list, N, M, P, D, A, B)
            # 这两个机器组成的pop的et值
            ET_pop_neei = fitness_et(A, B, S, E, D)
            et_neei_min = min(ET_pop_neei)  # 插入产生的pop的list中最优的
            et_neei_ini = ET_neei_m_all[ran_m_neei_1 - 1] + ET_neei_m_all[ran_m_neei_2 - 1]
            if et_neei_min < et_neei_ini:  # 得到更优的值
                pop_neei_return_frg = copy.deepcopy(pop_insert_list[ET_pop_neei.index(et_neei_min)])
                improvement = True
            else:  # 没有改进
                if len(L_neei) != 0:  # 如果还有可以选择的机器则选择另一个机器2
                    # 随意选择一个不同的机器
                    ran_m_neei_2 = L_neei[np.random.randint(low=0, high=len(L_neei))]
                    L_neei.remove(ran_m_neei_2)
                    # 机器2上的所有作业
                    # 机器2上的所有作业在染色体上的位置
                    ran_m_neei_job_2, ran_m_neei_job_pos_2 = get_job_pos(pop_neei, ran_m_neei_2, N)
                else:  # 没有改进
                    improvement = True
                    pop_neei_return_frg = copy.deepcopy(
                        ran_m_neei_job_1 + ran_m_neei_job_2 + [ran_m_neei_1 for _ in range(len(ran_m_neei_job_1))] + [
                            ran_m_neei_2 for _ in range(len(ran_m_neei_job_2))])
        else:  # 选择另一个机器
            if len(L_neei) != 0:  # 如果还有可以选择的机器则选择另一个机器2
                # 随意选择一个不同的机器
                ran_m_neei_2 = L_neei[np.random.randint(low=0, high=len(L_neei))]
                L_neei.remove(ran_m_neei_2)
                # 机器2上的所有作业
                # 机器2上的所有作业在染色体上的位置
                ran_m_neei_job_2, ran_m_neei_job_pos_2 = get_job_pos(pop_neei, ran_m_neei_2, N)
            else:  # 没有改进
                improvement = True
                pop_neei_return_frg = copy.deepcopy(
                    ran_m_neei_job_1 + ran_m_neei_job_2 + [ran_m_neei_1 for _ in range(len(ran_m_neei_job_1))] + [
                        ran_m_neei_2 for _ in range(len(ran_m_neei_job_2))])

    # 得到完整的pop返回
    pop_neei_return = get_total_pop(ran_m_neei_job_pos_1 + ran_m_neei_job_pos_2, pop_neei, pop_neei_return_frg, N)
    S, E, O = decoding([pop_neei_return], N, M, P, D, A, B)
    et_neei_return_l = fitness_et(A, B, S, E, D)
    if len(pop_neei_return) == 0:
        print('NEEIyouwenti')
    return pop_neei_return, et_neei_return_l[0]


# ok
# NEES 外部交叉 FI 首次改进
def NEES(pop_nees, N, M, P, D, A, B, Ma):
    ET_nees_m_all = get_m_et_all(M, N, P, D, A, B, pop_nees)  # 所有机器的et的list
    # 选择一台有延迟的机器
    # ran_m_neii选择的具有惩罚的机器
    # ran_m_neii_job该机器上的所有作业
    # ran_m_neii_job_pos该机器上的所有job在pop上的位置
    # ran_m_neii_et该机器的et
    ran_m_nees_1, ran_m_nees_job_1, ran_m_nees_job_pos_1, ran_m_nees_et_1 = NE_choosem(pop_nees, N, M, P, D, A, B)
    # 除选择的第一台机器之外的其他机器
    L_nees = [m_nees for m_nees in range(1, M + 1, 1)]  # 可以选择的机器列表
    L_nees.remove(ran_m_nees_1)
    # 随意选择一个不同的机器
    ran_m_nees_2 = L_nees[np.random.randint(low=0, high=len(L_nees))]
    L_nees.remove(ran_m_nees_2)
    # 机器2上的所有作业
    # 机器2上的所有作业在染色体上的位置
    ran_m_nees_job_2, ran_m_nees_job_pos_2 = get_job_pos(pop_nees, ran_m_nees_2, N)
    # 计算机器1机器2的et
    et_nees_ini = ET_nees_m_all[ran_m_nees_1 - 1] + ET_nees_m_all[ran_m_nees_2 - 1]
    pop_nees_swap = []  # 交叉之后两个机器的pop
    improvement = False
    # 所有可能产生交换的list
    sawp_nees_pro_list = []
    for pos_nees_1 in range(len(ran_m_nees_job_1)):
        if ran_m_nees_2 in Ma[ran_m_nees_job_1[pos_nees_1] - 1]:  # 机器1上的该job能在机器2上加工
            for pos_nees_2 in range(len(ran_m_nees_job_2)):
                if ran_m_nees_1 in Ma[ran_m_nees_job_2[pos_nees_2] - 1]:  # 机器2上的该job能在机器1上加工
                    sawp_nees_pro_list.append(copy.deepcopy([pos_nees_1, pos_nees_2]))
    while not improvement:  # 采用 FI 首次改进，improvement为true表示有改进或者已经遍历了所有的可能
        if len(sawp_nees_pro_list) == 0:  # 机器1与机器2之间没有可以交换的作业，考虑换一个机器2
            # print('jiqiliebioa', L_nees)
            if len(L_nees) == 0:  # 所有机器已经完成验证，没有更优的解
                # print('没有改进')
                improvement = True  # 没有可以改进的解，返回原解
                pop_nees_swap = copy.deepcopy(
                    ran_m_nees_job_1 + ran_m_nees_job_2 + [ran_m_nees_1 for _ in range(len(ran_m_nees_job_1))] + [
                        ran_m_nees_2 for _ in range(len(ran_m_nees_job_2))])
            else:  # 选择其他机器，继续swap
                # 随意选择一个不同的机器
                ran_m_nees_2 = L_nees[np.random.randint(low=0, high=len(L_nees))]
                L_nees.remove(ran_m_nees_2)
                # 机器2上的所有作业
                # 机器2上的所有作业在染色体上的位置
                ran_m_nees_job_2, ran_m_nees_job_pos_2 = get_job_pos(pop_nees, ran_m_nees_2, N)
                # 计算机器1机器2的et
                et_nees_ini = ET_nees_m_all[ran_m_nees_1 - 1] + ET_nees_m_all[ran_m_nees_2 - 1]
                # 所有可能产生交换的list
                sawp_nees_pro_list[:] = []
                for pos_nees_1 in range(len(ran_m_nees_job_1)):
                    if ran_m_nees_2 in Ma[ran_m_nees_job_1[pos_nees_1] - 1]:  # 机器1上的该job能在机器2上加工
                        for pos_nees_2 in range(len(ran_m_nees_job_2)):
                            if ran_m_nees_1 in Ma[ran_m_nees_job_2[pos_nees_2] - 1]:  # 机器2上的该job能在机器1上加工
                                sawp_nees_pro_list.append(copy.deepcopy([pos_nees_1, pos_nees_2]))
        else:  # 机器1与机器2之间有可以交换的作业
            # job_nees_from1_pos 第1个机器上的job在该机器上所有作业列表中的位置
            # job_nees_from2_pos 第2个机器上的job在该机器上所有作业列表中的位置
            job_nees_pos_list = sawp_nees_pro_list[np.random.randint(low=0, high=len(sawp_nees_pro_list))]
            sawp_nees_pro_list.remove(job_nees_pos_list)
            job_nees_from1_pos = job_nees_pos_list[0]
            job_nees_from2_pos = job_nees_pos_list[1]
            # 两个job可以swap
            # 交换job之前的pop
            pop_nees_swap = ran_m_nees_job_1 + ran_m_nees_job_2 + [ran_m_nees_1 for _ in
                                                                   range(len(ran_m_nees_job_1))] + [ran_m_nees_2 for _
                                                                                                    in range(
                    len(ran_m_nees_job_2))]
            # 交换job之后的pop
            pop_nees_swap[job_nees_from1_pos], pop_nees_swap[len(ran_m_nees_job_1) + job_nees_from2_pos] = \
                pop_nees_swap[len(ran_m_nees_job_1) + job_nees_from2_pos], pop_nees_swap[job_nees_from1_pos]
            # 计算交换job之后的et
            S, E, O = decoding([pop_nees_swap], N, M, P, D, A, B)
            et_nees_swap_l = fitness_et(A, B, S, E, D)
            et_nees_swap = et_nees_swap_l[0]
            if et_nees_swap < et_nees_ini:  # 交换之后的et与交换之前的进行比较
                improvement = True  # 有改进
                # print('et_nees_swap', et_nees_swap)
                # print('et_nees_ini', et_nees_ini)
            else:  # 没有改进
                if len(sawp_nees_pro_list) == 0:  # 已经完成这两个机器的所有组合的验证，没有更优的
                    # print('jiqiliebioa', L_nees)
                    if len(L_nees) == 0:  # 所有机器已经完成验证，没有更优的解
                        # print('没有改进')
                        improvement = True  # 没有可以改进的解，返回原解
                        pop_nees_swap = copy.deepcopy(ran_m_nees_job_1 + ran_m_nees_job_2 + [ran_m_nees_1 for _ in
                                                                                             range(len(
                                                                                                 ran_m_nees_job_1))] + [
                                                          ran_m_nees_2 for _ in range(len(ran_m_nees_job_2))])
                    else:  # 选择其他机器，继续swap
                        # 随意选择一个不同的机器
                        ran_m_nees_2 = L_nees[np.random.randint(low=0, high=len(L_nees))]
                        L_nees.remove(ran_m_nees_2)
                        # 机器2上的所有作业
                        # 机器2上的所有作业在染色体上的位置
                        ran_m_nees_job_2, ran_m_nees_job_pos_2 = get_job_pos(pop_nees, ran_m_nees_2, N)
                        # 计算机器1机器2的et
                        et_nees_ini = ET_nees_m_all[ran_m_nees_1 - 1] + ET_nees_m_all[ran_m_nees_2 - 1]

                        # 所有可能产生交换的list
                        sawp_nees_pro_list[:] = []
                        for pos_nees_1 in range(len(ran_m_nees_job_1)):
                            if ran_m_nees_2 in Ma[ran_m_nees_job_1[pos_nees_1] - 1]:  # 机器1上的该job能在机器2上加工
                                for pos_nees_2 in range(len(ran_m_nees_job_2)):
                                    if ran_m_nees_1 in Ma[ran_m_nees_job_2[pos_nees_2] - 1]:  # 机器2上的该job能在机器1上加工
                                        sawp_nees_pro_list.append(copy.deepcopy([pos_nees_1, pos_nees_2]))
    # 得到完整的pop返回
    pop_nees_return = get_total_pop(ran_m_nees_job_pos_1 + ran_m_nees_job_pos_2, pop_nees, pop_nees_swap, N)
    S, E, O = decoding([pop_nees_return], N, M, P, D, A, B)
    et_nees_return_l = fitness_et(A, B, S, E, D)
    return pop_nees_return, et_nees_return_l[0]


#
# NEIGS迭代贪婪搜索邻域 删除rj个作业 按照移动顺序插入回
def NEIGS(pop_neigs, pop_neigs_et, rj, N, M, P, D, A, B, Ma):
    ET_penalty_insert_min = 0
    # dc方法
    pop_neigs_copy_1 = copy.deepcopy(pop_neigs[0:N])
    pop_neigs_copy_2 = copy.deepcopy(pop_neigs[N:2 * N])
    # 随意去除rj个基因
    pop_neigs_rj_1 = []  # 去除的rj个基因
    pop_neigs_rj_2 = []
    for _ in range(rj):
        ran_neigs_pos = np.random.randint(low=0, high=len(pop_neigs_copy_1))
        pop_neigs_rj_1.append(copy.deepcopy(pop_neigs_copy_1[ran_neigs_pos]))
        pop_neigs_rj_2.append(copy.deepcopy(pop_neigs_copy_2[ran_neigs_pos]))
        del pop_neigs_copy_1[ran_neigs_pos]
        del pop_neigs_copy_2[ran_neigs_pos]
    # 重新按照顺序插入
    for pop_neigs_insert_n in range(len(pop_neigs_rj_1)):  # 对于每一个需要插入的任务
        POP_neigs_insert = []  # 对于这个插入的任务所产生的所有基因
        for pos in range(1 + len(pop_neigs_copy_1)):  # 把基因插入到每一个位置上
            for ma in Ma[pop_neigs_rj_1[pop_neigs_insert_n] - 1]:
                POP_neigs_insert.append(
                    copy.deepcopy(pop_neigs_copy_1[:pos] + [pop_neigs_rj_1[pop_neigs_insert_n]] + pop_neigs_copy_1[pos:]
                                  + pop_neigs_copy_2[:pos] + [ma] + pop_neigs_copy_2[pos:]))
        # 选出这个任务插入的最佳位置
        # 解码
        S, E, O = decoding(POP_neigs_insert, N, M, P, D, A, B)
        # 适应度
        Fit_insert, ET_penalty_insert = fitness(A, B, S, E, D)
        ET_penalty_insert_min = min(ET_penalty_insert)
        # 适应度最小的基因
        pop_neigs_copy_1 = POP_neigs_insert[Fit_insert.index(max(Fit_insert))][0:int(len(POP_neigs_insert[0]) / 2)]
        pop_neigs_copy_2 = POP_neigs_insert[Fit_insert.index(max(Fit_insert))][
                           int(len(POP_neigs_insert[0]) / 2):len(POP_neigs_insert[0])]
    if pop_neigs_et >= ET_penalty_insert_min:
        pop_dc = copy.deepcopy(pop_neigs_copy_1 + pop_neigs_copy_2)
        return pop_dc, ET_penalty_insert_min
    else:
        pop_dc = copy.deepcopy(pop_neigs)
        return pop_dc, pop_neigs_et


#
# NESIGS 交换迭代贪婪搜索邻域 随机选择rjs个作业，考虑所有可能的交换移动（内部交换、外部交换）
def NESIGS(pop_nesigs, pop_nesigs_et, rjs, N, M, P, D, A, B, Ma):
    ET_nesigs_m_all = get_m_et_all(M, N, P, D, A, B, pop_nesigs)  # 所有机器的et的list
    pop_nesigs_copy_1 = copy.deepcopy(pop_nesigs[0:N])
    pop_nesigs_copy_2 = copy.deepcopy(pop_nesigs[N:2 * N])
    # 随意选择rjs个基因
    pop_nesigs_rjs_1 = []  # 选择的rjs个基因
    pop_nesigs_rjs_2 = []
    rjs_pos_list = []  # 存储进行swap的pos
    for _ in range(rjs):
        pop_nesigs_pos = np.random.randint(low=0, high=len(pop_nesigs_copy_1))
        while pop_nesigs_pos in rjs_pos_list:
            pop_nesigs_pos = np.random.randint(low=0, high=len(pop_nesigs_copy_1))
        rjs_pos_list.append(pop_nesigs_pos)
        pop_nesigs_rjs_1.append(copy.deepcopy(pop_nesigs_copy_1[pop_nesigs_pos]))
        pop_nesigs_rjs_2.append(copy.deepcopy(pop_nesigs_copy_2[pop_nesigs_pos]))
    pop_NEIS_NEES_swap_list_forallrjs = []
    et_NEIS_NEES_swap_list_forallrjs = []
    pop_nesigs_NEIS_swap_return = []
    for pop_neigs_swap_n in range(len(pop_nesigs_rjs_1)):  # 对于每一个需要swap的任务
        # pop_nesigs_rjs_1[pop_neigs_swap_n] 需要进行swap的job
        # 该job所在机器
        job_nesigs_inm = pop_nesigs_rjs_2[pop_neigs_swap_n]

        # 内部swap
        # 获得该机器的所有job以及所在pos
        m_nesigs_job, m_nesigs_job_pos = get_job_pos(pop_nesigs, job_nesigs_inm, N)
        # 可能产生的所有的位置交换的list
        swap_nesigs_NEIS_list = []
        # 对于list中每一个进行交换之后的et
        et_swap_nesigs_NEIS_list = []
        # job0在m_nesigs_job中所在的位置
        pop_neigs_swap_n_pos = m_nesigs_job.index(pop_nesigs_rjs_1[pop_neigs_swap_n])
        for swap_job_pos in range(len(m_nesigs_job)):  # 对于该机器的所有的job，进行swap操作
            if pop_neigs_swap_n_pos != swap_job_pos:
                swap_nesigs_NEIS_list.append(copy.deepcopy([pop_neigs_swap_n_pos, swap_job_pos]))
        # 这个机器上的所有job的pop # 进行swap之前的这个机器的pop
        pop_nesigs_m_initial = copy.deepcopy(m_nesigs_job + [job_nesigs_inm for _ in range(len(m_nesigs_job))])
        for job_swap_pos_list in swap_nesigs_NEIS_list:  # 对于每一对可以进行交换的job
            # 机器中的两个位置的job进行交换
            job_swap_pos_1 = job_swap_pos_list[0]  # 第几个job进行swap
            job_swap_pos_2 = job_swap_pos_list[1]
            pop_nesigs_swap = copy.deepcopy(pop_nesigs_m_initial)  # swap之后的pop
            # 进行swap
            pop_nesigs_swap[job_swap_pos_1], pop_nesigs_swap[job_swap_pos_2] = pop_nesigs_swap[job_swap_pos_2], \
                                                                               pop_nesigs_swap[
                                                                                   job_swap_pos_1]
            # 计算进行完swap的个体的et
            S, E, O = decoding([pop_nesigs_swap], N, M, P, D, A, B)
            ET_pop_nesigs_swap = fitness_et(A, B, S, E, D)
            et_swap_nesigs_NEIS_list.append(ET_pop_nesigs_swap[0])
        # 内部swap中最优的swap的位置list
        if len(et_swap_nesigs_NEIS_list) != 0:
            et_swap_nesigs_NEIS = min(et_swap_nesigs_NEIS_list)
            swap_nesigs_best = copy.deepcopy(swap_nesigs_NEIS_list[et_swap_nesigs_NEIS_list.index(et_swap_nesigs_NEIS)])
            pop_nesigs_NEIS_best = copy.deepcopy(pop_nesigs_m_initial)  # 内部交换的最优个体
            pop_nesigs_NEIS_best[swap_nesigs_best[0]], pop_nesigs_NEIS_best[swap_nesigs_best[1]] = pop_nesigs_NEIS_best[
                                                                                                       swap_nesigs_best[
                                                                                                           1]], \
                                                                                                   pop_nesigs_NEIS_best[
                                                                                                       swap_nesigs_best[
                                                                                                           0]]
            # 内部swap的最优的pop
            pop_nesigs_NEIS_swap_return = get_total_pop(m_nesigs_job_pos, pop_nesigs, pop_nesigs_NEIS_best, N)

        # 外部swap
        # 除了这个作业所在机器之外的所有机器的list
        L_nesigs_NEES = [m_nees for m_nees in range(1, M + 1, 1)]  # 可以选择的机器列表
        L_nesigs_NEES.remove(job_nesigs_inm)
        # 每一个机器swap最优的的pop的list
        pop_swap_nesigs_NEES_m_list = []
        for m_nesigs_NEES in L_nesigs_NEES:  # 对于这个job所在机器之外的所有机器
            # 该job是否可以在该机器上加工
            if m_nesigs_NEES in Ma[pop_nesigs_rjs_1[pop_neigs_swap_n] - 1]:  # 可以在该机器上进行加工
                # 这个机器的所有的job以及job所在位置
                m_nesigs_job_2, m_nesigs_job_pos_2 = get_job_pos(pop_nesigs, m_nesigs_NEES, N)
                # 这两个机器所有job组成的pop
                pop_m_nesigs_NEES_ini = m_nesigs_job + m_nesigs_job_2 + [job_nesigs_inm for _ in
                                                                         range(len(m_nesigs_job))] + [m_nesigs_NEES for
                                                                                                      _ in range(
                        len(m_nesigs_job_2))]
                # 这两个机器所有job的et
                et_m_nesigs_NEES_ini = ET_nesigs_m_all[job_nesigs_inm - 1] + ET_nesigs_m_all[m_nesigs_NEES - 1]
                # job和该机器所有个体swap产生的所有的pop
                pop_m_nesigs_NEES_swap_list = []
                for m_nesigs_job_2_in in m_nesigs_job_2:  # 对于该机器上的所有作业
                    # 对于job与该机器上的一个job swap之后的个体
                    pop_m_nesigs_NEES_swap = m_nesigs_job + m_nesigs_job_2
                    pos_nesigs_NEES_1 = pop_m_nesigs_NEES_swap.index(pop_nesigs_rjs_1[pop_neigs_swap_n])
                    pos_nesigs_NEES_2 = pop_m_nesigs_NEES_swap.index(m_nesigs_job_2_in)
                    pop_m_nesigs_NEES_swap[pos_nesigs_NEES_1], pop_m_nesigs_NEES_swap[pos_nesigs_NEES_2] = \
                    pop_m_nesigs_NEES_swap[pos_nesigs_NEES_2], pop_m_nesigs_NEES_swap[pos_nesigs_NEES_1]
                    pop_m_nesigs_NEES_swap = pop_m_nesigs_NEES_swap + [job_nesigs_inm for _ in
                                                                       range(len(m_nesigs_job))] + [m_nesigs_NEES for
                                                                                                    _ in range(
                            len(m_nesigs_job_2))]

                    pop_m_nesigs_NEES_swap_list.append(copy.deepcopy(pop_m_nesigs_NEES_swap))
                S, E, O = decoding(pop_m_nesigs_NEES_swap_list, N, M, P, D, A, B)
                et_m_nesigs_NEES_swap_list = fitness_et(A, B, S, E, D)
                # job和该机器的所有作业进行swap 产生的最优的两个机器的pop
                if len(et_m_nesigs_NEES_swap_list) != 0:
                    pop_m_nesigs_NEES_swap_best = pop_m_nesigs_NEES_swap_list[et_m_nesigs_NEES_swap_list.index(min(et_m_nesigs_NEES_swap_list))]
                    # 对于该机器产生的最优的完整的pop
                    # 得到两个机器的job 的完整的 pop
                    pop_m_nesigs_NEES_swap_return = get_total_pop(m_nesigs_job_pos + m_nesigs_job_pos_2, pop_nesigs,
                                                              pop_m_nesigs_NEES_swap_best, N)
                    pop_swap_nesigs_NEES_m_list.append(pop_m_nesigs_NEES_swap_return)  # 每一个机器swap最优的的pop的list
        # pop_swap_nesigs_NEES_m_list 每一个机器swap最优的的pop的list

        # 内部+外部最优的pop
        pop_swap_nesigs_NEIS_NEES_list = []
        if len(pop_nesigs_NEIS_swap_return) != 0:
            pop_swap_nesigs_NEIS_NEES_list = pop_swap_nesigs_NEIS_NEES_list + copy.deepcopy([pop_nesigs_NEIS_swap_return])
        if len(pop_swap_nesigs_NEES_m_list) != 0:
            pop_swap_nesigs_NEIS_NEES_list = pop_swap_nesigs_NEIS_NEES_list + copy.deepcopy(pop_swap_nesigs_NEES_m_list)
        S, E, O = decoding(pop_swap_nesigs_NEIS_NEES_list, N, M, P, D, A, B)
        et_NEIS_NEES_swap_list = fitness_et(A, B, S, E, D)
        pop_NEIS_NEES_swap_list_forallrjs.append(
            copy.deepcopy(pop_swap_nesigs_NEIS_NEES_list[et_NEIS_NEES_swap_list.index(min(et_NEIS_NEES_swap_list))]))
        et_NEIS_NEES_swap_list_forallrjs.append(min(et_NEIS_NEES_swap_list))
    et_nesigs_best = min(et_NEIS_NEES_swap_list_forallrjs)
    if et_nesigs_best < pop_nesigs_et:
        pop_nesigs_re = pop_NEIS_NEES_swap_list_forallrjs[et_NEIS_NEES_swap_list_forallrjs.index(et_nesigs_best)]
        pop_nesigs_et_re = et_nesigs_best
        return pop_nesigs_re, pop_nesigs_et_re
    else:
        pop_nesigs_re = copy.deepcopy(pop_nesigs)
        pop_nesigs_et_re = pop_nesigs_et
        return pop_nesigs_re, pop_nesigs_et_re
