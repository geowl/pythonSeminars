#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

# list_num = [1,1,2,0,-1,3,4,4]
# print(len(set(list_num)))
# print(set(list_num))

import random

list_num = [1,1,2,0,-1,3,4,4, 487]
count = 0
new_list = []
for i in list_num:
    if i not in new_list:
        new_list.append(i)
print(len(new_list))
print(new_list)