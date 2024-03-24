import math as m
import random as r
import sort
import copy

class Tracked_Values:
    comp_count = 0
    write_count = 0
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def get_comp():
        return Tracked_Values.comp_count

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
    
class Test:
    lst = []
    print = False
    def __init__(self):
        pass

    @staticmethod
    def generate(length, max):
        Test.lst = []
        for i in range(length):
            Test.lst.append(Tracked_Values(r.randint(0,max+1)))
    
    @staticmethod
    def set_print():
        Test.print = True
    
    @staticmethod
    def not_print():
        Test.print = False

    @staticmethod
    def test(sort):
        lst = copy.deepcopy(Test.lst)

        #Set comparision count zero.
        Tracked_Values.reset()
        sorted_lst = sort(lst)
        if(Test.print):
            print(sort.__name__)
            for e in lst:
                print(e,end=" ")      
            print("")
            for e in sorted_lst:
                print(e,end=" ")
            print("")
            print(Tracked_Values.get_comp())
        return sorted_lst, Tracked_Values.get_comp()


if __name__ == "__main__":
    Test.generate(50,100)
    Test.set_print()
    lst2, count = Test.test(sort.bubble_sort)