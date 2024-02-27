"""
[Gold 3] 백준 1238번 파티

N개의 숫자로 구분된 각각의 마을에 한 명의 학생 살고 있음
이 N명의 학생이 X (1 <= X <= N)번 마을에 모여 파티를 하기로 함
마을 사이에는 M개의 단방향 도로,
i번째 길을 지나는데 T_i (1 <= T_i <= 100)의 시간 소비
각각의 학생들은 파티에 참석하기 위해 걸어갔다가 다시 돌아가야 함
최단시간을 원함
도로는 단방향임. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생이 누구인지 구하여라.

입력:
    첫째 줄: N M X - (1 <= N <= 1,000) (1 <= M <= 10,000)
    ~M개 줄: 도로의 시작점, 끝점, 소요시간 T_i
        시작점과 끝점 같은 도로 없음.
        시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개
    
    모든 학생은 집에서 X에 갈 수 있고, 돌아올 수 있음
"""

import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start, N):
    distance = [float("inf")] * (N + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if distance[node] < dist:
            continue

        for nxt, nxt_dist in graph[node]:
            cost = dist + nxt_dist
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(pq, (cost, nxt))

    return distance


if __name__ == "__main__":
    N, M, X = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    reverse_graph = [
        [] for _ in range(N + 1)
    ]  # X에서 각 마을로 돌아오는 길을 계산하기 위한 역방향 그래프

    for _ in range(M):
        a, b, T = map(int, input().split())
        graph[a].append((b, T))
        reverse_graph[b].append((a, T))  # 역방향 그래프에 경로 추가

    to_X = dijkstra(graph, X, N)  # X로 가는 최단 경로
    from_X = dijkstra(reverse_graph, X, N)  # X에서 돌아오는 최단 경로

    max_time = 0
    for i in range(1, N + 1):
        total_time = to_X[i] + from_X[i]  # 각 학생이 X로 가고 돌아오는 총 시간
        max_time = max(max_time, total_time)

    print(max_time)
