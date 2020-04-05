"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    a = n // 1000000000
    b = (n - a*1000000000) // 100000000
    c = (n - a*1000000000 - b*100000000) // 10000000
    d = (n - a*1000000000 - b*100000000 - c*10000000) // 1000000
    e = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000) // 100000
    f = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000 - e*100000) // 10000
    g = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000 - e*100000 - f*10000) // 1000
    h = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000 - e*100000 - f*10000 - g*1000) // 100
    i = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000 - e*100000 - f*10000 - g*1000 - h*100) // 10
    j = (n - a*1000000000 - b*100000000 - c*10000000 - d*1000000 - e*100000 - f*10000 - g*1000 - h*100 - i*10) // 1
    return a + b + c + d + e + f + g + h + i + j
