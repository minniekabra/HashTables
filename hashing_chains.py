#python2

'''
This code implements a hash table using the chaining scheme
'''

from __future__ import print_function

def hash_value(S, m):
    n = len(S)
    x = 0
    for i in range(0, n):
        x = x + (ord(S[i])*(263**i))
        x = (x % 1000000007 + 1000000007) % 1000000007


    x = (x%m + m)%m

    return x

def find(number, O2):
    c = False
    for i in range(0, len(L[number])):
        if L[number][i] == O2:
            c = True
            break
    return c

def delete(number, O2):
    for i in range(0, len(L[number])):
        if L[number][i] == O2:
            L[number].pop(i)
            break

def add(number,O2):
    L[number].append(O2)


m = input()
n = input()

L = [[] for _ in range(m)]
output_array = []

for i in range(0, n):
    O1, O2 = raw_input().split()

    if O1 == 'add' or O1 == 'find' or O1 == 'del':
        number = hash_value(O2, m)
        found = find(number, O2)
        if found == True:
            if O1 == 'find':
                output_array.append(['yes'])
            elif O1 == 'del':
                delete(number, O2)

        else:
            if O1 == 'find':
                output_array.append(['no'])
            elif O1 == 'add':
                add(number, O2)

    else:
        number = int(O2)
        if len(L[number]) == 0:
            output_array.append([''])
        else:
            arr = []
            for i in range(len(L[number]) -1, -1, -1):
                arr.append(L[number][i])

            output_array.append(arr)



for j in range(0, len(output_array)):
    for i in range(0, len(output_array[j])):
        if i == len(output_array[j]) - 1:
            print(output_array[j][i])
        else:
            print(output_array[j][i], end = ' ')
