import numpy as np


def solution(brown, yellow):
    answer = []
    x_add_y = brown / 2 + 2
    x_mul_y = brown + yellow

    x_sub_y = np.sqrt(np.power(x_add_y, 2) - 4 * x_mul_y)

    x = (x_add_y + x_sub_y) / 2
    y = (x_add_y - x_sub_y) / 2

    return [x, y]


"""
전체 카펫의 가로를 x, 세로를 y라고 한다면

{brown} + {yellow} = xy

{brown} = 2(x + y) - 4
{yellow} = (x-2)(y-2)

x+y = ({brown} / 2) + 2
xy = {brown} + {yellow}

(x+y)^2 - 4xy = (x-y)^2

(x-y)^2 = ({brown}^2 / 4) + 2{brown} + 4 - 4{brown} - 4{yellow}



"""

print(solution(10, 2))
