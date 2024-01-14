from functools import wraps


class Trace:
    def __init__(self, x):  # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.x = x  # 호출할 함수를 속성 func에 저장

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__name__, "함수 시작", self.x)  # __name__으로 함수 이름 출력
            r = func(*args, **kwargs)  # 속성 func에 저장된 함수를 호출
            print(func.__name__, "함수 끝", self.x)
            return r

        return wrapper  # wrapper 함수 반환


@Trace(3)  # @데코레이터
def hello():
    """hello docstring"""
    print("hello")


def main():
    hello()  # 함수를 그대로 호출
    print(hello.__doc__)
    print(hello.__name__)


if __name__ == "__main__":
    main()
