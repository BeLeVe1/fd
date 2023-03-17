import numpy as np
import copy

# A 提前惩罚
# B 拖后惩罚
# E 车辆任务结束作业的时间
# D 交货期
def fitness(A, B, S, E, D):
    Fit = []
    ET_Punishment = []
    for i_fit in range(len(E)):  # 对于每一个种群
        et = 0
        for j_fit in range(len(A)):  # 对于每一个任务
            if S[i_fit][j_fit] != E[i_fit][j_fit]:
                # 提前完工
                et += A[j_fit] * max((D[j_fit][0] - S[i_fit][j_fit]), 0)
                # 拖后完工
                et += B[j_fit] * max((E[i_fit][j_fit] - D[j_fit][1]), 0)
        # fit = 1/(fit+1)
        ET_Punishment.append(copy.deepcopy(et))
        # fit = np.exp(-fit/10)
        fit = 500-et
        Fit.append(copy.deepcopy(fit))
    return Fit, ET_Punishment


def fitness_et(A, B, S, E, D):
    ET_Punishment = []
    for i_fit in range(len(E)):  # 对于每一个种群
        et = 0
        for j_fit in range(len(A)):  # 对于每一个任务
            if S[i_fit][j_fit] != E[i_fit][j_fit]:
                # 提前完工
                et += A[j_fit] * max((D[j_fit][0] - S[i_fit][j_fit]), 0)
                # 拖后完工
                et += B[j_fit] * max((E[i_fit][j_fit] - D[j_fit][1]), 0)
        ET_Punishment.append(copy.deepcopy(et))
    return ET_Punishment


def et_getfit(et):
    return 500 - et