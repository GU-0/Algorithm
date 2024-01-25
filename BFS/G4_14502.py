"""2616ms
[Gold 4] 백준 14502번 연구소

연구소는 N X M 직사각형
연구소는 빈 칸, 벽으로 이루어져 있다. (벽은 칸 하나를 가득 차지)
일부 칸은 바이러스 존재. (상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.)
새로 세울 수 있는 벽의 개수: 3개 (꼭 3개 다 세워야 함)

입력 첫째 줄: N M (3 <= N, M <= 8)
둘째 줄 ~ 지도 모양 (0: 빈 칸, 1: 벽, 2: 바이러스) [2의 개수는 2 이상 10 이하, 빈 칸의 개수는 3개 이상]

출력: 얻을 수 있는 안전 영역의 최대 크기
"""

import sys
from collections import deque
from copy import deepcopy
from itertools import combinations as comb

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def bfs(walls):
    global res
    mat_b = deepcopy(mat)
    tmp = 0
    queue = deque()

    for r, c in walls:
        mat_b[r][c] = 1

    for r, c in virus_arr:
        queue.append((r, c))
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and mat_b[nr][nc] == 0:
                mat_b[nr][nc] = 2
                queue.append((nr, nc))

    for i in range(N):
        for j in range(M):
            if mat_b[i][j] == 0:
                tmp += 1
    res = max(res, tmp)


def main():
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2:
                virus_arr.append((i, j))
            elif mat[i][j] == 0:
                empty_arr.append((i, j))
    wall_cases = list(comb(empty_arr, 3))
    for walls in wall_cases:
        bfs(walls)

    print(res)


if __name__ == "__main__":
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    res = 0
    empty_arr = []
    virus_arr = []
    main()
