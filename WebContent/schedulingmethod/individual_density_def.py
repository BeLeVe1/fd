import copy

from decoding_def import decoding_task


def individual_density(POP, N, M, P, D, A, B):
    n_total = len(POP)  # 种群中所有个体的数量
    n_independent = 0  # 种群中独立个体的数量
    POP_task = decoding_task(POP, N, M, P, D, A, B)
    while len(POP_task) != 0:
        task_i = copy.deepcopy(POP_task[0])
        n_independent += 1
        POP_task.pop(0)
        while task_i in POP_task:
            POP_new_i_pos = POP_task.index(task_i)
            POP_task.pop(POP_new_i_pos)
    density = n_independent / n_total  # 种群的多样性
    print('多样性', density)
    return density
