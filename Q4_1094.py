'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1094

'''

n = int(input())
a = list(map(int, input().split()))

m = 0
p = a[0]

for i in range(1, n):
    if a[i] < p:
        m += p - a[i]
        a[i] = p
    p = a[i]

print(m)
