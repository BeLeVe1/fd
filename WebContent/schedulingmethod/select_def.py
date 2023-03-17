import numpy as np
import copy


def select_sa(POP, POP_crossover, Fit_POP, ET_penalty_POP, Fit_crossover, ET_penalty_crossover, T):
    POP_new = []
    Fit_POP_new = []
    ET_penalty_POP_new = []
    for i in range(len(POP)):  # 对种群中的每一个个体进行逐一对比，选择刚好的那一个
        # pop = POP[i]  # 父代个体
        # fit_pop = Fit_POP[i]
        # et_pop = ET_penalty_POP[i]
        # pop_crossover = POP_crossover[i]  # 交叉个体
        # fit_crossover = Fit_crossover[i]
        # et_crossover = ET_penalty_crossover[i]
        if Fit_POP[i] > Fit_crossover[i]:
            # print(np.exp(-(Fit_POP[i]-Fit_crossover[i])/T))
            if min(1, np.exp(-(Fit_POP[i]-Fit_crossover[i])/T)) > np.random.rand():  # fit越大越好
                POP_new.append(copy.deepcopy(POP_crossover[i]))
                Fit_POP_new.append(copy.deepcopy(Fit_crossover[i]))
                ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_crossover[i]))
                # print('接受劣解')
            else:
                POP_new.append(copy.deepcopy(POP[i]))
                Fit_POP_new.append(copy.deepcopy(Fit_POP[i]))
                ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_POP[i]))
        else:
            POP_new.append(copy.deepcopy(POP_crossover[i]))
            Fit_POP_new.append(copy.deepcopy(Fit_crossover[i]))
            ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_crossover[i]))
    return POP_new, Fit_POP_new, ET_penalty_POP_new


def select(POP, POP_crossover, Fit_POP, ET_penalty_POP, Fit_crossover, ET_penalty_crossover):
    POP_new = []
    Fit_POP_new = []
    ET_penalty_POP_new = []
    for i in range(len(POP)):  # 对种群中的每一个个体进行逐一对比，选择刚好的那一个
        # pop = POP[i]  # 父代个体
        # fit_pop = Fit_POP[i]
        # et_pop = ET_penalty_POP[i]
        # pop_crossover = POP_crossover[i]  # 交叉个体
        # fit_crossover = Fit_crossover[i]
        # et_crossover = ET_penalty_crossover[i]
        if Fit_POP[i] > Fit_crossover[i]:
            POP_new.append(copy.deepcopy(POP[i]))
            Fit_POP_new.append(copy.deepcopy(Fit_POP[i]))
            ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_POP[i]))
        else:
            POP_new.append(copy.deepcopy(POP_crossover[i]))
            Fit_POP_new.append(copy.deepcopy(Fit_crossover[i]))
            ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_crossover[i]))
    return POP_new, Fit_POP_new, ET_penalty_POP_new

def select_(POP, POP_crossover, Fit_POP, ET_penalty_POP, Fit_crossover, ET_penalty_crossover):
    POP_new = []
    Fit_POP_new = []
    ET_penalty_POP_new = []
    for i in range(len(POP)):  # 对种群中的每一个个体进行逐一对比，选择刚好的那一个
        # pop = POP[i]  # 父代个体
        # fit_pop = Fit_POP[i]
        # et_pop = ET_penalty_POP[i]
        # pop_crossover = POP_crossover[i]  # 交叉个体
        # fit_crossover = Fit_crossover[i]
        # et_crossover = ET_penalty_crossover[i]
        if Fit_POP[i] <= Fit_crossover[i]:
            POP_new.append(copy.deepcopy(POP_crossover[i]))
            Fit_POP_new.append(copy.deepcopy(Fit_crossover[i]))
            ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_crossover[i]))
        else:
            POP_new.append(copy.deepcopy(POP[i]))
            Fit_POP_new.append(copy.deepcopy(Fit_POP[i]))
            ET_penalty_POP_new.append(copy.deepcopy(ET_penalty_POP[i]))
    return POP_new, Fit_POP_new, ET_penalty_POP_new
