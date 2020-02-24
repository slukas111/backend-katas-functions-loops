#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Sasha Lukas"
##Geeks for Geeks, google, and slack help. 
##took about dayish, had to delete original repository.

def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    return (x + y)
print(add(2,4))


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    # your code here
    result = 0
    if y < 0:
        for i in range(y, 0):
            result = add(result, -x)
        return result
    elif y > 0:
        for i in range(y):
            result = add(result, x)
        return result
    else:
        return 0
print(multiply(6,-8))
# print(multiply(5,3))
# print(multiply(2,-4))
# print(multiply(-4,-4))


def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    return


def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    return


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
