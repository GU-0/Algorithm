"""44ms
[Gold 5] 백준 1174번 줄어드는 수

자연수를 십진법으로 표기했을 때, 왼쪽에서부터 자리수가 감소하면 그 수를 '줄어드는 수'라고 한다.
ex) 321, 950은 줄어드는 수, 322, 958은 아님

첫째 줄에 1,000,000 이하의 자연수 N이 주어질 때, N번째 작은 줄어드는 수를 출력한다.
"""

import sys

input = sys.stdin.readline

N = int(input())


# 백트래킹을 이용한 문제 풀이
def bt(cur):
    ans.append(int(cur))
    for j in range(0, int(cur[-1])):  # 현재 숫자의 끝자리보다 낮은 숫자들만 그 다음 자리수에 추가
        bt(cur + str(j))


if N > 1023:  # 9876543210: 1023번째
    print(-1)
else:
    ans = []
    for i in range(10):  # 맨 앞자리가 0, 1, ,... , 9
        bt(str(i))

    print(sorted(ans)[N - 1])
