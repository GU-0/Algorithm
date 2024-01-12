"""
백준 6603번 '로또'[Silver 2]

{1, 2, ..., 49}에서 수 6개 고름.
Guide: 가장 유명한 전략 -> 49가지 수 중 k(k>6)개의 수를 골라 집합 S 만든 후 그 수로만 번호 선택

Input:
    첫번째 수: k (6 < k < 13)
    다음 k개 수 : 집합 S에 포함되는 수 (오름차순)
    입력 마지막 줄: 0
"""

import sys
import itertools


def input_process():
    sets = []

    while True:  # 0이 나올 때까지 각 줄의 '원소만' sets 리스트에 추가
        line = sys.stdin.readline().strip()

        if line == "0":
            break

        k, *elements = map(int, line.split())
        S = list(elements)
        sets.append(S)
    return sets


def main():
    sets = input_process()

    for set in sets:
        comb = itertools.combinations(set, 6)  # 조합 사용
        for c in comb:
            print(*c)
        print()


if __name__ == "__main__":
    main()
