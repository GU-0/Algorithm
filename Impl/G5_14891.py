"""
[Gold 5] 백준 14891번 톱니바퀴

총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 일렬로 놓여 있음
각 톱니는 N극 또는 S극 중 하나를 나타냄
톱니바퀴에는 번호 존재
가장 왼쪽부터 1, 2, 3, 4번

톱니바퀴를 총 K번 회전시키려 한다. (회전은 한 칸을 기준)
    -> 회전은 시계 방향 or 반시계 방향
톱니를 회전시키려면 '회전시킬 톱니바퀴'와 '회전시킬 방향'을 결정해야 함

톱니가 회전할 때, 서로 맞닿은 극에 따라 옆에 있는 톱니바퀴 회전 가능
-> 톱니바퀴 A 회전할 때, 그 옆 톱니바퀴 B와 맞닿은 톱니의 극이 다르면 B는 A 회전의 반대방향으로 회전

입력:
    1~4번째 줄: 각각 i번 톱니바퀴의 상태
        상태는 8개의 정수 (N극은 0, S극은 1)
    다섯째 줄: 회전 횟수 K (1 <= K <= 100)
    다음 K개 줄: 회전시킨 방법
        -> 두 개의 정수로 이루어져 있음
            첫번째 정수: 회전시킨 톱니바퀴 번호
            두번째 정수: 방향 (1: 시계, -1: 반시계)

"""

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def rotate_wheel(n, d):
    prev_n = n - 1
    next_n = n + 1

    if 1 <= prev_n <= 4:
        if (wheels[n][-2] != wheels[prev_n][2]) and visited[prev_n] == 0:
            visited[prev_n] = 1
            rotate_wheel(prev_n, -d)
            visited[prev_n] = 0
    if 1 <= next_n <= 4:
        if (wheels[n][2] != wheels[next_n][-2]) and visited[next_n] == 0:
            visited[next_n] = 1
            rotate_wheel(next_n, -d)
            visited[next_n] = 0

    if d == 1:
        wheels[n] = [wheels[n][-1]] + wheels[n][:-1]
    elif d == -1:
        wheels[n] = wheels[n][1:] + [wheels[n][0]]

    return


def main():
    for c in cmd:
        visited[c[0]] = 1
        rotate_wheel(c[0], c[1])
        visited[c[0]] = 0
    print(wheels[1][0] + wheels[2][0] * 2 + wheels[3][0] * 4 + wheels[4][0] * 8)


if __name__ == "__main__":
    wheels = {i: list(map(int, input().strip())) for i in range(1, 5)}
    k = int(input())
    cmd = [list(map(int, input().split())) for _ in range(k)]
    visited = [0, 0, 0, 0, 0]
    main()
