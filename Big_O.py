import lib.test as Test
import lib.sort as sort
import matplotlib.pyplot as plt


if __name__ == "__main__":
    sorts = sort.sorts()
    lengths= range(10,2000,10)
    max = 10000009
    Test.not_print()
    Test.time_test(sorts,lengths,max)