from functools import wraps


def trace(func):  # 호출할 함수를 매개변수로 받음
    @wraps(func)  # 이것을 하면 디버깅할 때 도움이 됨.
    def wrapper(*args, **kwargs):
        print(func.__name__, "함수 시작")  # __name__으로 함수 이름 출력
        func(*args, **kwargs)  # 매개변수로 받은 함수를 호출
        print(func.__name__, "함수 끝")

    return wrapper  # wrapper 함수 반환


@trace  # @데코레이터
def hello():
    print("hello")


@trace  # @데코레이터
def world():
    print("world")


hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출
