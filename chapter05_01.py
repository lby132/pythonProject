# 파이썬 함수식 및 람다(Lambda)

# 예제1
def first_func(w):
    print("Hello,", w)

word = "Goodboy"

first_func(word)

# 예제2
def return_func(w):
    return "Hello, " + str(w)

x = return_func('Goodboy2')
print(x)

# 예제3(다중반환)
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
mul = func_mul(10)
print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(type(q), list(q))

# 리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul2(20)

print(type(p), p, set(p))

# 딕셔너리 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1':y1, 'v2':y2, 'v3':y3}

d = func_mul2(30)

print(type(d), d)

# 중요
# *args **kwargs

# *args(언패킹)
# 가변인자, 튜플
def args_func(*args): # 매개변수 명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

# **kwargs(언패킹)
# 가변인자, 딕셔너리
def kwargs_func(**kwargs): # 매개변수 명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Cho')

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
# func_in_func(1000) 중첩함수는 밖에서 사용할 수 없음

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x, y):
#     return x * y

# lambda x, y: x*y

# 일반적 함수 -> 변수
def mul_func(x, y):
    return x * y

print(mul_func(20, 50))
print()

mul_func_var = mul_func
print(mul_func_var(20, 50))
print()

# 람다 함수 -> 할당
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50,50))

def func_final(x, y, func):
    print('>>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y: x * y)
func_final(10, 20, lambda_mul_func)
func_final(10, 20, mul_func_var)