# from fibo import fib
#
# def fib2():
#     print('hello')
# try:
#     fib(1)
# except TypeError:
#     print('type error occurs')
#
# a = 3

# num = None
# while num != 2:
#     pass


def bubble(array):
    for i in range(len(array) - 1):  # n-1  # len()：返回容器中元素的数量，可以将i和j看成索引
        for j in range(len(array) - 1 - i):  # n - 1 -i
            if array[j] > array[j + 1]:  # 如果前一个大于后一个，则交换 1
                temp = array[j]  # 1、0
                array[j] = array[j + 1]  # 1,0
                array[j + 1] = temp  # 1, 0


#
#
# # if __name__ == "__main__":
# #  array = [265, 494, 302, 160, 370, 219, 247, 287,
# #  354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]
# #  print("------->排序前<-------")
# #  print(array)
# #  bubble(array)
# #  print("------->排序后<-------")
# #  print(array)
#
#
# def select_sort(array):
#     for i in range(len(array) - 1):  # 找出最小的数放与array[i]交换
#         for j in range(i + 1, len(array)):
#             if array[i] > array[j]:
#                 temp = array[i]
#                 array[i] = array[j]
#                 array[j] = temp
#
#
# if __name__ == "__main__":
#     array = [265, 494, 302, 160, 370, 219, 247, 287,
#              354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]
#     print(array)
#     select_sort(array)
#     print(array)
#
#     print("=======================================")
#
# import time
#
#
# def insertion_sort(array):
#     for i in range(1, len(array)):  # 对第i个元素进行插入，i前面是已经排序好的元素
#         position = i  # 要插入数的下标
#         current_val = array[position]  # 把当前值存下来
#         # 如果前一个数大于要插入数，则将前一个数往后移，比如5,8,12,7;要将7插入，先把7保存下来，比较12与7，将12往后移
#         while position > 0 and current_val < array[position - 1]:
#             array[position] = array[position - 1]
#             position -= 1
#         else:  # 当position为０或前一个数比待插入还小时
#             array[position] = current_val
#
#
# if __name__ == "__main__":
#     array = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
#     print(array)
#     time_start = time.time()
#     insertion_sort(array)
#     time_end = time.time()
#     print("time: %s" % (time_end - time_start))
#     print(array)


# import math
#
# print(math.log(10))
#
#
# def binary_search(list1, item):
#     low = 0  # 1
#     high = len(list1) - 1  # 1
#     while low <= high:  #
#         mid = (low + high) / 2
#         guess = list1[mid]
#         if guess == item:
#             return mid
#
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None
#
#
# a = binary_search([1, 2, 3, 4, 6, 8, 9], 7)
# print(a)

# '''
# 如何将一个数组用的元素按从下到大的顺序排列
# '''
#
#
# def find_smallest(arr):
#     # 用于找到最小元素
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest_index = find_smallest(arr)
#         new_arr.append(arr.pop(smallest_index))
#     return new_arr
#
#
# result = selection_sort([1, 3, 5, 6, 2, 0, 7, 9])
# print(result)
#
#
# # 伪代码
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print('found the key!')

# 用循环写sum
# def sum_num(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total
#
#
# result = sum_num([1, 2, 3])
# print(result)


# sum 函数,使用递归（调用函数自己）
# def my_sum(my_list):
#     if my_list == []:   # 基准线
#         return 0
#     else:
#         result = 0
#         new_list = []
#         for i in range(len(my_list)):
#             result += my_list[i]
#             new_list = my_list[i + 1:]
#             my_sum(new_list)
#     return result


# my_sum([1, 2, 3])

#
# def my_sum(arr):
#     if arr != []:
#         return sum(arr)
#     else:
#         return 0


# def my_sum(arr):
#     if arr == []:
#         return 0
#     return arr[0] + sum(arr[1:])
#
#
# print(my_sum([1, 2, 3, 4, 5]))
#
#
# # 编写递归函数，计算列表包含的元素数
# def count(arr):
#     if arr == []:
#         return 0
#     else:
#         return len(arr)
#
#
# # 找出列表中最大的数
# def max_num(arr):
#     if arr == []:
#         return
#     return max(arr)
#
#
# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return qsort(less) + pivot + qsort(greater)
#
#
# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         pivot = arr[0]
#         less = []
#         greater = []
#         for i in arr[1:]:
#             if i <= pivot:
#                 less.append(i)
#             else:
#                 greater.append(i)
#         return qsort(list(less)) + [pivot] + qsort(list(greater))
#
#
# def s(arr):
#     if len(arr) == 2:
#         if arr[0] < arr[1]:
#             return arr
#         else:
#             return [arr[1]] + [arr[0]]


# 广度优先搜索示例
from collections import deque


def search_seller(name):
    que = deque()  # 创建一个队列
    que += graph[name]  # 给队列添加值
    searched = []
    while que:
        person = que.popleft()  # 从队列的第一个开始弹出元素
        if person not in searched:  # 仅当这个人没检查过时才检查
            if person_seller(person):  # 检查弹出的元素是否符合要求
                print('We found him!' + ' ' + person)
                return True
            else:  # 如果不符合要求，就扩张队列, 并接着循环
                que += graph[person]  # 将不符合条件的人加入到队列中
                searched.append(person)

    return False


# 无限循环

def person_seller(name):
    return name[0] == '1'


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = ['you']
graph['thom'] = []
graph['jonny'] = []

print(search_seller('you'))
