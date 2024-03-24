import math as m
import random as r
import sort

class Tracked_Values:
    comp_count = 0
    write_count = 0
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def reset():
        Tracked_Values.comp_count = 0

    def __str__(self):
        return str(self.value)

    def trace_comp(comp):
        def wrapper(*args, **kwargs):
            Tracked_Values.comp_count += 1
            return comp(*args, **kwargs)
        return wrapper
    
    @trace_comp
    def __lt__(self, other):
        return self.value < other.value
    
    @trace_comp
    def __le__(self, other):
        return self.value <= other.value
    
    @trace_comp
    def __eq__(self, other):
        return self.value == other.value
    
    @trace_comp
    def __ne__(self, other):
        return self.value != other.value

    @trace_comp
    def __gt__(self, other):
        return self.value > other.value
    
    @trace_comp
    def __ge__(self, other):
        return self.value >= other.value
    

if __name__ == "__main__":
    print("bubble sort")
    lst = [] 
    for i in range(50):
        lst.append(Tracked_Values(r.randint(0,100))) #0부터 99사이의 숫자 50개.
    Tracked_Values.reset()
    sort.bubble_sort(lst)
    print(Tracked_Values.count)