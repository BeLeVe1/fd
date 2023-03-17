import copy

import matplotlib.pyplot as plt
import numpy as np

from decoding_def import decoding


# 最优个体
# 加工时间
def gantt(pop_gantt, flow, N, M, P, D, A, B):
    pop_gantt = copy.deepcopy(pop_gantt)
    workpiece = pop_gantt[0:N]  # 工件号 J1=1,J2=2
    macInfo = pop_gantt[N:2 * N]  # 对应的机器号 M1=1,M2=2,…
    # 解码
    S, E, O = decoding([pop_gantt], N, M, P, D, A, B)
    macStartTime = S[0]  # 开始作业时间
    print('S', S[0])
    print('E', E[0])
    plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Platform")
    plt.title("Gantt chart of platform dispatching")
    colorList = [  # 60个
        '#FFDCA6', '#FF33CC', '#3333CC', '#FFBFA0', '#FF6A66',
        '#66FF00', '#6699CC', '#FF9900', '#008B8B', '#99CC99',
        '#CCFF33', '#66CC66', '#99CCCC', '#CCCC66', '#009999',
        '#800080', '#0000FF', '#008000', '#FFD700', '#FF4500',
        '#8A2BE2', '#FAEB77', '#00FBBF', '#7FFFD4', '#D2691E',
        '#32CD32', '#800000', '#8FBC8F', '#0000FF', '#DEB887',
        '#FF00FF', '#A9A9A9', '#006400', '#9932CC', '#FF1493',
        '#1E90FF', '#B22222', '#228B22', '#DCDCDC', '#FAA700',
        '#808080', '#ADFF2F', '#4B0082', '#F0E68C', '#FFA0F5',
        '#E0FABF', '#D3D3D3', '#00FF00', '#66CDAA', '#FAE4E1',
        '#FDF5E6', '#FFA500', '#CD853F', '#DDA0DD', '#BC8F8F',
        '#C0C0C0', '#FFFAFA', '#FF6347', '#F5DEB3', '#008080',
        '#8A2BE2', '#FAEB77', '#00FBBF', '#7FFFD4', '#D2691E',
        '#32CD32', '#800000', '#8FBC8F', '#0000FF', '#DEB887',
        '#FF00FF', '#A9A9A9', '#006400', '#9932CC', '#FF1493',
        '#1E90FF', '#B22222', '#228B22', '#DCDCDC', '#FAA700',
        '#808080', '#ADFF2F', '#4B0082', '#F0E68C', '#FFA0F5',
        '#E0FABF', '#D3D3D3', '#00FF00', '#66CDAA', '#FAE4E1',
        '#FDF5E6', '#FFA500', '#CD853F', '#DDA0DD', '#BC8F8F',
        '#C0C0C0', '#FFFAFA', '#FF6347', '#F5DEB3', '#008080',
    ]  # 生成工件颜色矩阵
    for j in range(len(macInfo)):
        i = macInfo[j]  # 机器号 月台号
        w = workpiece[j]  # 工件号
        plt.barh(i, flow[w - 1][i - 1], 0.6, left=macStartTime[workpiece[j] - 1], edgecolor="black", color = colorList[w-1])
        # barh函数的参数：y坐标, width宽度, height高度, left左侧长度，color颜色 不指定颜色为随机颜色
        plt.text(macStartTime[workpiece[j] - 1] + flow[w - 1][i - 1] / 8, i, 'J%s' % (workpiece[j]), color="white",
                 size=12)
        # text函数的参数：x坐标, y坐标, s标注的内容
        # s标注的内容：s='J%s.%s' % (workpiece[j], operation[j]) 表示 J1.1
        # s=(CHS[j+12],End_time[i,j])表示（1，1）
    plt.yticks(np.arange(max(macInfo)) + 1, np.arange(max(macInfo)) + 1)  # 替换y坐标
    plt.show()
    # yticks函数的参数：ticks, labels
    # ticks：The list of ytick location
    # labels：The l
