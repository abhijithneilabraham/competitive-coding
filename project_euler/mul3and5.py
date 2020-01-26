def mul():
    a=[i for i in range(1000) if i%3==0 or i%5==0 ]
    print(a)
    print(sum(a))
mul()