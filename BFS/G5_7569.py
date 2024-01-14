"""1876ms
[Gold 5] 백준 7569번 토마토
가로 M, 세로 N 크기 박스에 격자 칸으로 토마토, 수직으로 H만큼 쌓아서 보관
익은 토마토의 인접한 익지 않은 토마토는 하루가 지나면 익음. (상하좌우전후 6방향, 대각선 X), 혼자서는 못 익음
일부 칸에는 토마토가 없을 수도 있음
모든 토마토가 익는 최소 일수?

첫째 줄: M, N, H (가로, 세로, 상자의 수) (2 <= M, N <= 100, 1 <= H <= 100)
그 다음 N줄씩: 상자 1개씩의 정보
[1은 익은 토마토, 0은 익지 않은 토마토, -1은 들어 있지 않은 칸]
입력은 토마토가 하나 이상 있는 경우로만 주어짐.

출력: 모두 익지 못하는 상황이면 -1
    or 다 익는 최소 일수
"""

import sys
from collections import deque

input = sys.stdin.readline


def main():
    m, n, h = map(int, input().split())
    mat = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    # mat[h][n][m]
    queue = deque()
    # 상하좌우전후
    dx, dy, dz = [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 1, -1], [1, -1, 0, 0, 0, 0]
    ans = -1
    tmp = 0

    # O(m * n * k)
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 1:
                    tmp += 1
                    queue.append((i, j, k))
                elif mat[i][j][k] == -1:
                    tmp += 1

    # 모두 익은 토마토인 경우
    if tmp == m * n * h:
        print(0)
        exit()

    # 익은 토마토가 존재하지 않는 경우 바로 종료
    # if len(queue) == 0:
    #     print(-1)
    #     exit()

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if mat[nz][ny][nx] == 0:
                    mat[nz][ny][nx] = mat[z][y][x] + 1
                    queue.append((nz, ny, nx))
                    ans = max(ans, mat[nz][ny][nx])

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if mat[i][j][k] == 0:
                    print(-1)
                    exit()
                ans = max(ans, mat[i][j][k])
    print(ans - 1)


if __name__ == "__main__":
    main()
