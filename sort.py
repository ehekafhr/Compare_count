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
    lst2 = lst
    for i in range(n-1):
        for j in range(n-1-i):
            pass

#선택 정렬
def selection_sort(lst):
    n = len(lst) 

#merge sort
#TODO
def merge_sort(lst):
    pass

#quick sort
#TODO
def quick_sort(lst):
    pass