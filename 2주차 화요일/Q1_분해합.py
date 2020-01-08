n = int(input())
flag = 1
for i in range(1, n):
    tmp = int(i)
    genor = int(0)

    while tmp:
        genor += tmp % 10
        tmp //= 10

    if n == i + genor:
        print(i)
        flag = 0
        break
if flag:
    print(0)