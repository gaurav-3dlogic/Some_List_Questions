
#First approch
list = [1, 2, 3, 4, 3, 3]
sum = 0
for i in list:
    sum += i
print(sum)

# Time complexity: O(n)
# Space complexity: O(1)


#Second approch
from functools import reduce

list1 = [1, 2, 3, 4, 3, 3]

def sum(a,b):
    return a + b

res = reduce(sum, list1)
print(res)
# Time complexity: O(n)
# Space complexity: O(1)


   





