from lib.sort import sorts
from lib.test import Test

if __name__ == "__main__":
    sorts = sorts()
    lengths= range(10,2000,10)
    max = 1000000
    Test.not_print()
    Test.time_test(sorts,lengths,max)