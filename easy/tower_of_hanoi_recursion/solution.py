def solution(n=float('-inf')):
    if n == float('-inf'):
        return 0
    if type(n) == str:
        try:
            n = int(n)
        except:
            return 0

    if n < 0:
        return 0
    if n-int(n) == 0:
        return 2**n-1
    return 0
