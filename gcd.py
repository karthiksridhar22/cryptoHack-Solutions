def gcd(a, b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
        gcd(a,b)

    return a

print(gcd(66528, 52920))