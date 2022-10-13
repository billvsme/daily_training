# coding: utf-8
import time
import requests
import functools
import itertools

# 用三种方法实现单例
# 使用__new__
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class A(Singleton):
    pass

# 使用__call__
class Singleton2(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class A2(metaclass=Singleton2):
    pass

# 使用共享属性
class Singleton3:
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class A3(Singleton3):
    def __init__(self):
        self.data = 1

# 类装饰器
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class A4():
    pass

# import方法
class Config:
    pass

config = Config()

# 实现一个retry构造器
def retry(delays=(0, 1, 5),
          exceptions=(Exception,),
          report=lambda *args: print(args)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            problems = []
            for delay in itertools.chain(delays, [None]):
                try:
                    return func(*args, **kwargs)
                except exceptions as problem:
                    problems.append(problem)
                    if delay is None:
                        report(problems)
                        raise
                    else:
                        report(problem)
                        time.sleep(delay)
        return wrapper
    return decorator

@retry()
def req():
    return requests.get("https://vmaigcc.com")


def base_code():
    # print(req())

    print(id(A()))
    print(id(A()))

    print(id(A2()))
    print(id(A2()))
    a = Singleton3()
    a2 = Singleton3()
    a.data = 2
    print(a.data)
    print(a2.data)
    print(id(A4))
    print(id(A4))


if __name__ == '__main__':
    base_code()
