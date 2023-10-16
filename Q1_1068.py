'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1068

'''
n = int(input())

seq = []

seq.append(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    seq.append(n)

for i in seq:
    print (i, end=" ")
