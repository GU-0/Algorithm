"""
[Gold 3] 백준 2252번 줄 세우기

N명의 학생들을 키 순서대로 줄을 세운다.
일부 학생 두명 사이의 키만 비교했을 때, 줄을 세우는 프로그램을 작성해라.

입력:
    첫째 줄: N M - N(1 <= N <= 32,000) M(1 <= M <= 100,000)
    N: 학생들의 번호는 1~N번
    M: 키를 비교한 횟수 

출력:
    학생들을 앞에서부터 줄을 세운 결과 출력, 답이 여러가지이면 아무거나 출력
"""

import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    for i in range(1, N + 1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        tmp = queue.popleft()
        ans.append(tmp)

        for k in graph[tmp]:
            inDegree[k] -= 1
            if inDegree[k] == 0:
                queue.append(k)

    print(*ans)


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    inDegree = [0] * (N + 1)
    queue = deque()
    ans = []
    main()
