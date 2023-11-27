# 파이썬 지원 자료형
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)
tuple2 = 7, 8, 9
set = {3, 5, 7}


# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

"""
// : 목
abs(x) : 절대값
pow(x, y) x ** y = x의y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777799999999999999 # 타입을 따로 지정하지 않아도 자동으로 큰값이 입력됨.

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777799999999999999
big_int2 = 34434343443777777777779999999111111
f1 = 1.234
f1 = 3.939

# +
print(">>>>>>+")
print("big_int1 + big_int2", big_int1 + big_int2)

# 형 변환 실습
a = 3. # 소수점 뒤 0 생략 가능
b = 6
c = .7 # 소수점 앞 숫자 생략 가능
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0
print(float(True))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형으로 자동 형변환
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)

print(x,y) # 몫과 나머지가 한번에 나옴.
print(pow(5, 3), 5 ** 3)


# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 적은 정수
print(math.pi)