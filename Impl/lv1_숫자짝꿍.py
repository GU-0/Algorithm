"""
프로그래머스 lv1 연습문제 숫자 짝꿍
"""


def solution(X, Y):
    answer = "-1"
    tmp = []
    cnt_set = {str(n): 0 for n in range(10)}

    for x in X:
        cnt_set[x] += 1

    for y in Y:
        if cnt_set[y] >= 1:
            tmp.append(y)
            cnt_set[y] -= 1

    if len(tmp) == 0:
        print(answer)
        return
    else:
        answer = ""
        tmp.sort(reverse=True)
        for e in tmp:
            answer += e
        if answer[0] == "0":
            answer = "0"
        print(answer)


solution("5525", "1255")
