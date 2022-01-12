import time
start_time = time.time()
import random

matrix = [random.randint(-10, 10) for i in range(20)]


print('Matrix:', matrix)
len_res = len(matrix)
print('Matrix size:', len_res)
sum = 0

for i in range(len_res):
    for j in range(i+1,len_res):
       for k in range(j + 1,len_res):
            if (matrix[i]+matrix[j]+matrix[k] == 0):
               #print(matrix[i], matrix[j], matrix[k])
               sum=sum+1
print('Numbers of triplet:', sum)
print("--- %s seconds ---" % (time.time() - start_time))