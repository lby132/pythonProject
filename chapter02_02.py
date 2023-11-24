n = 700

print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 타입에 맞는 오브젝트 생성

# 예1)
print(300)
print(int(300))
print(type(300))

# 예2)
n = 777
print(n, type(n))
print()

m = n
print(m, n)
print(type(m), type(n))
print()

m = 400

print(m, n)
print(type(m), type(n))
print()

# 같은 오브젝트 참조
m = 800
n = 655

print(id(m))
print(id(n))
print()

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언


