#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count_element = 0
    i = 0
    while i < x:
        try:
            print(my_list[i], end='')
            count_element += 1
        except IndexError:
            break
        i += 1

    print()
    return count_element
