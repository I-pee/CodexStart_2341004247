'''
Name: Ipshit Kumar Dubey
Reg No.: 2341004247
PS Link: https://cses.fi/problemset/task/1069

'''

dna = input()

b = dna[0]
c_in = 1
c_fin = 1

for i in range(1, len(dna)):
    if dna[i] == b:
        c_in += 1
    else:
        b = dna[i]
        c_in = 1

    c_fin = max(c_fin, c_in)

print(c_fin)
