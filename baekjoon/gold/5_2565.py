"""40ms
[Gold 5] 백준 2565번 전깃줄

두 전봇대 A와 B 사이에 전깃줄을 추가한다.
전깃줄이 교차되면 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 모든 전깃줄이 서로 교차하지 않도록 만들려고 한다.
전깃줄의 위치는 전봇대의 맨 위에서부터 1, 2, 3, ...

입력 첫째 줄: 두 전봇대 사이 전깃줄의 개수 (100 이하 자연수)
입력 둘째 줄 ~ : 전깃줄이 A전봇대에 연결되는 위치 번호와 B전봇대에 연결되는 위치 번호 주어짐. (각 번호 500 이하 자연수)
    -> 같은 위치에 두 개 이상 전깃줄 연결 X
"""

"""
전깃줄이 교차되면 안되므로 증가함수의 형태를 띄면 된다.
2차원 배열로 정렬 후, arr[i][1]들에 LIS 알고리즘.
"""

import sys

input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])


# Binary Search 후 값이 들어갈 idx 반환
def BS(arr, s, e, n):
    while s < e:
        m = (s + e) // 2
        if n > arr[m]:
            s = m + 1
        else:
            e = m
    return e


# 다음 항목이 부분 배열의 마지막 항목보다 크다면 끝에 붙이고,
# 작다면 적절한 위치를 BS를 통해 구하여 해당 위치에 삽입한다. <- 최대 길이 유지 가능
def LIS(arr, l):
    li = []
    max_len = 0
    for i in range(l):
        if i == 0:
            li.append(arr[i][1])
            max_len = 1
        else:
            if arr[i][1] > li[-1]:
                li.append(arr[i][1])
                max_len = max(max_len, len(li))

            elif arr[i][1] < li[-1]:
                idx = BS(li, 0, len(li), arr[i][1])
                li[idx] = arr[i][1]
    return max_len


ans = LIS(arr, n)
print(n - ans)
