import math

number = 1452

x = number % 10
y = math.floor((number % 1000) / 100)

print(x * y, 'result')