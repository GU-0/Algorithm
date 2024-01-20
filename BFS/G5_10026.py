"""
[Gold 5] 백준 10026번 적록색약

N X N 그리드에 R, G, B 중 하나를 색칠한 그림.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어짐
같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역 (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수 출력

입력: 첫째 줄: N (1 <= N <= 100)
둘째 줄 ~~ : 그림

출력: (일반인 구역 수) (적록색약 구역 수)
"""

"""
bfs로 1,1에서 시작 -> 다른 색 만나면 다른 색으로 탐색 시작 -> 같은 색이면 계속 탐색
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    # Input
    N = int(input().rstrip())
    mat = [list(input().rstrip()) for _ in range(N)]
    #
    a_res, b_res = 0, 0
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False] * N for _ in range(N)]

    #
    def dfs(i, j):
        visited[i][j] = True

        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if (0 <= nr < N) and (0 <= nc < N):
                if (visited[nr][nc] == False) and (mat[nr][nc] == mat[i][j]):
                    dfs(nr, nc)

    #
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                dfs(i, j)
                a_res += 1

    for i in range(N):
        for j in range(N):
            if mat[i][j] == "R":
                mat[i][j] = "G"

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                dfs(i, j)
                b_res += 1

    print(a_res, b_res)
    #


if __name__ == "__main__":
    main()
