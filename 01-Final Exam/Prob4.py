def threeDistinct(L):
    if len(L) < 3:
        return False

    def recThreeDistinct(L, n):
        if n == 3:
            return True

        if len(L) == 1 and n < 3:
            return False

        if L[0] == L[1]:
            return recThreeDistinct(L[1:], n)

        return recThreeDistinct(L[1:], n + 1)

    return recThreeDistinct(L, 1)


# print(threeDistinct([]))
# print(threeDistinct([1]))
# print(threeDistinct([1, 1]))
# print(threeDistinct([1, 10]))
# print(threeDistinct([1, 1, 10]))
# print(threeDistinct([1, 1, 10, 10, 10]))
# print(threeDistinct([1, 1, 3, 10, 10, 10]))
# print(threeDistinct([1, 1, 3, 10, 10, 10, 10, 10, 10]))
# print(threeDistinct([1, 1, 1, 1, 1, 3, 3, 4, 10]))
