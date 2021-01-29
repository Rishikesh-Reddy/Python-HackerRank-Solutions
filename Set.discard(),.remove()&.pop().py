n = int(input())
s = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    c = input().split(' ')
    if "remove" in c:
        s.remove(int(c[1]))
    elif "discard" in c:
        s.discard(int(c[1]))
    elif "pop" in c:
        s.pop()
print(sum(s))
