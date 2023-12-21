import matplotlib.pyplot as plt
import numpy.random as rand
from math import pi

def monteCarloPiApproximation(N):
    m =0
    approximatePi = []
    for n in range(1,N+1):
        x = rand.uniform(-1 , 1)
        y = rand.uniform(-1 , 1)
        if x**2 + y**2 <= 1 :
            m += 1
        approximatePi.append(4*m/n)
    return  approximatePi

X = [i for i in range(1 , 10001)]
Y = monteCarloPiApproximation(10000)
Z = [ abs(y - pi) for y in Y ]
plt.figure(figsize=(15,22))
plt.subplot(2 ,1 ,1)
plt.plot(X , Y , 'r' , label = 'approximation')
plt.plot([0 , 10000] , [pi , pi] , 'k' , label = 'p')
plt.xlabel('n')
plt.legend()

plt.subplot(2,1,2)
plt.plot(X , Z , 'k')
plt.ylabel('Absolute value of approximation error')
plt.yscale('log')
plt.xlabel('n')

plt.show()
