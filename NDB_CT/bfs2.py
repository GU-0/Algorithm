"""
N X M 크기의 직사각형 미로. 탈출해야 됨
초기 위치는 (1, 1)
출구는 (N, M)
한 번에 한 칸씩 이동 가능
0에는 괴물이 있고, 1에는 없음. 괴물 피해야 됨.
미로는 반드시 탈출할 수 있는 형태.
탈출하기 위해 지나는 최소한의 칸의 수를 구하라. (단, 시작 칸과 마지막 칸을 모두 포함한다.)


입력 첫 줄: N M (4 <= N, M <= 200)
다음 N개 줄: 각각 M개의 정수 (0 or 1, 공백 없이 붙어서 입력으로 제시)
시작 칸과 마지막 칸은 항상 1
"""

import sys

input = sys.stdin.readline
ans = 10000


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

    def bfs(r, c, cnt):
        global ans
        if r == N - 1 and c == M - 1:
            ans = min(ans, cnt)

        arr[r][c] = -1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr == N - 1 and nc == M - 1:
                ans = min(ans, cnt + 1)
                return

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1:
                    bfs(nr, nc, cnt + 1)

    bfs(0, 0, 1)
    print(ans)


if __name__ == "__main__":
    main()
