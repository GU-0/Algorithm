"""
[Gold 4] 백준 1922번 네트워크 연결

컴퓨터와 컴퓨터를 모두 연결하는 네트워크 구축하려는 상황
허브가 없음. 컴퓨터와 컴퓨터 직접 연결해야 하는데, 모든 컴퓨터가 연결이 되어 있어야 함

각 컴퓨터를 연결하는 데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용 출력해라

입력:
    첫째 줄: N - 컴퓨터의 수 (1 <= N <= 1,000)
    둘째 줄: M - 연결할 수 있는 선의 수 (1 <= M <= 100,000)
    ~M개 줄: a b c - 각 컴퓨터를 연결하는 데 드는 비용들. a와 b 컴퓨터를 연결하는 비용은 c (1 <= c <= 10,000)
        a와 b는 같을 수도 있음
출력:
    모든 컴퓨터를 연결하는데 필요한 최소비용 출력
"""

"""
간선이 많기 때문에 Prim 알고리즘 사용
-> 다 풀고 비교했는데 Kruskal이 더 빠름. 간선이 많아서 Prim이 적합한 줄 알았는데 이 문제는 간선이 많지 않은 편에 속하거나 다른 이유가 있는 듯
"""

import sys
import heapq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def prim(graph, start):
    visited = [False] * (N + 1)
    queue = [(0, start)]
    ans = 0

    while queue:
        cost, node = heapq.heappop(queue)
        if visited[node]:
            continue

        ans += cost
        visited[node] = True

        for n_node, n_cost in graph[node]:
            if not visited[n_node]:
                heapq.heappush(queue, (n_cost, n_node))

    return ans


def main():
    res = prim(graph, 1)
    print(res)


if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())

    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))  # 양방향 그래프

    main()
