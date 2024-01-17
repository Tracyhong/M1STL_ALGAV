import matplotlib.pyplot as plt
#MinHeapArray
from MinHeapArray import exec_time_construction_array
from MinHeapArray import exec_time_ajout_iteratif_array
from MinHeapArray import exec_time_union_array
#MinHeapTree
from MinHeapTree import exec_time_construction_tree
from MinHeapTree import exec_time_ajout_iteratif_tree
from MinHeapTree import exec_time_union_tree
#BinomialHeap
from BinomialHeap import exec_time_construction_binomial
from BinomialHeap import exec_time_union_binomial

## GENERATE DATA --------------------------------------------------------------------------------

#MinHeapArray
avg_times_construction_array = exec_time_construction_array()
avg_times_insertKeyList_array = exec_time_ajout_iteratif_array()
avg_times_union_array = exec_time_union_array()

#MinHeapTree
avg_times_construction_tree = exec_time_construction_tree()
avg_times_insertKeyList_tree = exec_time_ajout_iteratif_tree()
avg_times_union_tree = exec_time_union_tree()

#BinomialHeap
avg_times_construction_binomial = exec_time_construction_binomial()
avg_times_union_binomial = exec_time_union_binomial()


## GENERATE GRAPHICS -----------------------------------------------------------------------------

# BY FUNCTION -------------

nbJeu = 5
nbCle = [1000, 5000, 10000, 20000, 50000, 80000, 120000, 200000]

fig = plt.figure(figsize=(15,5))

#CONSTRUCTION 
plt.subplot(1,3,1) # row 1, col 2 index 1
plt.plot(nbCle, avg_times_construction_tree, label="Tree", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_construction_array, label="Array", marker='x', linestyle='-', color='r')
plt.plot(nbCle, avg_times_construction_binomial, label="Binomial", marker='x', linestyle='-', color='g')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Construction')

# AJOUT ITERATIF
plt.subplot(1,3,2) # index 2
plt.plot(nbCle, avg_times_insertKeyList_tree, label="Tree", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_insertKeyList_array, label="Array", marker='x', linestyle='-', color='r')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('AJOUT ITERATIF')

# UNION
plt.subplot(1,3,3) # index 2
plt.plot(nbCle, avg_times_union_tree, label="Tree", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_union_array, label="Array", marker='x', linestyle='-', color='r')
plt.plot(nbCle, avg_times_union_binomial, label="Binomial", marker='x', linestyle='-', color='g')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('UNION')
plt.show()


# BY STRUCTURE -------------
nbJeu = 5
nbCle = [1000, 5000, 10000, 20000, 50000, 80000, 120000, 200000]

fig = plt.figure(figsize=(15,5))

#ARRAY 
plt.subplot(1,3,1) # row 1, col 2 index 1
plt.plot(nbCle, avg_times_insertKeyList_array, label="Ajout iteratif", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_construction_array, label="Construction", marker='x', linestyle='-', color='r')
plt.plot(nbCle, avg_times_union_array, label="Union", marker='x', linestyle='-', color='g')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Min Heap Array')

# TREE
plt.subplot(1,3,2) # index 2
plt.plot(nbCle, avg_times_insertKeyList_tree, label="Ajout iteratif", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_construction_tree, label="Construction", marker='x', linestyle='-', color='r')
plt.plot(nbCle, avg_times_union_tree, label="Union", marker='x', linestyle='-', color='g')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Min Heap Tree')

# BINOMIAL
plt.subplot(1,3,3) # index 2
plt.plot(nbCle, avg_times_construction_binomial, label="Construction", marker='x', linestyle='-', color='b')
plt.plot(nbCle, avg_times_union_binomial, label="Union", marker='x', linestyle='-', color='r')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Binomial Heap')
plt.show()


# Single plot for binomial heap for more details --------------------
#Binomial
nbJeu = 5
nbCle = [1000, 5000, 10000, 20000, 50000, 80000, 120000, 200000]

fig = plt.figure(figsize=(15,5))

# Construction
plt.subplot(1,2,1) 
plt.plot(nbCle, avg_times_construction_tree, label="Construction", marker='x', linestyle='-', color='r')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Binomial Heap : Construction ')

# Union
plt.subplot(1,2,2) # index 2
plt.plot(nbCle, avg_times_union_binomial, label="Union", marker='x', linestyle='-', color='r')
plt.xlabel('Size of Data (Number of Keys)')
plt.ylabel('Average Execution Time (seconds)')
plt.legend()
plt.title('Binomial Heap : Union')
plt.show()