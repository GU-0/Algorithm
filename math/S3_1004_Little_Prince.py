""" 
[Silver 3] 백준 1004번: 어린 왕자

입력 첫 줄: 테스트 케이스 개수 T
각 테스트 케이스 첫 줄: x1, y1, x2, y2 <- 출발점, 도착점
각 테스트 케이스 둘째 줄: 행성계의 개수 n
각 테스트 케이스 세 번째 줄 ~ n 번째 줄: 행성계의 중점과 반지름 (c_k, c_y, r)

어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수?
(행성계의 경계가 맞닿거나 서로 교차하는 경우, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우는 주어지지 않음.)
"""

""" Solution
(출발 지점을 포함하는 행성계의 개수) + (도착 지점을 포함하는 행성계의 개수) - (출발 지점과 도착 지점을 모두 포함하는 행성계의 개수)

각각의 행성계를 입력으로 받으면서,
출발 지점과 도착 지점 중 하나만 해당 행성계의 내부에 있다면 +1
출발 지점과 도착 지점 모두 해당 행성계의 내부에 있다면 +0
이외의 경우는 모두 +0
"""


import sys


def min_path():
    min_count = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        c_x, c_y, r = map(int, sys.stdin.readline().split())
        bool_start_isin = isin_circle(x1, y1, c_x, c_y, r)
        bool_end_isin = isin_circle(x2, y2, c_x, c_y, r)

        if bool_start_isin ^ bool_end_isin:
            min_count += 1

    print(min_count)


def isin_circle(x, y, c_x, c_y, r):
    return (x - c_x) ** 2 + (y - c_y) ** 2 < r**2


def main():
    T = int(sys.stdin.readline().strip())
    answer = 0

    for _ in range(T):
        min_path()


if __name__ == "__main__":
    main()
