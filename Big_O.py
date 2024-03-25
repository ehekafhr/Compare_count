import math as m
import random as r
import sort
import Tracker
import copy
import matplotlib.pyplot as plt

class Test:
    lst = []
    print = False
    def __init__(self):
        pass

    @staticmethod
    def generate(length, max):
        Test.lst = []
        for i in range(length):
            Test.lst.append(Tracker.Tracked_Values(r.randint(0,max+1)))
    
    @staticmethod
    def set_print():
        Test.print = True
    
    @staticmethod
    def not_print():
        Test.print = False

    @staticmethod
    def unit_test(sort):
        lst = copy.deepcopy(Test.lst)

        #Set comparision count zero.
        Tracker.Tracked_Values.reset()
        sorted_lst = sort(lst)
        if(Test.print):
            print(sort.__name__)
            for e in lst:
                print(e,end=" ")      
            print("")
            for e in sorted_lst:
                print(e,end=" ")
            print("")
            print(Tracker.Tracked_Values.get_comp())
        return sorted_lst, Tracker.Tracked_Values.get_comp()
    
    #sorts -> list of sorts.
    #range -> list of number of length
    #max -> max integer
    @staticmethod
    def time_test(sorts, lengths, max):
        lst = []
        number = len(lengths)
        for i in range(len(sorts)):
            lst.append([])
        for a, length in enumerate(lengths):
            if a%10 == 0:
                print(a*100/number, "%")
            Test.generate(length,max)
            for i, sort in enumerate(sorts):
                sorted_lst, cnt = Test.unit_test(sort)
                lst[i].append(cnt)
        for i, counts in enumerate(lst):
            plt.plot(counts, label = sorts[i].__name__)
        plt.yscale('log')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    sorts = sort.sorts()
    lengths= range(10,2000,10)
    max = 10000009
    Test.not_print()
    Test.time_test(sorts,lengths,max)