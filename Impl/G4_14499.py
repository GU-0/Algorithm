"""
[Gold 4] 백준 14499 주사위 굴리기

크기가 N X M인 지도 (오른쪽: 동쪽, 위: 북쪽)
지도의 좌표는 (r, c)로 나타냄 {r: 북쪽으로부터 떨어진 칸의 개수, c: 서쪽으로부터 떨어진 칸의 개수}
주사위의 전개도는
    2
4   1   3
    5
    6
-> 지도 위에 윗면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓여져 있음 (놓여져 있는 곳의 좌표는 (x, y))
    가장 처음 주사위의 모든 면에는 0이 적혀져 있다.

지도의 각 칸에는 정수가 쓰여저 있음
주사위를 굴리고 이동한 칸에 쓰여 있는 수가 0이면 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
                                0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사 -> 칸에 쓰여 있는 수는 0이 됨

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때마다 상단에 쓰여 있는 값을 구하라
(주사위는 지도의 바깥으로 이동 못 함. 바깥으로 이동시키려고 하는 경우 해당 명령을 무시해야 하며 출력도 하면 안 됨)

입력 첫째 줄: N M x y K (1 <= N, M <= 20, 0 <= x <= N-1, 0 <= y <= M-1, 1<= K <= 1,000) K: 명령의 개수
둘째 줄 ~ 각 줄: 지도에 쓰여 있는 수가 북쪽에서 남쪽으로, 각 줄은 서쪽에서 동쪽 순서대로 주어짐
            주사위를 놓은 칸에 쓰여 있는 수는 항상 0
            지도의 각 칸에 쓰여 있는 수는 0~9 정수
마지막 줄: 이동하는 명령 {1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽}

출력: 이동할 때마다 주사위의 윗 면에 쓰여 있는 수 출력 (바깥으로 이동하려는 경우 해당 명령 무시, 출력 X)
"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def roll_dice(d):
    match d:
        case 1:  # 동
            (
                dice["top"],
                dice["bottom"],
                dice["north"],
                dice["south"],
                dice["east"],
                dice["west"],
            ) = (
                dice["west"],
                dice["east"],
                dice["north"],
                dice["south"],
                dice["top"],
                dice["bottom"],
            )
        case 2:  # 서
            (
                dice["top"],
                dice["bottom"],
                dice["north"],
                dice["south"],
                dice["east"],
                dice["west"],
            ) = (
                dice["east"],
                dice["west"],
                dice["north"],
                dice["south"],
                dice["bottom"],
                dice["top"],
            )
        case 3:  # 북
            (
                dice["top"],
                dice["bottom"],
                dice["north"],
                dice["south"],
                dice["east"],
                dice["west"],
            ) = (
                dice["south"],
                dice["north"],
                dice["top"],
                dice["bottom"],
                dice["east"],
                dice["west"],
            )
        case 4:  # 남
            (
                dice["top"],
                dice["bottom"],
                dice["north"],
                dice["south"],
                dice["east"],
                dice["west"],
            ) = (
                dice["north"],
                dice["south"],
                dice["bottom"],
                dice["top"],
                dice["east"],
                dice["west"],
            )


def moving(cmd):
    global x, y
    nx, ny = x + d[cmd][0], y + d[cmd][1]
    if (0 <= nx < N) and (0 <= ny < M):
        roll_dice(cmd)
        if mat[nx][ny] == 0:
            mat[nx][ny] = dice["bottom"]
        else:
            dice["bottom"] = mat[nx][ny]
            mat[nx][ny] = 0
        x, y = nx, ny
        print(dice["top"])


def main():
    for c in cmd:
        moving(c)
    return


if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    cmd = list(map(int, input().split()))
    d = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동서북남
    dice = {"top": 0, "bottom": 0, "north": 0, "south": 0, "east": 0, "west": 0}
    main()
