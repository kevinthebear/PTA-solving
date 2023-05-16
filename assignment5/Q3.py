# Q3 - Lewis Goodman Miller 의사 난수 생성기를 사용하여 다음을 수행합니다.

import matplotlib.pyplot as plt

# a) 1000개의 Binomial 분포 (n=44, p=0.64) 샘플을 생성하시오.

def lgm(m = (2**31)-1, a = (7**5), c = 0):
    global seed
    seed = (a * seed + c) % m
    return seed / m

lgm_random_num = [lgm() for i in range(10000)]

n = 44
p = 0.64
z = (p/(1-p))
y = ((1-p)**n)
k = 0
x = y

for i, num in enumerate(lgm_random_num):
    if num < x:
        lgm_random_num[i] = k
    else :
        y = ((n-k)/(k+1))*(z*y)
        x = x + y
        k = k + 1

# b) 위의 샘플에 대한 히스토그램을 그리고 위의 Binomial Distribution이 40 이상이 될 확률을 위의 샘플들을 이용해 계산하시오.
# 교수님께서 40으로 진행해도 괜찮다고 하셨지만 30 이상일 경우도 구해보았다.

plt.hist(lgm_random_num, bins = 100, edgecolor = 'black')
plt.show()

print(str(((sum(i >= 40 for i in lgm_random_num)) / 10000) * 100) + "%")

print(str(((sum(i >= 30 for i in lgm_random_num)) / 10000) * 100) + "%")

# c) Binomial 분포의 공식을 이용하여 30 이상이 될 확률을 구하고 (b)의 결과와 비교하시오. 

print("Binomial 분포의 공식을 이용하여 30 이상이 될 확률을 구하였을때 34.17%가 나왔다. 이는 b)에서 구한 결과인 99%와 다소 차이가 크다.")

