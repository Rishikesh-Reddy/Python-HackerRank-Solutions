import re
n = int(input())
l = []
for i in range(n):
    try:
        s = input()
        re.compile(s)
    except:
        l.append(False)
        continue
    l.append(True)
for i in l:
    print(i)
