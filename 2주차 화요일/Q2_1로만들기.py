def small(a, b):
    if a < b:
        return a
    else:
        return b

cal_list = [0, 0, 1, 1]#to 3
n = int(input())

for i in range(4, n + 1):
    cal_list.append(cal_list[-1])

    if not i % 2:
        cal_list[i] = small(cal_list[i], cal_list[i // 2])
    if not i % 3:
        cal_list[i] = small(cal_list[i], cal_list[i // 3])
    cal_list[i]+=1

print(cal_list[n])
