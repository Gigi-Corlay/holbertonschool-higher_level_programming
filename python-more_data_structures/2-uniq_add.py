#!/usr/bin/python3
def uniq_add(my_list=[]):
    stock_integer = []
    for nbr in my_list:
        if nbr not in stock_integer:
            stock_integer.append(nbr)

    total = sum(stock_integer)

    return total
