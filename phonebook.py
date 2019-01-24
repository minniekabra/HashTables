#python2

'''
This code implements a simple phone book manager using Hashing which is able to process operations like adding a number,
deleting a number and finding a number
'''


def add(jobs):
    number = int(jobs[1])
    name = jobs[2]
    L[number] = name

def find(jobs):
    number = int(jobs[1])
    if L[number] == None:
        find_array.append('not found')
    else:
        find_array.append(L[number])


def dele(jobs):
    number = int(jobs[1])
    if L[number] !=  None:
        L[number] = None


n = input()
L = [None]*10000000
find_array = []

for i in range(0,n):
    jobs = list(raw_input().split())
    n = len(jobs)

    if n == 3:
        add(jobs)

    if n == 2:
        if jobs[0] == 'find':
            find(jobs)
        elif jobs[0] == 'del':
            dele(jobs)

for i in range(0, len(find_array)):
    print(find_array[i])
