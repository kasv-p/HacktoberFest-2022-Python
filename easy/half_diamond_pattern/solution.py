def solution(n=float('-inf')):
    if n == 0 or n == 1 or n < 0:
        return -1
    if n == float('-inf'):
        return -1
    N = n//2+1
    res = ''
    for i in range(N):

        for j in range(0, i + 1):
            res += '*'
        res += '\n'

    # Loop to print the lower half
    # diamond pattern
    for i in range(1, N):

        for j in range(i, N):
            # print("*", end="")
            res += '*'
        res += '\n'
    return res[:-1]
