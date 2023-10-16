'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1070

'''

n= int(input())
if n==2 or n==3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i, end=" ")
    for i in range(1, n+1,2):
        print(i, end=" ")
