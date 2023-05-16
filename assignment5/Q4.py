# Q4 - ANSI C 의사 난수 생성기를 사용하여 다음을 수행합니다.

import numpy as np
import matplotlib.pyplot as plt

# a) 5000개의 Uniform [0,1] 분포 샘플을 생성하시오.

def ansi(m = (2**31), a = 1103515245 , c = 12345):
    global seed
    seed = (a*seed + c) % m
    return seed / m

ansi_random_num = [ansi() for i in range(5000)]

# b) 5000개의 표준 정규분포 mean = 0, variance = 1을 가진 샘플을 Box-Muller 알고리즘으로 생성하시고 히스토그램을 그리시오.

bm_U1_list = [ansi() for i in range(5000)]
bm_U1 = np.array(bm_U1_list)
bm_U2_list = [ansi() for i in range(5000)]
bm_U2 = np.array(bm_U2_list)

R = np.sqrt(-2 * np.log(bm_U1))
Theta = 2 * np.pi * bm_U2

bm_X = R * np.cos(Theta)
bm_Y = R * np.sin(Theta)

fig,(ax1,ax2) = plt.subplots(1,2)
temp = ax1.hist(bm_X, bins = 50, edgecolor = 'black')
temp = ax2.hist(bm_Y, bins = 50, edgecolor = 'black')
plt.suptitle('Box-Muller',fontsize=20)
plt.show()

# c) 5000개의 표준 정규분포 mean = 0, variance = 1을 가진 샘플을 Polar-Marsaglia 알고리즘으로 생성하시고 히스토그램을 그리시오.

pm_U1_list = [ansi() for i in range(5000)]
pm_U1 = np.array(pm_U1_list)
pm_U2_list = [ansi() for i in range(5000)]
pm_U2 = np.array(pm_U2_list)

V1 = 2 * pm_U1 - 1
V2 = 2 * pm_U2 - 1

W = (V1**2) + (V2**2)

T = np.sqrt((-2 * np.log(W)) / W)
    
pm_X = V1 * T
pm_Y = V2 * T

fig,(ax1,ax2) = plt.subplots(1,2)
temp = ax1.hist(pm_X, bins = 50, edgecolor = 'black')
temp = ax2.hist(pm_Y, bins = 50, edgecolor = 'black')
plt.suptitle('Polar-Marsaglia',fontsize=20)
plt.show()

# d) 이제 5000개의 정규 분포를 생성하는데 걸리는 시간을 비교하시오. 어떤 방법론이 더 효율적인가? 만약 시간차이가 적은 경우 샘플 사이즈를 늘려 확인하시오.

print("\nPolar-Marsaglia 방법론은 Box-Muller 방법론과 달리 sin cos을 사용하지 않아 더 빠를 것이라 예상했다. 그러나, 예상과 달리 Box-Muller 방법론이 Polar-Marsaglia 보다 더욱 짧은 시간안에 정규 분포를 생산해냈다. 결론적으로, Box-Muller 방법론이 더 효율적이다.")