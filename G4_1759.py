"""40ms
[Gold 5] 백준 1759번 암호 만들기

암호는 서로 다른 L개의 알파벳 소문자, 최소 한개의 모음 (a, e, i, o, u)과 최소 두 개의 자음으로 구성
암호를 이루는 알파벳은 오름차순일 가능성 높음

주어진 문자의 종류는 C가지
C개의 문자들이 주어졌을 때 가능한 암호들을 모두 구하라.

입력 첫 줄: L C (3 <= L <= C <= 15)
둘째 줄 ~ : C개의 문자들
"""

import sys
from itertools import combinations as comb

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def main():
    com = list(comb(arr, L))
    res = []

    for c in com:
        if any(x in c for x in "aeiou"):
            consonants = sum(1 for x in c if x not in "aeiou")
            if consonants >= 2:
                res.append("".join(c))
    for r in sorted(res):
        print(r)


if __name__ == "__main__":
    L, C = map(int, input().split())
    arr = sorted(list(map(str, input().split())))
    main()
