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