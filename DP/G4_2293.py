"""
[Gold 5] 백준 2293번 동전1

n가지 종류의 동전, 각각의 가치는 다름
이 동전을 적당히 사용하여 가치의 합이 k원이 되도록 하는 경우의 수는?
(각각의 동전은 몇 개라도 사용 가능)
(순서 없음)

입력:
    첫째 줄: n, k (1 <= n <= 100, 1 <= k <= 10,000)
    ~ n개 줄: 동전의 가치
출력:
    경우의 수
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    for v in arr:
        for i in range(v, k + 1):
            dp[i] += dp[i - v]
    print(dp[k])


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = sorted([int(input()) for _ in range(n)])
    dp = [0] * (k + 1)
    dp[0] = 1
    main()
