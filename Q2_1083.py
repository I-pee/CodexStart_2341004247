'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1083

'''

n=int(input())
l=list(map(int,input().split()))
sum_n=int( n*(n+1)/2)
sum_l=0
for i in l:
    sum_l+=i
missing=sum_n-sum_l
print(missing)

