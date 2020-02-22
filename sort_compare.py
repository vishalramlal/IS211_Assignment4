#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assignment 4 Part 2

import random
import time

def randlist(n):
    the_list = range(n)
    random.shuffle(the_list)
    return the_list

intlist5h = [randlist(500)for i in range(100)]
intlist1th = [randlist(1000) for i in range(1000)]
intlist10th = [randlist(10000) for i in range(10000)]




def insertion_sort(a_list):
    lists = [sub_list[0] for sub_list in a_list]
    startclock = time.time()
    for lists in a_list:
        for index in range(1, len(lists)):
            current_value = lists[index]
            position = index
            while position > 0 and lists[position - 1] > current_value:
                lists[position] = lists[position - 1]
                position = position - 1
            lists[position] = current_value
    endclock = time.time()
    runtime = (endclock - startclock)
    return runtime


def shell_sort(a_list):
    lists = [sub_list[0] for sub_list in a_list]
    startclock = time.time()
    for lists in a_list:
        sublist_count = len(lists) // 2
        while sublist_count > 0:
            for start_position in range(sublist_count):
                gap_insertion_sort(lists, start_position, sublist_count)
                #print("After increments of size", sublist_count, "The list is",a_list)
                sublist_count = sublist_count // 2
    endclock = time.time()
    runtime = (endclock - startclock)
    return runtime
        
        
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
            
            

def python_sort(the_list):
    lists = [sub_list[0] for sub_list in the_list]
    startclock = time.time()
    for lists in the_list:
        startclock = time.time()
        the_list.sort()
        endclock = time.time()
        runtime = (endclock - startclock)
    return runtime


insort5h = []
insort1th = []
insort10th = []

shsort5h = []
shsort1th = []
shsort10th = []

pysort5h = []
pysort1th = []
pysort10th = []


def main():
    insort5h.append(insertion_sort(intlist5h))
    insort1th.append(insertion_sort(intlist1th))
    insort10th.append(insertion_sort(intlist10th))
    shsort5h.append(insertion_sort(intlist5h))
    shsort1th.append(insertion_sort(intlist1th))
    shsort10th.append(insertion_sort(intlist10th))
    pysort5h.append(insertion_sort(intlist5h))
    pysort1th.append(insertion_sort(intlist1th))
    pysort10th.append(insertion_sort(intlist10th))
    
    
    insort5h_avg = sum(insort5h)/500
    insort1th_avg = sum(insort1th)/1000
    insort10th_avg = sum(insort10th)/10000
    shsort5h_avg = sum(shsort5h)/500
    shsort1th_avg = sum(shsort1th)/1000
    shsort10th_avg = sum(shsort10th)/10000
    pysort5h_avg = sum(pysort5h)/500
    pysort1th_avg = sum(pysort1th)/1000
    pysort10th_avg = sum(pysort10th)/10000
    
    
    print "Insertion Sort took %10.7f seconds to run, on average, for a list of 500" %insort5h_avg
    print "Insertion Sort took %10.7f seconds to run, on average, for a list of 1000" %insort1th_avg
    print "Insertion Sort took %10.7f seconds to run, on average, for a list of 10000" %insort10th_avg
    print "Shell Sort took %10.7f seconds to run, on average, for a list of 500" %shsort5h_avg
    print "Shell Sort took %10.7f seconds to run, on average, for a list of 1000" %shsort1th_avg
    print "Shell Sort took %10.7f seconds to run, on average, for a list of 10000" %shsort10th_avg
    print "Python Sort took %10.7f seconds to run, on average, for a list of 500" %pysort5h_avg
    print "Python Sort took %10.7f seconds to run, on average, for a list of 1000" %pysort1th_avg
    print "Python Sort took %10.7f seconds to run, on average, for a list of 10000" %pysort10th_avg
    
    
if __name__ == "__main__":
        main()


# In[ ]:




