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
 for i in range(len(array)-1):  # len()：返回容器中元素的数量，可以将i和j看成索引
    for j in range(len(array)-1-i):
        if array[j] > array[j+1]: # 如果前一个大于后一个，则交换
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


# if __name__ == "__main__":
#  array = [265, 494, 302, 160, 370, 219, 247, 287,
#  354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]
#  print("------->排序前<-------")
#  print(array)
#  bubble(array)
#  print("------->排序后<-------")
#  print(array)


def select_sort(array):
    for i in range(len(array)-1): # 找出最小的数放与array[i]交换
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp


if __name__ == "__main__":
    array = [265, 494, 302, 160, 370, 219, 247, 287,
    354, 405, 469, 82, 345, 319, 83, 258, 497, 423, 291, 304]
    print(array)
    select_sort(array)
    print(array)


    print("=======================================")

import time


def insertion_sort(array):
    for i in range(1, len(array)): # 对第i个元素进行插入，i前面是已经排序好的元素
        position = i # 要插入数的下标
        current_val = array[position] # 把当前值存下来
# 如果前一个数大于要插入数，则将前一个数往后移，比如5,8,12,7;要将7插入，先把7保存下来，比较12与7，将12往后移
        while position > 0 and current_val < array[position-1]:
            array[position] = array[position-1]
            position -= 1
        else: # 当position为０或前一个数比待插入还小时
            array[position] = current_val




if __name__ == "__main__":
    array = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
    print(array)
    time_start = time.time()
    insertion_sort(array)
    time_end = time.time()
    print("time: %s" % (time_end-time_start))
    print(array)





    