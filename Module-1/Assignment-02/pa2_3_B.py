#PART B
x= int(input("Enter x : "))

if x <= 1 :
    print("x should be greater or equal to 2")
    
else :
    y=0
    
    for n in range(2,x+1):
        isPrime = True
        d = 2 
        while d**2 <= n:
            
            if n%d == 0 :
                isPrime = False
                break
            d+=1
        if isPrime :
            y+=1
            
print("Fraction of primes less than or equal to",x,":", y/x)      