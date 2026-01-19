#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        a_first = tuple_a[0]
    else:
        a_first = 0

    if len(tuple_a) >= 2:
        a_second = tuple_a[1]
    else:
        a_second = 0

    if len(tuple_b) >= 1:
        b_first = tuple_b[0]
    else:
        b_first = 0

    if len(tuple_b) >= 2:
        b_second = tuple_b[1]
    else:
        b_second = 0

    result_first = a_first + b_first
    result_second = a_second + b_second

    return (result_first, result_second)
