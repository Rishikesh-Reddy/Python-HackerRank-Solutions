a = int(input())
A = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    c = input().split(' ')
    b = set(map(int, input().split()))
    if "intersection_update" in c:
        A.intersection_update(b)
    elif "symmetric_difference_update" in c:
        A.symmetric_difference_update(b)
    elif "difference_update" in c:
        A.difference_update(b)
    else:
        A.update(b)
print(sum(A))
    
