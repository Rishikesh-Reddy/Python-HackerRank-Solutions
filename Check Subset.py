# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int, input().split()))
    for i in A:
        if i not in B:
            print("False")
            break
    else:
        print("True")
        
        
