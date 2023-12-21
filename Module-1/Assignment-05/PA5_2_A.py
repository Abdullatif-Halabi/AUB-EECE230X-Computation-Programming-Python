import matplotlib.pyplot as plt
from math import log2

N = [n for n in range(2,31)]
plt.figure(figsize=(11 ,25))
for i in range(1,6):
    plt.subplot(3,2,i)
    if i==1:
        Y = [log2(x) for x in N]
        col = 'r'
        plt.ylabel('log_2(n)')
        plt.title('Logarithmic Growth')
    elif i==2:
        Y = N
        col = 'g'
        plt.ylabel('n')
        plt.title('Linear Growth')
    elif i==3:
        Y = [x*log2(x) for x in N]
        col = 'b'
        plt.ylabel('n*log_2(n)')
        plt.title('Loglinear Growth')
    elif i==4:
        Y = [x**2 for x in N]
        col = 'k'
        plt.ylabel('n^2')
        plt.title('Quadratic Growth')
    else:
        Y = [2**x for x in N]
        col = 'y'
        plt.ylabel('2^n')
        plt.title('Exponential Growth')

    plt.plot(N,Y,col)
    plt.xlabel('n')
plt.show()