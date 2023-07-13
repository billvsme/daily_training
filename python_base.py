# coding: utf-8
import time
import logging
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


# 不带参数装饰器
def runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        rest = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__, end_time-start_time)
        return rest

    return wrapper


# 带参数装饰器
def runtime2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            rest = func(*args, **kwargs)
            end_time = time.time()
            print(text, end_time-start_time)
            return rest


# 不带和带参数都可以的装饰器
def runtime3(func=None, *, text="runtime"):
    if not func:
        return functools.partial(runtime3, text=text)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        rest = func(*args, **kwargs)
        end_time = time.time()
        print(text, end_time-start_time)
        return rest

    return wrapper


# 类装饰器
class runtime4:
    def __init__(self, text):
        self.text = text

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            rest = func(*args, **kwargs)
            end_time = time.time()
            print(self.text, end_time-start_time)
            return rest

        return wrapper


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


# 实现一个即可以带参数也可以不带参数带装饰器
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return functools.partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged(level=logging.ERROR, name="example")
@logged
def add(x, y):
    return x + y


def singleton_code():
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


# 切片
def slice_code():
    a = list(range(10))
    # 取前5个
    print(a[:5])

    # 取偶数个, step
    print(a[::2])

    # 负索引
    # 负索引和普通索引一样，先转化成正值在看
    print(a[5:-1])

    # 负数step
    # 负step时候，start当作无穷大，end当作无穷小，还是作开右闭合
    print(a[5::-1])
    print(a[:4:-2])


def base_code():
    # print(req())
    print(add(1, 2))
    singleton_code()
    slice_code()


if __name__ == '__main__':
    base_code()
