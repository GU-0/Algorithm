"""
[Gold 4] 백준 1967번 트리의 지름

트리: 사클이 없는 무방향 그래프
    어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다.
    어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가ㅇ 길게 늘어나는 경우가 있을 것.
        이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 양 끝 점으로 하는 원 안에 들어감
            이 두 노드 사이 경로의 길이를 '트리의 지름'이라고 함
                즉, 트에 존재하는 모든 경로들 중에서 가장 긴 것의 길이
    
    입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트의 지름을 구해서 출력하여라.


입력:
    첫째 줄: n - 노드의 개수 (1 <= n <= 10,000)
    ~ n-1개 줄: a b c - 각 간선에 대한 정보 (부모 노드, 자식 노드, 간선의 가중치)
        부모 노드의 번호가 작은 것부터 입력
            부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것부터 입력
        루트 노드는 항상 1
        가중치 <= 100인 양의 정수
"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for i in range(n + 1):
    tree[i].sort(key=lambda x: x[1], reverse=True)


############################


def dfs(s, dis):
    for i in tree[s]:
        a, b = i
        if distance[a] == -1:
            distance[a] = dis + b
            dfs(a, dis + b)


distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

s = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[s] = 0
dfs(s, 0)

print(max(distance))
