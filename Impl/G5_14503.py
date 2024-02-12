"""44ms
[Gold 5] 백준 14503번 로봇 청소기

N X M 크기의 직사각형 방. (1 X 1 크기의 정사각형 칸으로 나누어져 있음)
청소기는 동, 서, 남, 북 중 하나의 방향을 바라봄. (r, c)

로봇 청소기 동작 메커니즘
1. 현재 칸이 청소되지 않은 경우, 현재 칸을 청소
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    - 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아감
    - 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    - 반시계 방향으로 90도 회전
    - 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
    3. 1번으로 돌아감

입력 첫째 줄: N M (3 <= N, M <= 50)
    둘째 줄: 로봇 청소기가 있는 칸의 좌표 (r, c), 바라보는 방향 d {0: 북, 1: 동, 2: 남, 3: 서}
    셋째 줄~: 각 칸의 상태 나타내는 칸 (0: 청소되지 않은 빈 칸, 1: 벽)

출력: 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수
"""


import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    def cleaning():
        global res
        if mat[cr][cc] == 0:
            mat[cr][cc] = -1  # case 1
            res += 1
        moving()

    def moving():
        global cr, cc, cd
        no_cnt = 0
        for i in range(1, 5):
            cd = (cd + 3) % 4  # case 3-1
            nr, nc = cr + dr[cd], cc + dc[cd]
            if mat[nr][nc] == 0:  # case 3
                cr, cc = nr, nc  # case 3-2
                cleaning()  # case 3-3
            else:
                no_cnt += 1
        if no_cnt == 4:
            nd = (cd + 2) % 4  # 바라보는 반대 방향
            nr, nc = cr + dr[nd], cc + dc[nd]
            if mat[nr][nc] == 1:  # case 2-2
                return
            else:
                cr, cc = nr, nc
                cleaning()

    cleaning()
    print(res)


if __name__ == "__main__":
    #
    N, M = map(int, input().split())
    cr, cc, cd = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    #
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북동남서
    res = 0

    main()
