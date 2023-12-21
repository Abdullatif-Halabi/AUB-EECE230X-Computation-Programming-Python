def isPalindrome(s):
    def isPalindromeRec(s, low, high):
        if low >= high:  #First base case
            return True
        if s[low] != s[high]:  #Second base case
            return False
        return isPalindromeRec(s, low + 1, high - 1)  # Conquering ...

    n = len(s)
    return isPalindromeRec(s, 0, n-1)


# print(isPalindrome("anna"))
# print(isPalindrome("civic"))
# print(isPalindrome("a"))
# print(isPalindrome("tx1aa1xt"))
# print(isPalindrome(""))
# print(isPalindrome("Civic"))
# print(isPalindrome("ab"))