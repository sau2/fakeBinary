"""
Fake Binary
https://www.codewars.com/kata/57eae65a4321032ce000002d/python
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.
Note: input will never be an empty string
"""


def compSame(s="1234567890"):
    return ''.join(('0' if int(i) < 5 else '1') for i in s)


if __name__ == '__main__':
    print(compSame())
