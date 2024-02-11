"""
[Gold 5] 백준 17070번 파이프 옮기기 1

크기가 N X N인 새 집, 1 X 1 크기의 정사각형 칸으로 나누어져 있음
각각의 칸은 (r, c)로 나타내어짐 (1부터 시작)

집 수리를 위해 파이프 하나를 옮기려고 함
2개의 연속된 칸을 차지하는 크기
가로 2칸, 세로 두 칸, 대각 2칸 형태 가능
(파이프는 매우 무겁기 때문에 밀어서 이동시키려고 함)
벽지를 새로 해서 벽도 긁으면 안 됨
    -> 파이프는 항상 빈 칸만 차지해야 함
밀 수 있는 방향은 오른쪽, 오른쪽 아래, 아래의 세 방향 뿐

가장 처음에 파이프는 (1, 1)과 (1, 2) 차지, 방향은 가로
    파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구하여라.

입력:
    첫째 줄: N - (3 <= N <= 16) 집의 크기
    ~N개 줄: 집의 상태 - 빈 칸은 0, 벽은 1
            (1,1)과 (1,2)는 항상 빈 칸
출력:
    첫째 줄에 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수 출력
    이동시킬 수 없는 경우에는 0 출력
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N + 1)]
    dp[1][1] = [1, 0, 0]

    for i in range(N):
        for j in range(N):
            if i == j == 0:
                continue
            if mat[i][j] == 0:
                # 가로
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
                # 세로
                dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
                # 대각선
                if mat[i - 1][j] == mat[i][j - 1] == 0:
                    dp[i][j][2] = sum(dp[i - 1][j - 1])
    print(sum(dp[N][N - 1]))


if __name__ == "__main__":
    N = int(input().strip())
    mat = [list(map(int, input().split())) for _ in range(N)]
    main()
