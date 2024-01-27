"""
[Gold 4] 백준 11054번 가장 긴 바이토닉 부분 수열

수열 S가 어떤 수 S_k를 기준으로 S_1 < S_2 < ... < S_k > S_k+1 > ... > S_N을 만족하면 바이토닉 수열이라고 한다.
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구해라.

입력 첫째 줄: 수열 A의 크기 N
둘째 줄: 수열 A를 이루고 있는 A_i (1 <= N <= 1,000, 1 <= A_i <= 1,000)

출력: 수열 A의 부분 수열 중 가장 긴 바이토닉 수열의 길이 출력
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    dp1 = [1] * N
    dp2 = [1] * N

    # LIS 계산
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)

    # LDS 계산
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)

    # 최대 바이토닉 부분 수열 길이 계산
    res = max(dp1[i] + dp2[i] - 1 for i in range(N))

    print(res)


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().split()))
    main()
