"""[Gold 4]백준 14500: 테트로미노 => 4504ms
폴리오미노: 크기가 1 X 1인 정사각형을 여러 개 이어 붙인 도형
    조건:
        - 정사각형은 서로 겹치면 안 된다.
        - 도형은 모두 연결되어 있어야 한다.
        - 정사각형의 변끼리 연결되어 있어야 한다. (꼭짓점끼리 맞닿아 있으면 안 된다.)

테트로미노: 정사각형 4개를 이어 붙인 폴리오미노
    - 형태는 5가지가 있다.

문제: 크기가 N X M인 종이 위에 테트로미노 하나를 놓는다.
    종이는 1 X 1 큼기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
    테트로미노 하나를 적절히 놓아 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 코드 작성 (최전, 대칭 가능)
"""

"""
첫째 줄: 종이의 세로 크기 N, 가로 크기 M (4 ≦ N, M ≦ 500)
둘째 줄 ~ : 각 칸에 해당하는 수
(입력으로 주어지는 수들은 1,000 미만 자연수)
"""

"""
배열을 만들고, 하나의 칸에서 인접한 칸으로 4칸까지 뻗어나감.
뻗어나간 네 칸 경우들 중에 합이 가장 큰 경우 채택. <- dfs 사용
"""

import sys

input = sys.stdin.readline

# 방문한 좌표 visited 리스트에 있는지 확인하는 방법 or visited matrix 만들어서 T/F 판별 둘 다 해보기


def dfs(x, y, total, cnt):
    global maxValue
    if maxValue >= total + maxValue * (4 - cnt):
        return

    if cnt == 4:
        maxValue = max(maxValue, total)
        return

    for i, j in move:
        nx = x + i
        ny = y + j

        if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0):
            visited[nx][ny] = 1
            dfs(nx, ny, total + mat[nx][ny], cnt + 1)
            visited[nx][ny] = 0


# 예외 ㅏㅓㅜㅗ 모양. 현재 좌표를 중심으로 상하좌우 숫자 모두 구한 후 가장 작은 숫자를 뺀다.
def exce(x, y):
    global maxValue
    if maxValue >= mat[x][y] + maxValue * 3:
        return

    no_cnt = 0
    temp_min = 1001
    temp_sum = mat[x][y]

    for i, j in move:
        nx = x + i
        ny = y + j

        if not ((0 <= nx < N) and (0 <= ny < M)):  # 현재 좌표가 edge일 경우
            no_cnt += 1
            if no_cnt >= 2:  # 현재 좌표가 꼭짓점일 경우 해당 모양 형성 불가능
                continue
        else:
            temp_min = min(temp_min, mat[nx][ny])
            temp_sum += mat[nx][ny]
    if no_cnt == 1:  # 현재 좌표 edge일 경우 4개 합 그대로
        maxValue = max(maxValue, temp_sum)
    else:
        maxValue = max(maxValue, temp_sum - temp_min)


### MAIN ###
if __name__ == "__main__":
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우 움직임
    maxValue = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = 1
            dfs(i, j, mat[i][j], 1)
            visited[i][j] = 0

            exce(i, j)

    print(maxValue)
