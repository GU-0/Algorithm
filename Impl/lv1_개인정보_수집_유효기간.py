"""
[Lv 1] 프로그래머스 2023 카카오 블라인드 채용 - 개인정보 수집 유효기간
"""


def calculate_date(year: int, month: int, day: int, period: int):
    month_c = period % 12
    year_c = period // 12

    month_r = month + month_c
    if month_r > 12:  # 월이 12를 초과할 경우 연도 증가
        year_c += month_r // 12
        month_r %= 12

    year_r = year + year_c

    # 마지막 날짜 처리 로직
    if day == 1:
        if month_r == 1:
            year_r -= 1
            month_r = 12
        else:
            month_r -= 1
        day_r = 28
    else:
        day_r = day - 1

    return year_r, month_r, day_r


def solution(today, terms, privacies):
    answer = []

    terms_dict = {
        term.split()[0]: int(term.split()[1]) for term in terms
    }  # {type: period}

    today_year, today_month, today_day = map(int, today.split("."))

    for idx, privacy in enumerate(privacies):
        p_year, p_month, p_day, p_type = *map(int, privacy[:-2].split(".")), privacy[-1]
        period = terms_dict[p_type]  # 타입에 따른 유효기간을 가져옴
        deadline_year, deadline_month, deadline_day = calculate_date(
            p_year, p_month, p_day, period
        )

        if (deadline_year, deadline_month, deadline_day) < (
            today_year,
            today_month,
            today_day,
        ):
            answer.append(idx + 1)

    return answer


# 예제 호출
print(
    solution(
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    )
)
