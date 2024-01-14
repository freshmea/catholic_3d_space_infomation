from functools import wraps


def trace(x):  # 호출할 함수를 매개변수로 받음
    def real_decorator(func):
        @wraps(func)  # 이것을 하면 디버깅할 때 도움이 됨.
        def wrapper():
            print(func.__name__, "함수 시작", x)  # __name__으로 함수 이름 출력
            func()  # 매개변수로 받은 함수를 호출
            print(func.__name__, "함수 끝", x)

        return wrapper  # wrapper 함수 반환

    return real_decorator


@trace(3)  # @데코레이터
def hello():
    """hello docstring"""
    print("hello")


@trace(2)  # @데코레이터
def world():
    """world docstring"""
    print("world")


def main():
    hello()  # 함수를 그대로 호출
    world()  # 함수를 그대로 호출
    print(hello.__name__)
    print(world.__name__)
    print(hello.__doc__)
    print(world.__doc__)
    print(world.__dict__)


if __name__ == "__main__":
    main()
