"""460ms
[Gold 5] 백준 15686번 치킨배달
***문제 설명***
크기가 N X N인 도시.
도시는 1 X 1 크기의 칸으로 나누어져 있음.
각 칸은 [빈 칸, 치킨집, 집] 중 하나
도시의 칸은 (r, c)의 형태로 표현

def 치킨 거리 -> 집과 가장 가까운 치킨집 사이의 거리
    도시의 치킨 거리 -> 모든 집의 치킨 거리의 합

임의의 두 칸 [(r1, c1), (r2, c2)]사이의 거리 = |r1 - r2| + |c1 - c2|

도시의 치킨집은 모두 같은 프렌차이즈인데, 본사는 수익 증진을 위해 일부 치킨집을 폐업할 예정
도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수: 최대 M개
도시의 치킨집 중 최대 M 개를 고르고 나머지 치킨빕은 모두 폐업시켜야 함.
도시의 치킨 거리가 가장 작게 되도록 M을 구해라.

입력 첫 줄: N M (2 <= N <= 50, 1 <= M <= 13)
둘째 줄~N개 줄: 도시 정보 mat {0: 빈 칸, 1: 집, 2: 치킨집}
(1 <= 집의 개수 < 2N) (M <= 치킨집 개수 <= 13)
"""

"""
여기서 거리 구하는 방식은 "칸 차이"
"""

import sys
from itertools import combinations as comb

input = sys.stdin.readline


def get_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def main():
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    res = 1e9
    ch_list = []
    home_list = []

    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                ch_list.append([i, j])
            elif mat[i][j] == 1:
                home_list.append([i, j])

    ch_comb = list(comb(ch_list, M))

    for ch in ch_comb:
        dis = []
        for h in home_list:
            tmp = 1e9
            for i in range(M):
                dr, dc = ch[i][0], ch[i][1]
                tmp = min(tmp, get_distance(h[0], h[1], dr, dc))
            dis.append(tmp)
        res = min(res, sum(dis))

    print(res)


if __name__ == "__main__":
    main()
