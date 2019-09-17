from functools import wraps, partial
from functools import wraps
from flask import abort
from flask_login import current_user

# 装饰器
# def sum_add(*args1):  # 我们要给我们的装饰器decorator，带上参数
#     def decorator(func):
#         @wraps(func)  # 加上这句，原函数func被decorator作用后，函数性质不变  ????
#         def my_sum(*args2):  # 注意，参数要和原函数保持一致，真正实行扩展功能的是外层的装饰器
#             my_s = 0
#             for n in args1:
#                 my_s = my_s + n  # 这个是我们新加的求和结果
#             return func(*args2) + my_s  # 这个，我们在原求和函数的结果上再加上s，并返回这个值
#
#         return my_sum  # 返回my_sum函数，该函数扩展原函数的功能
#
#     return decorator  # 返回我们的装饰器


# @sum_add(10, 20)  # 启用装饰器 对sum函数进行功能扩展
# def sum(*args):
#     s = 0
#     for n in args:
#         s = s + n
#     return s


# print(sum(1, 2, 3, 4, 5))
# print(sum.__name__)



# # 偏函数
# def sum(*args):
#     s = 0
#     for n in args:
#         s = s + n
#     return s
#
#
# sum_add_10 = partial(sum, 10)  # 10 作用在sum第一个参数的位置
# sum_add_10_20 = partial(sum, 10, 20)  # 10 20 分别作用在sum第一个和第二个参数的位置
# print('A____________我们看下原函数sum的函数地址入口：')
# print(sum)
# print('B______我们看下partial函数返回函数的地址入口：')
# print(partial(sum, 10))
# print(sum_add_10(1, 2, 3, 4, 5))  # --> 10 + 1 + 2 + 3 + 4 + 5 = 25
# print(sum_add_10_20(1, 2, 3, 4, 5))  # --> 10 + 20 + 1 + 2 + 3 + 4 + 5 = 45


#
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         '''decorator'''
#         print('Calling decorated function...')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @my_decorator
# def example():
#     """Docstring"""
#     print('Called example function')
#
#
# print(example.__name__, example.__doc__)



class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMIN)(f)


