def primecheck(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif 3 <= n < 13:
        x = n-3
        n1 = 6*x+1
        n2 = 6*x-1
        if n%2 != 0:
            return n2
        else:
            return n1
    elif n >= 13:
        n = n-13
        y = n**2+n+41
        return y

print(primecheck(5))