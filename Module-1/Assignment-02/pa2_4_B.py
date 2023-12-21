##PART B
n=int(input("Enter an integer n : "))
if n < 0 :
    print(n , "is not a square")

elif n==0 or n==1 :
    print("YES square: " , n , "=" ,n, "^2")
    
else :
    square = False
    low = 2
    high = n
    
    while high-low > 1 :
        mid = (low+high)//2 
        if mid*mid == n :
            square = True
            break
        
        elif mid*mid > n :
            high = mid
            
        else : 
            low = mid
        
        
    if square:
        print("YES square: " , n , "=" ,mid, "^2")
        
    else:
        print(n,"is not a square")