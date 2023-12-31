# 모듈
# Module : 함수, 변수, 클래스 등의 파이썬 구성 요소 등을 모아놓은 파일

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y


# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)


# __name__ 사용
# 내 자신을 바로 실행할때 __main__ 이 실행된다.
# 이코드는 외부에서 import를 해서 자동으로 실행되지 않게 해주는 코드이다.
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print('-' * 15)
