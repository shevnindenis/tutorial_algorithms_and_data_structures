import time
import random
start_time = time.time()


matrix = [random.randint(-100000, 100000) for i in range(5000)]


#print(matrix)
len_res = len(matrix)
print(len_res)
sum = 0
start_time2 = time.time()
for j in range(len_res):
    wall = len_res-j
    for i in range(wall-1):
       if (matrix[i] > matrix[i + 1]):
           temp = matrix[i]
           matrix[i] = matrix[i + 1]
           matrix[i + 1] = temp
    #print(matrix)
print("Bubble_Sort --- %s seconds ---" % (time.time() - start_time2))

#Selection_Sort
start_time3 = time.time()
for i in range(0,len_res):
    wall = len_res-i
    max_index = 0
    for current_index in range(0, wall):


       if (matrix[current_index] > matrix[max_index]):
           max_index = current_index
    temp = matrix[wall-1]
    matrix[wall-1] = matrix[max_index]
    matrix[max_index] = temp
#print(matrix)
print("Selection_Sort --- %s seconds ---" % (time.time() - start_time3))