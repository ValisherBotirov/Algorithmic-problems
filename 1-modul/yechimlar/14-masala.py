def reverse_number(number):
    s = str(number)
    n = s[2] + s[1] + s[0]
    return n

print(reverse_number(123))