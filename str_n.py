def fun(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s


s = str(input())
n = int(input())
print(fun(s, n))
