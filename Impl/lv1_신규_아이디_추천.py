"""
[Lv 1] 프로그래머스 2021 카카오 블라인드 채용 - 신규 아이디 추천

규칙에 맞지 않는 아이디에 대하여, 입력된 아이디와 유사하며 규칙에 맞는 아이디 추천해주기
규칙:
    3자 이상 15자 이하
    알파벳 소문자, 숫자 '-', '_', '.' 문자만 사용
    단, '.'는 처음과 끝에 사용 불가, 연속으로 사용 불가

7단계의 순차적 처리 과정:
    1. new_id의 모든 대문자를 대응되는 소문자로 치환
    2. new_id에서 알파벳 소문자, 숫자, '-', '_', '.' 제외한 모든 문자 제거
    3. new_id에서 '.'가 두 번 이상 연속된 부분을 하나의 마침표로 치환
    4. new_id에서 마침표가 처음이나 끝에 위치한다면 제거
    5. new_id가 빈 문자열이면 new_id에 'a' 대입
    6. new_id의 길이가 16자 이상이라면 첫 15자 제외한 문자 모두 제거
        제거 후 마침표가 끝에 위치한다면 마침표 제거
    7. new_id의 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복하여 붙임
"""


def solution(new_id):
    # possible alphabets, 특수문자들
    possible_list = []
    for i in range(97, 123):
        possible_list.append(chr(i))
    for i in range(47, 58):
        possible_list.append(chr(i))
    possible_list += ["-", "_", "."]
    # step 1
    id = new_id.lower()
    # step 2
    tmp = ""
    for c in id:
        if c in possible_list:
            tmp += c
    id = tmp
    # step 3
    tmp = ""
    is_repeated = False
    for c in id:
        if is_repeated:
            if c == ".":
                continue
        if c == ".":
            is_repeated = True
        else:
            is_repeated = False
        tmp += c
    id = tmp
    # step 4
    id = id.strip(".")
    # step 5
    if not id:
        id = "a"
    # step 6
    if len(id) > 15:
        id = id[:15]
        if id[-1] == ".":
            id = id[:-1]
    # step 7
    if len(id) < 3:
        n = 3 - len(id)
        tmp = id[-1]
        for i in range(n):
            id += tmp

    answer = id
    return answer


############################
print(solution("abcdefghijklmn.p"))
