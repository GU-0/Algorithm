"""
[Gold 4] 백준 3190번 뱀

'Dummy" 라는 도스게임에서, 뱀이 나와서 기어다니는데 사과를 먹으면 뱀 길이가 늘어난다.
뱀은 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다.

게임은 N X N 정사각 보드 위에서 진행, 몇몇 칸에는 사과 놓여져 있음
보드의 상하좌우 끝에는 벽

게임 시작 시 뱀은 최상단 좌측에 위치, 길이는 1, 오른쪽 향함

뱀은 매 초마다 이동.
이동 규칙:
    - 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킴
    - 벽이나 자기 자신의 몸과 부딪히면 게임 끝
    - 이동한 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
    - 이동한 칸에 사과가 없다면 몸 길이를 줄여서 꼬리가 위치한 칸을 비워줌 <- 몸 길이는 변하지 않음

사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 구하여라

입력:
    첫째 줄: N - 보드의 크기 (2 <= N <= 100)
    둘째 줄: K - 사과의 개수 (0 <= K <= 100)
    ~K개의 줄: r c -  사과의 위치 (행, 열, 각 사과의 위치는 모두 다름. 1행 1열에는 사과가 없음)
    다음 줄: L - 뱀의 방향 변환 횟수 (1 <= L <= 100)
    ~L개의 줄: X C - 방향 변환 정보 (게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽('L') 또는 오른쪽 ('D')으로 회전함) (X <= 10,000인 정수)
                    (X가 증가하는 순으로 주어짐)

출력:
    게임이 몇 초에 끝나는지

"""

import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    global dir, loc

    cmd = cmds_queue.popleft()
    time = 1
    while True:
        nr, nc = loc[0] + dirs[dir][0], loc[1] + dirs[dir][1]
        if (nr < 0) or (nr >= N) or (nc < 0) or (nc >= N):  # 벽에 부딪힐 경우
            break
        elif mat[nr][nc] == 1:  # 자신의 몸과 부딪힐 경우
            break

        if mat[nr][nc] == 2:  # 사과일 경우
            mat[nr][nc] = 1
        else:
            mat[nr][nc] = 1
            tmp = loc_history.popleft()
            mat[tmp[0]][tmp[1]] = 0  # 꼬리 자리 비워서 몸 길이 유지
        loc_history.append((nr, nc))
        loc = [nr, nc]

        if time == cmd[0]:  # 명령에 따른 방향 전환
            match cmd[1]:
                case "L":
                    dir = (dir - 1) % 4
                case "D":
                    dir = (dir + 1) % 4
            cmd = cmds_queue.popleft()

        time += 1
    print(time)


if __name__ == "__main__":
    N = int(input().strip())
    mat = [[0] * N for _ in range(N)]  # N X N matrix
    mat[0][0] = 1  # 뱀이 있는 곳을 1로 설정

    K = int(input().strip())
    apple_loc = [tuple(map(int, input().split())) for _ in range(K)]
    for apple in apple_loc:
        mat[apple[0] - 1][apple[1] - 1] = 2  # 사과가 있는 곳을 2로 설정

    L = int(input().strip())
    cmds_queue = deque()  # 명령 모음은 queue 사용
    for _ in range(L):
        num, char = input().split()
        cmds_queue.append((int(num), char))
    cmds_queue.append((10e9, "X"))  # empty queue로 인한 에러 방지용

    loc = [0, 0]
    loc_history = deque()
    loc_history.append((0, 0))

    len = 1
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌 (시계방향)
    dir = 1
    main()
