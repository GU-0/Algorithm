"""76ms
[Silver 1] 백준 2178번 미로 탐색

N X M 배열로 표현되는 미로
1: 이동할 수 있는 칸
0: 이동할 수 없는 칸
(1,1)에서 출발하여 (N, M) 위치로 이동할 때 지나야 하는 최소의 칸 수 구하기

입력: 두 정수 \n 배열 (2 <= N, M <= 100)
    -> 배열의 각 수는 붙어서 입력으로 주어진다.
출력: 지나야 하는 최소 칸 수 출력
"""

import sys
from collections import deque

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    mat = [[int(i) for i in input().rstrip()] for _ in range(N)]
    queue = deque()
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    ans = 1e9

    queue.append((0, 0))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr == N - 1 and nc == M - 1:
                ans = min(ans, mat[r][c] + 1)
            elif 0 <= nr < N and 0 <= nc < M and mat[nr][nc] == 1:
                queue.append((nr, nc))
                mat[nr][nc] = mat[r][c] + 1
            else:
                pass
    print(ans)


if __name__ == "__main__":
    main()
