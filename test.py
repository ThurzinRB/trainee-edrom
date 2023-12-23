from itertools import permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

[word, n] = input().strip().split(' ')

res = [''.join(i) for i in list(permutations(word, 2))]


res.sort()

for i in res:
    print(i)