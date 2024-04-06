"""
[Gold 4] 백준 1339번 단어 수학
"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
weight = {}

for word in words:
    for i, c in enumerate(word[::-1]):
        if c in weight:
            weight[c] += 10**i
        else:
            weight[c] = 10**i

weights = sorted(weight.values(), reverse=True)

ans = 0
num = 9

for w in weights:
    ans += w * num
    num -= 1

print(ans)
