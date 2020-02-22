#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Assignment 4 Part 1

import random
import time

def randlist(n):
    the_list = range(n)
    random.shuffle(the_list)
    return the_list

intlist5h = [randlist(500) for i in range(100)]
intlist1th = [randlist(1000) for i in range(100)]
intlist10th = [randlist(10000) for i in range(100)]



def sequential_search(a_list, item):
    startclock = time.time()
    lists = [sub_list[0] for sub_list in a_list]
    for lists in a_list:        
        pos = 0
        found = False
        while pos < len(lists) and not found:
            if lists[pos] == item:
                found = True
            else:
                pos = pos+1
    endclock = time.time()
    runtime = (endclock - startclock)
    return found, runtime



def ordered_sequential_search(a_list, item):
    startclock = time.time()
    lists = [sub_list[0] for sub_list in a_list]
    for lists in a_list:
        pos = 0
        found = False
        stop = False
        while pos < len(lists) and not found and not stop: 
            if lists[pos] == item:
                found = True
            else:
                if lists[pos] > item:
                    stop = True
                else:
                    pos = pos+1
    endclock = time.time()
    runtime = (endclock - startclock)
    return found, runtime



def binary_search_iterative(a_list, item):
    startclock = time.time()
    lists = [sub_list[0] for sub_list in a_list]
    for lists in a_list:
        first = 0
        last = len(lists) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if lists[midpoint] == item:
                found = True
            else:
                if item < lists[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
    endclock = time.time()
    runtime = (endclock - startclock)
    return found, runtime



seq5h = []
seq1th = []
seq10th = []

ordseq5h = []
ordseq1th = []
ordseq10th = []

binsiter5h = []
binsiter1th = []
binsiter10th = []



def main():
    seq5h.append(sequential_search(intlist5h, -1)[1])
    seq1th.append(sequential_search(intlist1th, -1)[1])
    seq10th.append(sequential_search(intlist10th, -1)[1])


    intlist5h.sort()
    intlist1th.sort()
    intlist10th.sort()

    binsiter5h.append(binary_search_iterative(intlist5h, -1)[1])
    binsiter1th.append(binary_search_iterative(intlist1th, -1)[1])
    binsiter10th.append(binary_search_iterative(intlist10th, -1)[1])


    ordseq5h.append(sequential_search(intlist5h, -1)[1])
    ordseq1th.append(sequential_search(intlist1th, -1)[1])
    ordseq10th.append(sequential_search(intlist10th, -1)[1])



    seq5h_avg = (sum(seq5h))/500
    seq1th_avg = (sum(seq1th))/1000
    seq10th_avg = (sum(seq10th))/10000

    ordseq5h_avg = (sum(ordseq5h))/500
    ordseq1th_avg = (sum(ordseq1th))/1000
    ordseq10th_avg = (sum(ordseq10th))/10000

    binsiter5h_avg = (sum(binsiter5h))/500
    binsiter1th_avg = (sum(binsiter1th))/1000
    binsiter10th_avg = (sum(binsiter10th))/10000


    print "Sequential Search took %10.7f seconds to run, on average, using a list of 500" %seq5h_avg
    print "Sequential Search took %10.7f seconds to run, on average, using a list of 1000" %seq1th_avg
    print "Sequential Search took %10.7f seconds to run, on average, using a list of 10000" %seq10th_avg

    print "Ordered Sequential Search took %10.7f seconds to run, on average, using a list of 500" %ordseq5h_avg
    print "Ordered Sequential Search took %10.7f seconds to run, on average, using a list of 1000" %ordseq1th_avg
    print "Ordered Sequential Search took %10.7f seconds to run, on average, using a list of 10000" %ordseq10th_avg

    print "Binary Search Iterative took %10.7f seconds to run, on average, using a list of 500" %binsiter5h_avg
    print "Binary Search Iterative took %10.7f seconds to run, on average, using a list of 1000" %binsiter1th_avg
    print "Binary Search Iterative took %10.7f seconds to run, on average, using a list of 10000" %binsiter10th_avg
    
    
if __name__ == "__main__":
        main()

#def binary_search_recursive(a_list, item):
#    startclock = time.time()
#    lists = [sub_list[0] for sub_list in a_list]
#    for lists in a_list:
#        if len(lists) == 0:
#            endclock = time.time()
#            runtime = (endclock - startclock)
#            return False, runtime
#        else:
#            midpoint = len(lists) // 2
#            if lists[midpoint] == item:
#                endclock = time.time()
#                runtime = (endclock - startclock)
#                return True, runtime
#            else:
#                if item < lists[midpoint]:
#                    return binary_search_recursive(lists[:midpoint], item)
#                else:
#                    return binary_search_recursive(lists[midpoint + 1:], item)


# In[ ]:





# In[ ]:




