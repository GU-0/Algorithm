"""
마을에는 여러 개의 식량창고 있음. 일직선으로 이어져서.
각 식량창고에는 정해진 수의 식량 저장, 적은 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정.
정찰병은 인접한 식량창고가 공격받으면 알아챌 수 있음
따라서 최소한 한 칸 이상 떨어진 창고를 약탈해야 함

입력 첫 줄: 식량창고 개수 N (3 <= N <= 100)
둘째 줄에 공백 기준 각 식량창고 식량 개수 K 주어짐 (0 <= K <= 1,000)

출력: 얻을 수 있는 식량 최댓값
"""

"""
i번째 창고를 공격했을 경우의 정보에서, i+1, i+2번째 까지 나아가며 dp 전개
a_n+2 = max(a_n + arr[n+2], a_n+1) (n번째 공격 후 n+2번째 공격 or n+1번째 공격 후 n+2번째 공격X)
"""

import sys
import time


input = sys.stdin.readline


def main():
    N = int(input().strip())
    arr = list(map(int, input().split()))

    # 재귀보다 dp가 훨씬 빠름
    # def dp(n):
    #     if n == 0:
    #         return arr[0]
    #     elif n == 1:
    #         return max(arr[0], arr[1])
    #     else:
    #         return max(dp(n - 2) + arr[n], dp(n - 1))

    # ans = dp(N - 1)
    # print(ans)

    d = [0] * 100

    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, N):
        d[i] = max(d[i - 11], d[i - 2] + arr[i])
    print(d[N - 1])


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(f"total time: {et - st}")
