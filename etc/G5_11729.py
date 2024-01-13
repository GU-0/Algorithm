"""896ms
[Gold 5] 백준 11729번 하노이 탑 이동 순서

1. 한 번에 한 개의 원판만 옮길 수 있음
2. 쌓아 놓은 원판은 항상 위가 아래보다 작아야 함.

이 작업을 수행하는데 필요한 이동 순서를 출력해라. (이동 횟수는 최소)

입력 첫째 줄: 원판의 개수 (1 <= N <= 20)
출력 첫째 줄: 옮긴 횟수 K
두번째 줄부터 수행 과정
"""

import sys

input = sys.stdin.readline


def main():
    def hanoi(n, start, end):
        if n == 1:
            print(start, end)
            return
        else:
            oth = 6 - start - end
            hanoi(n - 1, start, oth)
            print(start, end)
            hanoi(n - 1, oth, end)

    N = int(input().rstrip())

    print(2**N - 1)
    hanoi(N, 1, 3)


if __name__ == "__main__":
    main()
