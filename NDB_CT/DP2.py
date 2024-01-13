"""
정수 X에 대해 사용할 수 있는 연산은 다음과 같은 4가지
1. X가 5로 나누어 떨어지면 5로 나눔
2. X가 3으로 나누어 떨어지면 3으로 나눔
3. X가 2로 나누어 떨어지면 2로 나눔
4. X에서 1을 뺌

정수 X가 주어졌을 때 연산 4개를 적절히 사용해서 값을 1로 만든다.
연산을 사용하는 횟수의 최솟값은?

입력 첫째 줄: 정수 X (1 <= X <= 30,000)
출력: 연산 횟수 최솟값 출력
"""

# dp dict로 해당 숫자에 대한 연산 횟수 저장

import sys
import time

input = sys.stdin.readline


def main():
    X = int(input().rstrip())

    dp = {1: 0, 2: 1, 3: 1, 4: 2, 5: 1}

    def DP(n):
        res = 1000000
        if n in dp:
            res = dp[n]
            return res

        if n % 5 == 0:
            res = min(res, DP(n // 5) + 1)
        if n % 3 == 0:
            res = min(res, DP(n // 3) + 1)
        if n % 2 == 0:
            res = min(res, DP(n // 2) + 1)
        res = min(res, DP(n - 1) + 1)
        dp[n] = res
        return res

    DP(X)
    print(dp[X])


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"total time: {et - st}")
