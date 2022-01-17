import time
import random
start_time = time.time()
size_matrix = 8000

#Bubble_Sort
matrix = [random.randint(-100000, 100000) for i in range(size_matrix)]
#print(matrix)
len_res = len(matrix)
print(len_res)
start_time2 = time.time()
for wall in range(1, len_res):
    for k in range(0, len_res - wall):
       if (matrix[k] > matrix[k + 1]):
           matrix[k], matrix[k + 1] = matrix[k+1], matrix[k]
#print(matrix)
print("Bubble_Sort --- %s seconds ---" % (time.time() - start_time2))


#Selection_Sort
matrix = [random.randint(-100000, 100000) for i in range(size_matrix)]
#print(matrix)
len_res = len(matrix)
print(len_res)
start_time3 = time.time()
for pos in range(0,len_res-1):
    for k in range(pos, len_res):
       if (matrix[pos] > matrix[k]):
           matrix[pos], matrix[k] = matrix[k], matrix[pos]
#print(matrix)
print("Selection_Sort --- %s seconds ---" % (time.time() - start_time3))


#Insert_Sort
matrix = [random.randint(-100000, 100000) for i in range(size_matrix)]
#print(matrix)
len_res = len(matrix)
print(len_res)
start_time4 = time.time()
for top in range(1,len_res):
    j = top
    while(j>0 and matrix[j-1] > matrix[j]):
        matrix[j],matrix[j-1] = matrix[j-1],matrix[j]
        j=j-1
#print(matrix)
print("Insert_Sort --- %s seconds ---" % (time.time() - start_time4))



#Shell_Sort
matrix = [random.randint(-100000, 100000) for i in range(size_matrix)]
#print(matrix)
len_res = len(matrix)
print(len_res)
start_time5 = time.time()
gap = len_res//2
while gap > 0:
    for iIndex in range(gap, len_res):
        temp = matrix[iIndex]
        jIndex = iIndex
        while jIndex >= gap and matrix[jIndex - gap] > temp:
            matrix[jIndex] = matrix[jIndex - gap]
            jIndex -= gap
        matrix[jIndex] = temp
    gap //= 2
#print(matrix)
print("Shell_Sort --- %s seconds ---" % (time.time() - start_time5))




#Merge_Sort
matrix = [random.randint(-100000, 100000) for i in range(size_matrix)]
#print(matrix)
len_res = len(matrix)
print(len_res)
def msort(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result
start_time6 = time.time()
result_matrix = msort(matrix)
#print(result_matrix)
print("Merge_Sort --- %s seconds ---" % (time.time() - start_time6))