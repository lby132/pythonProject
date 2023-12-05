# 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.

# NameError : 참조 없음
# a = 10
# b = 15
# print(c) # NameError

# ZeroDivisionError
# print(100 / 0) # ZeroDivisionError

# KeyError
# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby']) # KeyError

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time

# print(time.time2())  # 모듈안에 정의 되어 있지 않은 함수를 호출할때 에러

# ValueError
# 어떤 시퀀스안에서 데이터를 찾으려고 하는데 존재하지 않을때 발생하는 에러
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.tx') # 가져 오려는 파일이 없으면 FileNotFoundError

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2] # 리스트 형식이라 가변형
# y = (1, 2) # 튜플형식이라 불변형
# print(x + y) # 불변형과 가변형이기 때문에 내부적 구조로 인해 데이터가 하나로 합쳐질 수 없어서 TypeError

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에러명2:
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
try:
    z = 'Kim'
    x = name.index(z)
    print('Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok!')

print()

# 예제2
try:
    z = 'Cho'
    x = name.index(z)
    print('Found it! {} in name'.format(z, x + 1))
except Exception:
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok!')

print()


# 예제3
try:
    z = 'Cho'
    x = name.index(z)
    print('Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e) # 에러 내용 출력
    print('Not found it! - Occurred ValueError!')
else:
    print('Ok! else')
finally:
    print('Ok! finally')

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok Pass!')
    else:
        raise ValueError # 직접적으로 에러발생
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')

