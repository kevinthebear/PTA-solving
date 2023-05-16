# Q1 - Lewis Goodman Miller 의사 난수 생성기를 사용하여 다음을 수행합니다.

import matplotlib.pyplot as plt
import numpy as np

# a) Lewis Goodman Miller 의사 난수 알고리즘을 이용하여 10,000개의 Uniform 분포 수열을 생성하고 히스토그램 그래프를 생성하시오.

def lgm(m = (2**31)-1, a = (7**5), c = 0):
    global seed
    seed = (a * seed + c) % m
    return seed / m

lgm_random_num = [lgm() for i in range(10000)]

plt.hist(lgm_random_num, bins = 100, edgecolor = 'black')
plt.show()

# b) Numpy의 random 함수를 이용하여 (a)와 같은 작업을 하시오.

nump_random_num = np.random.uniform(0,1,10000)
plt.hist(nump_random_num, bins = 100, edgecolor = 'black')
plt.show()