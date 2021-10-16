import timeit
#### selection sort####
def Selection_Sort(values):
    m = len(values)
    for i in range(m-1):
        # Assume ith is the smallest element
        minpos = i
        # Determine any other element if is smaller
        for j in range(i+1,m):
            if values[minpos] > values[j]:
                minpos = j
        # Swap the ith value and minpos value if the smallest value is not in the proper position
        if minpos!=i:
            values[i] , values[minpos] = values[minpos] , values[i]
    return values

start = timeit.default_timer()
values = [34,56,76,12,35,98,10]
x=Selection_Sort(values)
print('Selection Sort:\n',x)
stop = timeit.default_timer()
print('time traken by implemented func',start-stop)



def insertion_sort(values):
    m = len(values)
    for i in range(1,m):
        x = values[i]
        j = i-1
        while j>=0 and values[j]>x:
            values[j+1] = values[j]
            j-=1
        values[j+1]=x
    return values

start = timeit.default_timer()
values = [34,56,76,12,35,98,10]
x=insertion_sort(values)
print('inserttion Sort:\n',x)
stop = timeit.default_timer()
print('time traken by implemented func',start-stop)

