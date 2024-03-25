import math as m 
import copy
from .tracker import Tracked_Values

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
def merge(lst1, lst2):
    result = []
    n = Tracked_Values(len(lst1)) # first list
    m = Tracked_Values(len(lst2)) # second list
    p1 = Tracked_Values(0) # pivot of first list
    p2 = Tracked_Values(0) # pivot of second list

    while p1< n and p2 < m:
        if lst1[p1.value]<lst2[p2.value]:
            result.append(lst1[p1.value])
            p1.value+=1
        else:
            result.append(lst2[p2.value])
            p2.value+=1

    if p1<n:
        result.extend(lst1[p1.value:])
    else:
        result.extend(lst2[p2.value:])

    return result

def merge_sort(lst):
    n = len(lst)
    pivot = int(n/2)
    
    #least case
    if n==1:
        return lst
    
    left = lst[:pivot]
    right = lst[pivot:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

#quick sort
#TODO
def quick_sort(lst):
    pass

def python_sort(lst):
    return sorted(lst)

def sorts():
    return [bubble_sort, insert_sort, selection_sort, merge_sort,python_sort]
