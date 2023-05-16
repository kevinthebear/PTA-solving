# Q5

import matplotlib.pyplot as plt
import numpy as np

# a) 표준 정규분포 mean = 0, variance = 1의 확률 밀도 함수를 이용하여 밀도 그래프를 그리시오. -4부터 4까지 0.0005 스텝으로 그리시오.

x = np.arange(-4,4,0.0005)
pdf = np.exp(-np.square(x)/2)/(np.sqrt(2*np.pi))

plt.plot(x,pdf)
plt.show()

# b) Q4에서 생성한 그래프와의 차이를 설명하시오.
print("Box-Muller의 경우, independent, normally distributed random numbers를 다루고, Probability density function (PDF)의 경우, continuous random variable을 다룬다. 따라서 Box-Muller의 그래프는 끊어져있는 반면, PDF의 그래프는 연속적으로 이어져 있다는 것을 볼 수 있다. 또한, 두 그래프가 표현하는 바 역시 차이점이 있다. Box-Muller는 정규 분포를 그린 반면에, PDF는 그러한 정규 분포의 밀도를 표현한 그래프임으로, 서로 다른 의미를 내포하고 있다.")