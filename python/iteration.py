"""
# 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 (power of 2)
n = 1
while n <= 1024:
    print(n)
    n *= 2

n = 1
while n <= 1024:
    print(n)
    n += n
"""


# Checks if n is divisible to 4 or 7
n = 1
while n <= 50:
    if n % 4 == 0 or n % 7 == 0:
        print(n)
    n += 1
