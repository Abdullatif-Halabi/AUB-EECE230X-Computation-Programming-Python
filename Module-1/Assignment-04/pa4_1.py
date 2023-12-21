s = input("Enter string: ")
n=len(s)
pal = True
if n>1 :
    for i in range(n//2):
        if  s[i] != s[-1-i]:
            pal = False
            break

if pal:
    print("YES palindrome")   
else:
    print("NOT a palindrome")