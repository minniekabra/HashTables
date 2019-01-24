#python2
'''
This code finds pattern in a text using Rabin–Karp’s algorithm
'''

from __future__ import print_function

def hash_value(S):
    n = len(S)
    x = 0
    k = 1
    for i in range(0, n):
        x = x + (ord(S[i]))

    return (x%1000000007 + 1000000007)%1000000007

def arequal(S1, S2):
    match = True
    if len(S1) != len(S2):
        match = False
    else:
        for i in range(0, len(S1)):
            if (S1[i] != S2[i]):
                match = False
                break
    return match


P = raw_input()
T = raw_input()
val_P = hash_value(P)


n = len(T)
m = len(P)
x = 1
y = pow(x, m, 1000000007)
result = []

for i in range(n-m, -1, -1):

    if i == n-m:
        val_L = hash_value(T[n-m: n-m+m])
        val_v = val_L
    else:
        hash_v = x*val_L + ord(T[i]) - ord(T[i+m])*(y)
        val_v = (hash_v % 1000000007 + 1000000007) % 1000000007
        val_L = val_v

    #print(val_L, val_P)

    if val_v != val_P:
        continue
    else:
        match = (P == T[i: i+m])


    if match == True:
        result.append(i)



#print results
for i in range(len(result) - 1, -1, -1):
    print(result[i], end = ' ')
