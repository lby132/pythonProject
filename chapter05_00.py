# 파이썬 함수

# 함수
# 예제1: 매개변수가 필요하지 않은 함수
def function1():
    print('ex1 call')

# 예제2: 매개변수가 필요한 함수
def function2(a, b):
    print('ex2 call', a,b)

# 예제3: 결과값 반환 X
def function3(x, y):
    print('ex3 call', x, y)

# 예제4: 결과값 반환 O
def function4(x, y):
    return x + y;

# 실행
function1()
function2(1,2)
function3(10,100)
r = function4(50, 50)
print('ex4 call', r)
