def binarySearch(L, k):
    Low = 0
    High = len(L) - 1
    while Low <= High:
        Mid = (Low + High) // 2
        if k == L[Mid]:
            return Mid
        elif k < L[Mid]:
            High = Mid - 1
        else:
            Low = Mid + 1
    return -1


L = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
k = 22
print(binarySearch(L, k))
