""" 104ms
[Gold 5] 백준 9251번 LCS [Longest Common Subsequence]
두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것 찾기.

ex:
    ACAYKP와 CAPCAK의 LCS는 ACAK

첫째 줄과 둘째 줄에 대문자 알파벳으로만 이루어진 두 문자열이 주어진다.
(최대 1,000글자)
"""

import sys

input = sys.stdin.readline


def main():
    str1 = input().strip()
    str2 = input().strip()
    curr_row = [0] * 1000

    for i_s2, s2 in enumerate(str2):
        tmp = 0
        for i_s1, s1 in enumerate(str1):
            if tmp < curr_row[i_s1]:
                tmp = curr_row[i_s1]
            elif s2 == s1:
                curr_row[i_s1] = tmp + 1

    ans = max(curr_row)
    print(ans)


if __name__ == "__main__":
    main()
