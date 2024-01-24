"""
[Gold 4] 백준 9663번 N-Queen
N-Queen 문제는 크기가 N X N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
N이 주어졌을 때 퀸을 놓는 방법의 수를 구하여라.

입력 첫째 줄: N (1 <= N < 15)
"""

"""
배열: N X N
k와 같은 열: (i * n + k)
k와 같은 행: (~~~)
k의 대각선: ()
"""
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


N = int(input().rstrip())
res = 0
arr = [0] * N


def is_not_attackable(x):
    for i in range(x):
        if arr[x] == arr[i] or x - i == abs(arr[i] - arr[x]):
            return False
    return True


def queen(x):
    global res
    if x == N:
        res += 1
        return
    else:
        for i in range(N):
            arr[x] = i
            if is_not_attackable(x):
                queen(x + 1)


queen(0)
print(res)
