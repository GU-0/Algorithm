"""40ms
[Gold 5] 백준 2668번 숫자고르기

2 X N 형태의 표
첫째 줄에는 1, 2, ... , N
둘째 줄 각 칸에는 1 이상 N 이하 정수들

첫째 줄에서 숫자를 적절히 뽑으면, 그 정수들이 이루는 집합과 해당 칸 둘째 줄에 있는 정수들이 이루는 집합이 일치하도록 정수를 뽑는다.
이 방식으로 뽑되, 최대한 많은 수를 뽑아야 한다.
"""

"""
입력의 첫 줄은 N
둘째 줄부터는 표의 둘째 줄에 들어가는 정수들이 한 줄에 하나씩 입력

=> 첫째 줄에 뽑힌 정수들의 개수 출력, 다음 줄부터는 뽑힌 정수들을 오름차순으로 한 줄에 하나씩 출력
"""
# dfs로 탐색, 순환 발생 시 ans 리스트에 추가

import sys

input = sys.stdin.readline


def dfs(i):
    if visited[i] == False:
        visited[i] = True

        set_up.add(i)
        set_down.add(arr[i])

        if set_up == set_down:
            ans.extend(list(set_down))
            return
        dfs(arr[i])

    visited[i] = False


n = int(input())
arr = [-1]
for _ in range(n):
    arr.append(int(input()))
visited = [False] * (n + 1)
ans = []

for i in range(1, n + 1):
    set_up = set()
    set_down = set()

    dfs(i)
ans = sorted(list(set(ans)))

print(len(ans))
for n in ans:
    print(n)
