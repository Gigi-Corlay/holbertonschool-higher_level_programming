#!/usr/bin/python3
"""
Print the alphabet in reverse order, 
alternating lowercase and uppercase letters, 
without a newline
"""
for i in range(26):
    if i % 2 == 0:
        lowercase = chr(122 - i)
        print(lowercase, end='')
    else:
        uppercase = chr(90 - (i // 2) *  2 - 1)
        print(uppercase, end='')
