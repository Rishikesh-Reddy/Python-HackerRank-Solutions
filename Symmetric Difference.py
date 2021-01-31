# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = set(map(int, input().split()))
for i in sorted(set(N ^ set(M))):
    print(i)
