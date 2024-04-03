number = 1234
s = str(number)
l = []
for num in s:
    num = int(num)
    num += 1
    if num > 9:
        num = 0
        l.append(num)
    else:
        l.append(num)

print (int(''.join(str(v) for v in l)))
