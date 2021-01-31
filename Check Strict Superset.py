s = set(map(int, input().split()))
n = int(input())
l = True
for _ in range(n):
    s1 = set(map(int, input().split()))
    if s1 == s:
        l = False
    for i in s1:
        if i not in s:
            l = False
            break
print(l)
