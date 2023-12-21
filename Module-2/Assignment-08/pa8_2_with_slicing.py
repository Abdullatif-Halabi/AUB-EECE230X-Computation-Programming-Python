# def isPalindrome(s): # Wrapper function

#     if len(s) in (0,1) : return True       #First base case

#     def isPalindromeRec(s,low,high):
#         """ Recursive function which checks if substring s[low ... high] is palindrome
#         returns a True/False value"""
#         mid = (low + high)//2
#         if len(s) %2 == 0  :
#             left = s[low:mid+1]
#             right = s[mid+1:high+1]
#         else :
#             left = s[low:mid]
#             right = s[mid+1:high+1]

#         if len(left) == 1 :   #Second base case ..(or len(right) > 1 cz they will always have the same length) 
#             return left == right       
        
#         elif s[low] != s[high]:    #Third base case        
#             return False
        
#         else:
#             return isPalindromeRec(s,low+1 , high-1)
#     n = len(s)
#     return isPalindromeRec(s,0,n-1)

#############################################

def isPalindrome(s):
    def isPalindromeRec(s, low, high):
        if low >= high:
            return True
        if s[low] != s[high]:
            return False
        return isPalindromeRec(s, low + 1, high - 1)

    n = len(s)
    return isPalindromeRec(s, 0, n-1)

# Test cases
print(isPalindrome("anna"))
print(isPalindrome("civic"))
print(isPalindrome("a"))
print(isPalindrome("tx1aa1xt"))
print(isPalindrome(""))
print(isPalindrome("Civic"))
print(isPalindrome("ab"))



#########################################################

# def isPalindrome(s): # Wrapper function
#     def isPalindromeRec(s,low,high):
#         """ Recursive function which checks if substring s[low ... high] is palindrome
#         returns a True/False value"""
#         if len(s)%2 == 0 :
#             if s[low] != s[high] : return False
#             elif high-low+1 > 2:
#                 return isPalindromeRec(s, low+1 , high-1) 
#             else :
#                 return s[low] == s[high]  #Second base case
#         else :
#             if s[low] != s[high] : return False
#             elif high-low+1 > 3:
#                 return isPalindromeRec(s, low+1 , high-1)
#             else :
#                 return s[low] == s[high]   #Third base case


#     n = len(s)
#     if n in (0,1) : return True #First base case
#     return isPalindromeRec(s,0,n-1)


# print(isPalindrome("anna"))
# print(isPalindrome("civic"))
# print(isPalindrome("a"))
# print(isPalindrome("tx1aa1xt"))
# print(isPalindrome(""))
# print(isPalindrome("Civic"))
# print(isPalindrome("ab"))

# print('C' == 'c')