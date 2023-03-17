import numpy as np

pop = [1, 5, 6, 7, 2, 3, 4, 8, 1, 8, 1, 1, 1, 4, 3, 1]
pop=np.array(pop)

def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


pop1, pop2 = split_list(pop)
print('pop1:', pop1)
print('pop2:', pop2)
pop1inds = pop1.argsort()
sorted_pop1 = pop1[pop1inds]
sorted_pop2 = pop2[pop1inds]
print('sorted_pop1:', sorted_pop1)
print('sorted_pop2:', sorted_pop2)
