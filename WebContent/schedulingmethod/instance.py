import random
import numpy as np
import copy

# 按照规则生成一个算例

M = 10  # 机器数
N = 50  # 工件数
n_type = 5  # 车辆的种类（不同的车型）
# 机器可加工工件类别 5台机器 3个类别.（不同的月台类型 匹配不同的车型）
Lbm = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [1, 2, 3, 4, 5]
]

M = 20  # 机器数
N = 100  # 工件数
n_type = 5  # 车辆的种类（不同的车型）
Lbm = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [1],
    [2],
    [3],
    [4],
    [5],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

# Lbm = [[] for _ in range(M)]
# for n_type_i in range(n_type):  # 对于每一种类型的月台有3个
#     n_type_in = n_type_i + 1
#     for _ in range(3):
#         ran_lbm = np.random.randint(low=0, high=M)
#         while n_type_in in Lbm[ran_lbm]:
#             ran_lbm = np.random.randint(low=0, high=M)
#         Lbm[ran_lbm].append(n_type_in)

# M = 4  # 机器数
# N = 20  # 工件数
# n_type = 2  # 车辆的种类（不同的车型）
# # 机器可加工工件类别 5台机器 3个类别.（不同的月台类型 匹配不同的车型）
# Lbm = [
#     [1],
#     [2],
#     [1, 2],
#     [1, 2]
# ]

# M = 3  # 机器数
# N = 20  # 工件数
# n_type = 2  # 车辆的种类（不同的车型）
# # 机器可加工工件类别 5台机器 3个类别.（不同的月台类型 匹配不同的车型）
# Lbm = [
#     [1],
#     [2],
#     [1, 2]
# ]

# 交货期
# T = 0.2  # tardiness factor
T_list = [0.1, 0.3]
# RDD = 0.8  # relative　range of the due windows
RDD_list = [1.2, 1.4]
R_list = [0.2, 0.4]

for T in T_list:
    for RDD in RDD_list:
        for R in R_list:
            # 工件可以在哪个类型的机器上加工，随机生成
            Lbn = [random.randint(1, n_type) for n in range(N)]  # 1~n_type之间的随机自然数
            b_bound_left = 1
            b_bound_right = 5
            # 提前惩罚
            A = [1 for n in range(N)]
            for _ in range(int(N*0.2)):  # 有5%的客户为vip客户
                ran_a = np.random.randint(low=0, high=N)
                while A[ran_a] != 1:
                    ran_a = np.random.randint(low=0, high=N)
                A[ran_a] = 5
            # 拖后惩罚
            B = [a_in*2 for a_in in A]

            Lbmnum = np.zeros(M, dtype=np.int)  # 机器的类别数量
            i = 0
            for lbm in Lbm:
                for lbmm in lbm:  # 机器的类别数量的计算
                    Lbmnum[i] += 1
                i += 1
            Ma = []  # 每个零件可以使用的机器
            for n in range(N):
                Ma.append([])
            Manum = np.zeros(N, dtype=np.int)  # 每个零件可以使用的机器数量
            for n1 in range(N):  # 对于每个工件，计算Ma
                lbn = Lbn[n1]  # 这个工件在哪个类别的机器上加工
                for m in range(M):  # 每一个机器
                    lbm = Lbm[m]  # lbm 机器m可以加工的类别
                    i = 0
                    lbmnum = Lbmnum[m]
                    for l in range(lbmnum):  # 对于机器的每一个类别
                        if lbm[i] == lbn:
                            Ma[n1].append(m + 1)
                            Manum[n1] += 1
                            break
                        i += 1


            # 工件的加工时间
            P = []  # 1-100之间的随机自然数
            p_sum = 0
            p_num = 0
            for n in range(N):  # 对于每一个工件
                pn = []  # 对于每一个工件的在每一个机器上的加工时间
                for m in range(M):  # 对于每一个机器
                    # 平均作业时长
                    if Lbn[n] in Lbm[m]:  # Lbn[n]工件的类别，Lbm[m]机器可以加工的类别
                        ran = random.randint(20, 100)  # 之间的随机自然数
                        p_sum += ran
                        p_num += 1
                        pn.append(copy.deepcopy(ran))
                    else:
                        pn.append(999)
                P.append(copy.deepcopy(pn))
            p_av = p_sum/p_num  # 每个工件的总的平均加工时间
            print('p_av', p_av)
            # 每个工件的平均加工时间

            print('T=', T)
            print('RDD=', RDD)
            print('R=', R)
            window_center_bound_left = (1 - T - RDD / 2) * p_av * N / M
            window_center_bound_right = (1 - T + RDD / 2) * p_av * N / M
            print(window_center_bound_left, ',', window_center_bound_right)
            D = []  # 窗口
            for n in range(N):  # 对于每一个工件
                status = True
                p_min = 999  # 车辆作业的时间的最大值
                p_sum = 0
                p_max = 0
                for ma in Ma[n]:  # 对于每一个车辆可以使用的月台
                    p_sum += P[n][ma - 1]
                    if p_min > P[n][ma - 1]:
                        p_min = P[n][ma - 1]
                    if p_max < P[n][ma - 1]:
                        p_max = P[n][ma - 1]
                while status:
                    window_center = np.random.randint(low=window_center_bound_left, high=window_center_bound_right)
                    window_size = np.random.randint(low=p_min, high=p_max*(1+R))
                    ran_s = window_center - int(window_size/2)
                    ran_e = ran_s + window_size
                    if ran_s >= 0:
                        status = False
                dn = [copy.deepcopy(ran_s), copy.deepcopy(ran_e)]
                D.append(copy.deepcopy(dn))
            print('Lbn =', Lbn)
            print('Lbm =', Lbm)
            print('A =', A)
            print('B =', B)
            print('P =', P)
            print('D =', D)