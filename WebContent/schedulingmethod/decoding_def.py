import numpy as np
import copy


# POP 第一段：车辆的作业顺序,第二段：车辆的作业月台
# N 工件数
# M 机器数
# P 工件的加工时间
# A 提前惩罚
# B 拖后惩罚
import numpy as np
import copy


# POP 第一段：车辆的作业顺序,第二段：车辆的作业月台
# N 工件数
# M 机器数
# P 工件的加工时间
# A 提前惩罚
# B 拖后惩罚
def decoding(POP, N, M, P, D, A, B):
    # 参考 求解带有时间窗和提前_拖期惩罚的飞机着陆问题的遗传算法_王宏一文
    S = []
    E = []
    O = []
    for pop in POP:
        task = []  # 对于这个种群 每个月台的作业的车辆
        for m1 in range(M):
            task.append([])
        for i in range(int(len(pop) / 2)):
            n = copy.deepcopy(pop[i])  # 车辆
            m = pop[i + int(len(pop) / 2)]  # 作业月台
            task[m - 1].append(n)
        # 得到了该种群 每个月台的作业的车辆
        e = []  # 对于每一个种群 车辆结束作业时间
        s = []  # 车辆开始作业时间
        o = []  # 月台占用时间 n行 每行中一个块为另一个小列表
        for n1 in range(N):
            e.append(0)
            s.append(0)
        for m1 in range(M):
            o.append([])
        for m in range(M):  # 对于(m+1)月台上的 车辆作业任务进行解码
            Block = []  # 块，连续作业为一个块
            R = 0  # 该月台上的作业车辆总数
            for task_m in task[m]:
                R += 1
            r = 1  # 该月台上的第r个作业车辆

            t = 1  # 该月台块数
            for _ in range(2):
                o[m].append([])
            Block.append([])  # 第一个块

            if R != 0:  # 该月台上有车辆作业任务
                # 对r=1时
                n_copy = copy.deepcopy(task[m][r - 1])  # 第一个作业的车辆
                Block[t - 1].append(n_copy)
                s[n_copy - 1] = D[n_copy - 1][0]
                e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                o[m][2 * t - 1 - 1] = s[n_copy - 1]
                o[m][2 * t - 1] = e[n_copy - 1]
                while r < R:
                    n_copy = copy.deepcopy(task[m][r + 1 - 1])  # 第r+1个作业的车辆
                    if o[m][2 * t - 1] < D[n_copy - 1][0]:  # 块的结束时间<下一个作业车辆的最早开始时间，将该任务分为下一个块的第一个任务
                        r += 1
                        t += 1  # 建另一个块
                        for _ in range(2):
                            o[m].append([])
                        Block.append([])  # 新建一个块
                        s[n_copy - 1] = D[n_copy - 1][0]
                        e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                        o[m][2 * t - 1 - 1] = s[n_copy - 1]
                        o[m][2 * t - 1] = e[n_copy - 1]
                        Block[t - 1].append(n_copy)
                    elif o[m][2 * t - 1] == D[n_copy - 1][0]:  # 块的结束时间=下一个作业车辆的最早开始时间，将该任务放进块t中
                        r += 1
                        s[n_copy - 1] = D[n_copy - 1][0]
                        e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                        o[m][2 * t - 1] = e[n_copy - 1]
                        Block[t - 1].append(n_copy)
                    else:  # o[2 * t - 1] > D[n_copy - 1][0]:  块的结束时间>下一个作业车辆的最早开始时间，导致了任务r+1拖后
                        r += 1
                        n_copy = copy.deepcopy(task[m][r - 1])  # 作业车辆
                        s[n_copy - 1] = o[m][2 * t - 1]
                        o[m][2 * t - 1] = o[m][2 * t - 1] + P[n_copy - 1][m]
                        e[n_copy - 1] = o[m][2 * t - 1]
                        Block[t - 1].append(n_copy)
                        check_move = True
                        while check_move:
                            check_move = False
                            x = []  # 变量x ， x表示块可以提前的距离
                            x_bound = 0  # 变量x的取值范围
                            if t == 1:  # 如果是第一个块
                                x_bound = o[m][2 * t - 1 - 1]
                                # 块前边与0的距离 下一个作业与块的结束之间的距离
                            else:
                                x_bound = o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1]
                            if x_bound != 0:
                                for r_b in range(len(Block[t - 1])):  # 函数的分段 变量x边界
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_copy = copy.deepcopy(e[n_copy - 1] - D[n_copy - 1][1])
                                    if x_copy not in x:
                                        x.append(x_copy)
                                for r_b in range(len(Block[t - 1])):
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_copy = copy.deepcopy(s[n_copy - 1] - D[n_copy - 1][0])
                                    if x_copy not in x:
                                        x.append(x_copy)
                                for i in range(len(x) - 1):  # 对ｘ进行冒泡排序
                                    for j in range(len(x) - i - 1):
                                        if x[j] > x[j + 1]:
                                            x[j], x[j + 1] = x[j + 1], x[j]
                                x_slope = []  # 储存x对应惩罚的斜率，找出斜率从负到正的转变点
                                # 负无穷到第一个点
                                x_slope_n = 0
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_slope_n += -B[n_copy - 1]
                                x_slope.append(copy.deepcopy(x_slope_n))
                                for x_num in range(len(x) - 1):
                                    #  对于x(x_num)和x(x_num+1)区间求斜率
                                    x_slope_n = 0
                                    for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                        n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                        if s[n_copy - 1] - D[n_copy - 1][0] <= x[x_num]:  # 提前惩罚
                                            x_slope_n += A[n_copy - 1]
                                        if e[n_copy - 1] - D[n_copy - 1][1] >= x[x_num + 1]:  # 拖后惩罚
                                            x_slope_n += -B[n_copy - 1]
                                    x_slope.append(copy.deepcopy(x_slope_n))
                                # 最后一个点到正无穷
                                x_slope_n = 0
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_slope_n += A[n_copy - 1]
                                x_slope.append(copy.deepcopy(x_slope_n))

                                for x_slope_num in range(len(x_slope)):
                                    if x_slope[len(x_slope) - 1] > 0:  # x_slope中的最后一位是否大于零，是则pop
                                        x_slope.pop()
                                x_move = x[len(x_slope)-1]
                                if x_move < 0:
                                    x_move = 0
                                elif x_move > x_bound:
                                    x_move = x_bound
                                o[m][2 * t - 1 - 1] = o[m][2 * t - 1 - 1] - x_move
                                o[m][2 * t - 1] = o[m][2 * t - 1] - x_move
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    e[n_copy - 1] = e[n_copy - 1] - x_move
                                    s[n_copy - 1] = s[n_copy - 1] - x_move

                                if t > 1:
                                    if o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1] == 0:  # 判断块是否需要合并
                                        for b in Block[t - 1]:
                                            b_copy = copy.deepcopy(b)
                                            Block[t - 1 - 1].append(b_copy)
                                        del Block[t - 1]
                                        o[m][2 * t - 2 - 1] = o[m][2 * t - 1]
                                        del o[m][2 * t - 1]
                                        del o[m][2 * t - 1 - 1]
                                        t -= 1
                                        check_move = True
        s_copy = copy.deepcopy(s)
        e_copy = copy.deepcopy(e)
        o_copy = copy.deepcopy(o)
        S.append(s_copy)
        E.append(e_copy)
        O.append(o_copy)
    return S, E, O


def decoding_(pop, N, M, P, D, A, B):
    task = []  # 对于这个种群 每个月台的作业的车辆
    for m1 in range(M):
        task.append([])
    for i in range(int(len(pop) / 2)):
        n = copy.deepcopy(pop[i])  # 车辆
        m = pop[i + int(len(pop) / 2)]  # 作业月台
        task[m - 1].append(n)
    # 得到了该种群 每个月台的作业的车辆
    e = []  # 对于每一个种群 车辆结束作业时间
    s = []  # 车辆开始作业时间
    o = []  # 月台占用时间 n行 每行中一个块为另一个小列表
    for n1 in range(N):
        e.append(0)
        s.append(0)
    for m1 in range(M):
        o.append([])
    for m in range(M):  # 对于(m+1)月台上的 车辆作业任务进行解码
        Block = []  # 块，连续作业为一个块
        R = 0  # 该月台上的作业车辆总数
        for task_m in task[m]:
            R += 1
        r = 1  # 该月台上的第r个作业车辆

        t = 1  # 该月台块数
        for _ in range(2):
            o[m].append([])
        Block.append([])  # 第一个块

        if R != 0:  # 该月台上有车辆作业任务
            # 对r=1时
            n_copy = copy.deepcopy(task[m][r - 1])  # 第一个作业的车辆
            Block[t - 1].append(n_copy)
            s[n_copy - 1] = D[n_copy - 1][0]
            e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
            o[m][2 * t - 1 - 1] = s[n_copy - 1]
            o[m][2 * t - 1] = e[n_copy - 1]
            while r < R:
                n_copy = copy.deepcopy(task[m][r + 1 - 1])  # 第r+1个作业的车辆
                if o[m][2 * t - 1] < D[n_copy - 1][0]:  # 块的结束时间<下一个作业车辆的最早开始时间，将该任务分为下一个块的第一个任务
                    r += 1
                    t += 1  # 建另一个块
                    for _ in range(2):
                        o[m].append([])
                    Block.append([])  # 新建一个块
                    s[n_copy - 1] = D[n_copy - 1][0]
                    e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                    o[m][2 * t - 1 - 1] = s[n_copy - 1]
                    o[m][2 * t - 1] = e[n_copy - 1]
                    Block[t - 1].append(n_copy)
                elif o[m][2 * t - 1] == D[n_copy - 1][0]:  # 块的结束时间=下一个作业车辆的最早开始时间，将该任务放进块t中
                    r += 1
                    s[n_copy - 1] = D[n_copy - 1][0]
                    e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                    o[m][2 * t - 1] = e[n_copy - 1]
                    Block[t - 1].append(n_copy)
                else:  # o[2 * t - 1] > D[n_copy - 1][0]:  块的结束时间>下一个作业车辆的最早开始时间，导致了任务r+1拖后
                    r += 1
                    n_copy = copy.deepcopy(task[m][r - 1])  # 作业车辆
                    s[n_copy - 1] = o[m][2 * t - 1]
                    o[m][2 * t - 1] = o[m][2 * t - 1] + P[n_copy - 1][m]
                    e[n_copy - 1] = o[m][2 * t - 1]
                    Block[t - 1].append(n_copy)
                    check_move = True
                    while check_move:
                        check_move = False
                        x = []  # 变量x ， x表示块可以提前的距离
                        x_bound = 0  # 变量x的取值范围
                        if t == 1:  # 如果是第一个块
                            x_bound = o[m][2 * t - 1 - 1]
                            # 块前边与0的距离 下一个作业与块的结束之间的距离
                        else:
                            x_bound = o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1]
                        if x_bound != 0:
                            for r_b in range(len(Block[t - 1])):  # 函数的分段 变量x边界
                                n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                x_copy = copy.deepcopy(e[n_copy - 1] - D[n_copy - 1][1])
                                if x_copy not in x:
                                    x.append(x_copy)
                            for r_b in range(len(Block[t - 1])):
                                n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                x_copy = copy.deepcopy(s[n_copy - 1] - D[n_copy - 1][0])
                                if x_copy not in x:
                                    x.append(x_copy)
                            for i in range(len(x) - 1):  # 对ｘ进行冒泡排序
                                for j in range(len(x) - i - 1):
                                    if x[j] > x[j + 1]:
                                        x[j], x[j + 1] = x[j + 1], x[j]
                            x_slope = []  # 储存x对应惩罚的斜率，找出斜率从负到正的转变点
                            # 负无穷到第一个点
                            x_slope_n = 0
                            for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                x_slope_n += -B[n_copy - 1]
                            x_slope.append(copy.deepcopy(x_slope_n))
                            for x_num in range(len(x) - 1):
                                #  对于x(x_num)和x(x_num+1)区间求斜率
                                x_slope_n = 0
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    if s[n_copy - 1] - D[n_copy - 1][0] <= x[x_num]:  # 提前惩罚
                                        x_slope_n += A[n_copy - 1]
                                    if e[n_copy - 1] - D[n_copy - 1][1] >= x[x_num + 1]:  # 拖后惩罚
                                        x_slope_n += -B[n_copy - 1]
                                x_slope.append(copy.deepcopy(x_slope_n))
                            # 最后一个点到正无穷
                            x_slope_n = 0
                            for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                x_slope_n += A[n_copy - 1]
                            x_slope.append(copy.deepcopy(x_slope_n))

                            for x_slope_num in range(len(x_slope)):
                                if x_slope[len(x_slope) - 1] > 0:  # x_slope中的最后一位是否大于零，是则pop
                                    x_slope.pop()
                            x_move = x[len(x_slope) - 1]
                            if x_move < 0:
                                x_move = 0
                            elif x_move > x_bound:
                                x_move = x_bound
                            o[m][2 * t - 1 - 1] = o[m][2 * t - 1 - 1] - x_move
                            o[m][2 * t - 1] = o[m][2 * t - 1] - x_move
                            for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                e[n_copy - 1] = e[n_copy - 1] - x_move
                                s[n_copy - 1] = s[n_copy - 1] - x_move

                            if t > 1:
                                if o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1] == 0:  # 判断块是否需要合并
                                    for b in Block[t - 1]:
                                        b_copy = copy.deepcopy(b)
                                        Block[t - 1 - 1].append(b_copy)
                                    del Block[t - 1]
                                    o[m][2 * t - 2 - 1] = o[m][2 * t - 1]
                                    del o[m][2 * t - 1]
                                    del o[m][2 * t - 1 - 1]
                                    t -= 1
                                    check_move = True


    return s, e, o


def decoding_task(POP, N, M, P, D, A, B):
    # 参考 求解带有时间窗和提前_拖期惩罚的飞机着陆问题的遗传算法_王宏一文
    S = []
    E = []
    O = []
    POP_task = []
    for pop in POP:
        task = []  # 对于这个种群 每个月台的作业的车辆
        for m1 in range(M):
            task.append([])
        for i in range(int(len(pop) / 2)):
            n = copy.deepcopy(pop[i])  # 车辆
            m = pop[i + int(len(pop) / 2)]  # 作业月台
            task[m - 1].append(n)
        # 得到了该种群 每个月台的作业的车辆
        e = []  # 对于每一个种群 车辆结束作业时间
        s = []  # 车辆开始作业时间
        o = []  # 月台占用时间 n行 每行中一个块为另一个小列表
        for n1 in range(N):
            e.append(0)
            s.append(0)
        for m1 in range(M):
            o.append([])
        for m in range(M):  # 对于(m+1)月台上的 车辆作业任务进行解码
            Block = []  # 块，连续作业为一个块
            R = 0  # 该月台上的作业车辆总数
            for task_m in task[m]:
                R += 1
            r = 1  # 该月台上的第r个作业车辆

            t = 1  # 该月台块数
            for _ in range(2):
                o[m].append([])
            Block.append([])  # 第一个块

            if R != 0:  # 该月台上有车辆作业任务
                # 对r=1时
                n_copy = copy.deepcopy(task[m][r - 1])  # 第一个作业的车辆
                Block[t - 1].append(n_copy)
                s[n_copy - 1] = D[n_copy - 1][0]
                e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                o[m][2 * t - 1 - 1] = s[n_copy - 1]
                o[m][2 * t - 1] = e[n_copy - 1]
                while r < R:
                    n_copy = copy.deepcopy(task[m][r + 1 - 1])  # 第r+1个作业的车辆
                    if o[m][2 * t - 1] < D[n_copy - 1][0]:  # 块的结束时间<下一个作业车辆的最早开始时间，将该任务分为下一个块的第一个任务
                        r += 1
                        t += 1  # 建另一个块
                        for _ in range(2):
                            o[m].append([])
                        Block.append([])  # 新建一个块
                        s[n_copy - 1] = D[n_copy - 1][0]
                        e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                        o[m][2 * t - 1 - 1] = s[n_copy - 1]
                        o[m][2 * t - 1] = e[n_copy - 1]
                        Block[t - 1].append(n_copy)
                    elif o[m][2 * t - 1] == D[n_copy - 1][0]:  # 块的结束时间=下一个作业车辆的最早开始时间，将该任务放进块t中
                        r += 1
                        s[n_copy - 1] = D[n_copy - 1][0]
                        e[n_copy - 1] = s[n_copy - 1] + P[n_copy - 1][m]
                        o[m][2 * t - 1] = e[n_copy - 1]
                        Block[t - 1].append(n_copy)
                    else:  # o[2 * t - 1] > D[n_copy - 1][0]:  块的结束时间>下一个作业车辆的最早开始时间，导致了任务r+1拖后
                        r += 1
                        n_copy = copy.deepcopy(task[m][r - 1])  # 作业车辆
                        s[n_copy - 1] = o[m][2 * t - 1]
                        o[m][2 * t - 1] = o[m][2 * t - 1] + P[n_copy - 1][m]
                        e[n_copy - 1] = o[m][2 * t - 1]
                        Block[t - 1].append(n_copy)
                        check_move = True
                        while check_move:
                            check_move = False
                            x = []  # 变量x ， x表示块可以提前的距离
                            x_bound = 0  # 变量x的取值范围
                            if t == 1:  # 如果是第一个块
                                x_bound = o[m][2 * t - 1 - 1]
                                # 块前边与0的距离 下一个作业与块的结束之间的距离
                            else:
                                x_bound = o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1]
                            if x_bound != 0:
                                for r_b in range(len(Block[t - 1])):  # 函数的分段 变量x边界
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_copy = copy.deepcopy(e[n_copy - 1] - D[n_copy - 1][1])
                                    if x_copy not in x:
                                        x.append(x_copy)
                                for r_b in range(len(Block[t - 1])):
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_copy = copy.deepcopy(s[n_copy - 1] - D[n_copy - 1][0])
                                    if x_copy not in x:
                                        x.append(x_copy)
                                for i in range(len(x) - 1):  # 对ｘ进行冒泡排序
                                    for j in range(len(x) - i - 1):
                                        if x[j] > x[j + 1]:
                                            x[j], x[j + 1] = x[j + 1], x[j]
                                x_slope = []  # 储存x对应惩罚的斜率，找出斜率从负到正的转变点
                                # 负无穷到第一个点
                                x_slope_n = 0
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_slope_n += -B[n_copy - 1]
                                x_slope.append(copy.deepcopy(x_slope_n))
                                for x_num in range(len(x) - 1):
                                    #  对于x(x_num)和x(x_num+1)区间求斜率
                                    x_slope_n = 0
                                    for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                        n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                        if s[n_copy - 1] - D[n_copy - 1][0] <= x[x_num]:  # 提前惩罚
                                            x_slope_n += A[n_copy - 1]
                                        if e[n_copy - 1] - D[n_copy - 1][1] >= x[x_num + 1]:  # 拖后惩罚
                                            x_slope_n += -B[n_copy - 1]
                                    x_slope.append(copy.deepcopy(x_slope_n))
                                # 最后一个点到正无穷
                                x_slope_n = 0
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    x_slope_n += A[n_copy - 1]
                                x_slope.append(copy.deepcopy(x_slope_n))

                                for x_slope_num in range(len(x_slope)):
                                    if x_slope[len(x_slope) - 1] > 0:  # x_slope中的最后一位是否大于零，是则pop
                                        x_slope.pop()
                                x_move = x[len(x_slope)-1]
                                if x_move < 0:
                                    x_move = 0
                                elif x_move > x_bound:
                                    x_move = x_bound
                                o[m][2 * t - 1 - 1] = o[m][2 * t - 1 - 1] - x_move
                                o[m][2 * t - 1] = o[m][2 * t - 1] - x_move
                                for r_b in range(len(Block[t - 1])):  # 遍历块t中的每一个车辆作业任务
                                    n_copy = copy.deepcopy(Block[t - 1][r_b])  # 作业车辆
                                    e[n_copy - 1] = e[n_copy - 1] - x_move
                                    s[n_copy - 1] = s[n_copy - 1] - x_move

                                if t > 1:
                                    if o[m][2 * t - 1 - 1] - o[m][2 * t - 2 - 1] == 0:  # 判断块是否需要合并
                                        for b in Block[t - 1]:
                                            b_copy = copy.deepcopy(b)
                                            Block[t - 1 - 1].append(b_copy)
                                        del Block[t - 1]
                                        o[m][2 * t - 2 - 1] = o[m][2 * t - 1]
                                        del o[m][2 * t - 1]
                                        del o[m][2 * t - 1 - 1]
                                        t -= 1
                                        check_move = True
        s_copy = copy.deepcopy(s)
        e_copy = copy.deepcopy(e)
        o_copy = copy.deepcopy(o)
        S.append(s_copy)
        E.append(e_copy)
        O.append(o_copy)
        POP_task.append(copy.deepcopy(task))
    return POP_task
