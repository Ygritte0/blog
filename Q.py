# encoding: utf-8
from collections import deque

list1 = deque([1, 2, 3, 4, 5, 7, 8, 0])

for i in list1:
    print(i)
    # list1.append(9)

a = {1: 1}
for i in a:
    a[i + 1] = i + 1
    print(a)
