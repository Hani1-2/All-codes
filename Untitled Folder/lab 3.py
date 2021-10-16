import timeit
def Binary_Search(list,item):
    low = 0
    high = len(list)-1
    while low <= high :
        Mid = (low + high)//2
        if list[Mid] == item:
            return Mid
        elif  item<list[Mid] :
            high = Mid - 1
        else:
            low = Mid +1
    return None
beg = timeit.default_timer()
lst = input("Enter a sorted numeric List : ")
lst=lst.split(',')
lst1 = [int(i) for i in lst]
lst1.sort()
print(lst1)
item = int(input("Enter item you want to search in list"))
x = Binary_Search(lst1,item)
if item in lst1:
    print('The item' , item , 'is present at index',x)
else:
    print('The item' , item , 'is not present in list')
end = timeit.default_timer()
print('The time taken by implemented func',beg-end)

beg = timeit.default_timer()
print(lst1)
item = int(input("Enter item you want to search in list"))
x=lst1.index(item)
print('The item' , item , 'is present at index',x)
end = timeit.default_timer()
print('The time taken by builtin func',beg-end)

def Binary_Search_ins(lst,item):
    if lst != sorted(lst):
        print('List is not sorted , now we sort it for further implementation')
        lst =sorted(lst)
    print(lst)
    low = 0
    high = len(lst)-1
    while low <= high :
        Mid = (low + high)//2
        if lst[Mid] == item:
            print('The item' , item , 'is present at index',Mid)
            return Mid
        elif  item<lst[Mid] :
            high = Mid - 1
        else:
            low = Mid +1
    else:
        if item not in lst:
            print('Item',item, ' is not in list , so now we add it in list')
            lst.append(item)
            Binary_Search_ins(lst,item)


##
##lst = input("Enter a sorted numeric List : ")
##lst=lst.split(',')
##lst1 = [int(i) for i in lst]
##item = int(input("Enter item you want to search in list"))
##x = Binary_Search_ins(lst1,item)


    
