"""
[Gold 5] 백준 14719번 빗물

2차원에 블록이 쌓여있음. 비가 오면 블록 사이에 빗물이 고임. 비는 충분히 많이 옴. 고이는 빗물의 총량은?

입력:
    첫째 줄: H W - H: 2차원의 세로 길이, W: 가로 길이 (1 <= H, W <= 500)
    두번째 줄: W개의 블록 높이 정수들 (0 이상 H 이하)
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    arr = list(map(int, input().split()))
    left_max = [0] * W
    right_max = [0] * W
    res = 0

    max_height = 0
    for i in range(W):
        max_height = max(max_height, arr[i])
        left_max[i] = max_height

    max_height = 0
    for i in range(W - 1, -1, -1):
        max_height = max(max_height, arr[i])
        right_max[i] = max_height

    for i in range(W):
        res += min(left_max[i], right_max[i]) - arr[i]

    print(res)


if __name__ == "__main__":

    main()
