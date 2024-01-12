"""
[Gold 5] 백준 7576번 토마토

토마토는 가로 M, 세로 N 크기의 격자 모양 상자의 칸에 하나씩 넣어 창고에 보관한다.
보관 후 하루가 지나면 익은 토마토들에 인접한 익지 않은 토마토들은 익게 된다. (상하좌우 네 방향, 대각선X, 혼자서는 못 익음)

며칠이 지나야 창고에 보관된 토마토들이 다 익게 되는지 최소 일수?
"""
"""
2 <= M, M <= 1,000

입력 첫 줄: M, N (M: 가로, N: 세로)
둘째 줄부터 N개의 줄: 토마토의 정보 <- 1은 익음, 0은 안 익음, -1은 안 들어있음
토마토가 아예 없는 경우는 입력으로 주어지지 않음
"""

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1  # 현재 좌표 횟수에서 1 더하면서 나아가기
                queue.append([nx, ny])


###
bfs()
for row in mat:
    for e in row:
        if e == 0:
            print(-1)
            exit()
    ans = max(ans, max(row))

print(ans - 1)
