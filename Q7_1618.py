'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1618

'''

n= int(input())
zero=0
while n>=5:
    zero= int(zero + n/5)
    n=n/5
print(zero)

