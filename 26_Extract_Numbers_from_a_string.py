# Extract Numbers from a string


import re


def numbers(str):
    return re.findall('\d+', str)


s = "Python123"
num = numbers(s)
print(''.join(num))
