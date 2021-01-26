n,m = map(int, input().split())
h = 0
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
for i in arr:
    if i in a:
        h += 1
    elif i in b:
        h -= 1
print(h)
