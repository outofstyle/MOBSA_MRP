#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import timeit
from time import clock


def get_random_number(num):
    '''get random number, no repeated element; use random.sample() method'''
    return random.sample(range(num), num)


if __name__ == "__main__":
    #use clock() method to calculate time
    start = clock()
    list_a = get_random_number(200)
    finish = clock()
    print(finish - start)
    #check the length of list generated by function
    print(len(list_a))
    print(len(set(list_a))) 

    #use timeit.Timer() method
    t1 = timeit.Timer('get_random_number(200)',
                      setup="from __main__ import get_random_number")
    #only excute once
    print(t1.timeit(1))
    #only repeat once, and only excute once
    print(t1.repeat(1, 1))

    #use timeit.Timer() and lambda to invoke function
    print(timeit.Timer(lambda: get_random_number(200)).timeit(1))