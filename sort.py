import math as m 
import copy

#버블 정렬
def bubble_sort(l):
    n = len(l)
    lst = copy.deepcopy(l)
    for j in range(n-1):
        for i in range(n-1):
            if lst[i]>lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
    return lst

#삽입 정렬
def insert_sort(lst):
    n = len(lst)
    lst2 = []
    #First Value
    lst2.append(lst[0])
    for i in range(n-1):
        pivot = i+1
        val = lst[i+1]
        for j, e in enumerate(lst2):
            if val<e:
                pivot = j
                break
        lst2.insert(pivot,val)
    return lst2

#선택 정렬
def selection_sort(lst):
    n = len(lst) 
    lst2 = copy.deepcopy(lst)
    lst3 = []
    for i in range(n):
        m = min(lst2)
        lst2.remove(m)
        lst3.append(m)
    return lst3

#merge sort
#TODO
def merge_sort(lst):

    pass

#quick sort
#TODO
def quick_sort(lst):
    pass