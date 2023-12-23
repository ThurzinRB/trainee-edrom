from collections import defaultdict
# Enter your code here. Read input from STDIN. Print output to STDOUT

[n, m] = list(map(int, input().strip().split(' ')))

A = defaultdict(list)
# print(A)

for i in range(n):
    A[input()].append(i+1)

 
B = [input() for _ in range(m)]

for i in B:
    print(*A[i]) if len(A[i])>0 else print('-1')

# print(n, m)
# print(A)
# print(B) *A[i] if len(A[i])>0 else 
