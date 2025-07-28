#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

print(add_tuple((1, 2), (3, 4)))       # (4, 6)
print(add_tuple((1, ), (3, 4)))        # (4, 4)
print(add_tuple((), (5,)))             # (5, 0)
print(add_tuple((7, 8, 9), (1, 2)))    # (8, 10)
