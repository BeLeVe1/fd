import numpy as np


def action_choose(action_num, action_list, reward_list):
    action_pool = list(range(0, action_num))
    # 每个action在滑动时间窗内 被选中的次数
    n_action = [0 for _ in range(action_num)]
    # 每个action在滑动时间窗内的平均reward
    r_action = [0 for _ in range(action_num)]
    # 统计n_action, r_action
    window_num = 0  # 时间窗的第几位
    for action_i in action_list:  # 对于记录中的每一条
        for action in action_pool:  # 对于每一个action
            if action_i == action:
                n_action[action] += 1
                r_action[action] += reward_list[window_num]
        window_num += 1
    for num_i in range(action_num):
        if n_action[num_i] != 0:
            r_action[num_i] = r_action[num_i] / n_action[num_i]
    # print('被选中的次数', n_action)
    # print('平均reward', r_action)
    # r最小的动作的选择次数
    mi = min(n_action)
    # 控制探索概率的参数
    w = 0.95  # 论文推荐参数,500代978所搜没有停滞
    # w = 0.5  # 500代 978 1021搜索250左右停滞
    # w = 0.2  # 500代 986 1013搜索250左右停滞
    # 探索概率
    p = w / (w + np.square(mi))
    ran = np.random.rand()
    action_choice = 0  # 选择的动作
    if ran > p:  # 选择使r最大的动作
        if sum(r_action) == 0:  # 所有reward为0
            action_choice = np.random.randint(low=0, high=action_num)
        else:
            action_choice = r_action.index(max(r_action))
    else:  # 选择被选次数最小的动作
        action_choice = n_action.index(min(n_action))
    # print('action', action_choose)
    return action_choice
