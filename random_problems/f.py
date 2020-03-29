
def f(i):
    if i<=1:
        return 1
    else:
        m=f(i-1)+2
        print(m)
        return m
print(f(11))
