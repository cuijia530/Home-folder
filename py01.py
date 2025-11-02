a = 10
s = 0 
while a <= 1010:
    j = 1
    while j <= a:
        print('%d*%d=%d' % (a, j, a*j), end="\t")
        j += 1
    a += 1
    print()  # 换行
