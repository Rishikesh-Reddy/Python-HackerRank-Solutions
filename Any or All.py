n = int(input())
l = list(map(int, input().split()))
print(all([all([i > 0 for i in l]), any(j == int(str(abs(j))[::-1])for j in l)]))
