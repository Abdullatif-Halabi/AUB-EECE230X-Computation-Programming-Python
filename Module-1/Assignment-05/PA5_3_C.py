import matplotlib.pyplot as plt
from math import log

def generatePrimes(n):
    P = []
    B = [False] * (n)

    if n <= 2:
        return (P, B)

    B[2] = True

    for i in range(3, n, 2):
        B[i] = True

    for i in range(3, int(n**0.5) + 1, 2):
        if B[i]:
            for j in range(i*i, n, 2*i):
                B[j] = False

    P = [i for i, is_prime in enumerate(B) if is_prime and i >= 2]

    return (P, B)


def primesCount(n):
    (P , B) = generatePrimes(n)
    y = []
    primes = 0
    for i in range(len(B)):
        if B[i] :
            primes += 1
        y.append(primes)

    return y


X = [i for i in range(200)]
Y = [y for y in primesCount(200) ]
Z = [i/log(i) for i in range(2,200)]


plt.figure(figsize=(5 , 5))
plt.plot(X , Y , 'r' , label = 'pi(i)')
plt.plot(X[2:] , Z , 'k' , label = 'i/log(i)')
plt.xlabel('i')
plt.title('Density of primes')
plt.legend()
plt.show()
