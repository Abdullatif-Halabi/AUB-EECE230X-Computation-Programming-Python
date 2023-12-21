import matplotlib.pyplot as plt
from math import log2

N = [n for n in range(2,31)]
Y_all = [ [log2(x) for x in N] , N ,
          [x*log2(x) for x in N] , [x**2 for x in N] ,
          [2**x for x in N] ]
colors = ['r' , 'g' , 'b' , 'k' , 'y']
labels = ['log_2(n)' , 'n' , 'n*log_2(n)' , 'n^2' , '2^n']

plt.figure(figsize=(10,10))

plt.subplot(1,2,1)
for i in range(3):
    plt.plot(N , Y_all[i] , colors[i] , label = labels[i])
plt.yscale('log')
plt.xlabel('n')
plt.title(f'{labels[0]} vs. n vs. {labels[2]}')
plt.legend() 

plt.subplot(1,2,2)
for i in range(2,5):
    plt.plot(N , Y_all[i] , colors[i] , label = labels[i])
plt.yscale('log')
plt.xlabel('n')
plt.title(f'{labels[2]} vs. n^2 vs. 2^n')
plt.legend() 

plt.show()