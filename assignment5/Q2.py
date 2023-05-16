# Q2 - ANSI C 의사 난수 생성기를 사용하여 다음을 수행합니다.

# a) 의사 난수 알고리즘을 이용하여 10,000개의 Uniform 분포 수열을 생성

def ansi(m = (2**31), a = 1103515245 , c = 12345):
    global seed
    seed = (a * seed + c) % m
    return seed / m

ansi_random_num = [ansi() for i in range(10000)]

# b) a)의 결과를 이용하여 다음 분포로 10,000개의 샘플 생성

for i, x in enumerate(ansi_random_num):
    if x < 0.3:
        ansi_random_num[i] = -1
    elif x < 0.8:
        ansi_random_num[i] = 0
    else:
        ansi_random_num[i] = 1
