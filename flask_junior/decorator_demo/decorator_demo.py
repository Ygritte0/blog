# encoding: utf-8

from functools import wraps


# 装饰器函数本质上就是一个函数
# 装饰器有两个特别的点
# 1. 参数是个函数
# 2. 返回值也是一个函数

# 在打印run之前，先打印hello world
# 在所有函数执行前，都先打印hello world


# 1. 装饰器的使用时通过@符号，放在函数的上面
# 2. 装饰器中定义的函数要使用 *args, **kwargs这对兄弟的组合， 并且在这个函数
# 中执行原始函数的时候也要把*args, **kwargs传进去。
# 3. 要使用functools.wraps，在装饰器中的函数上把传进来的参数函数进行一个包裹，
# 这样就不会丢失原来函数的__name__等属性


def my_log(func):
    @wraps(func)  # 保留被装饰函数的名称
    def wrapper(*args, **kwargs):
        print('hello world')
        func(*args, **kwargs)

    return wrapper  # 注意：该返回值函数没有（）,因为此处只是返回一个函数，而不用执行该函数


@my_log
def run():
    print('run')


# run = my_log(run) = wrapper
#
# run()
# # 等于
# wrapper()

# run()


# run.__name__ 代表run这个函数的名称
print(run.__name__)


@my_log
def add(a, b):
    c = a + b
    print(u'结果是：%s' % c)


add(1, 2)
