""" 44ms
[Gold 5] 백준 2225번 합분해

0부터 N 까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하기
(덧셈의 순서가 바뀐 경우는 다른 경우, 한 개의 수 여러 번 사용 가능)

첫째 줄에 두 정수 N, K 주어짐 (1 <= N, K <= 200)
답을 1,000,000,000으로 나눈 나머지 출력
"""

"""
(0 ~ N) 까지 서로 다른 (N+1)개에 파티션 (K-1)개
-> 범위에 0도 포함되므로 파티션 위치는 중복 허용
-> (N+1)H(K-1) = (N+K-1)C(K-1)

=> Combination 공식으로 factorial을 통해 답 구하면 overflow로 답 안 나옴.
    => 반복문으로 약분된 공식 사용
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

tmp1 = 1
tmp2 = 1

# (N+K-1)C(K-1) 계산
for n in range(N + K - 1, N, -1):
    tmp1 *= n
    tmp2 *= n - N

print(tmp1 // tmp2 % 1000000000)
