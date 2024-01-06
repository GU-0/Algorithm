""" 40ms
[Gold 5] 백준 1068번 트리

트리에서 노드를 지웠을 때 남은 트리에서 리프 노드의 개수 구하기 (해당 노드와 자손까지 다 지워짐)
"""
import sys

input = sys.stdin.readline

N = int(input())
p_list = list(map(int, input().split()))
di = int(input().strip())


def dfs(n):
    p_list[n] = -2

    for i in range(N):
        if n == p_list[i]:
            dfs(i)


def main():
    cnt = 0
    dfs(di)
    for i in range(N):
        if p_list[i] != -2 and i not in p_list:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
