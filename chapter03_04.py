# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) 불변

# 선언

a = ()
b = (1)

print(type(a), type(b)) # 원소가 하나일땐 int로 됨.
b = (1,) # 원소가 하나일때 콤마를 찍어주어야 튜플이된다.
print(type(b))

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>')
print('d - ',  d[1])
print('d - ',  d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 수정x
# d[0] = 1500 # 에러발생

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', d[2][1:3])

# 튜플 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print()

# 튜플 함수
a = (5, 2, 3, 1, 4, 2)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))
print()

# 패킹 & 언패킹

# 패킹
t = ('foo', 'bar', 'baz', 'qux') # 하나로 묶는게 패킹
print(t)
print(t[0])
print(t[-1])

# 언패킹
(x1, x2, x3, x4) = t # 패킹된 t의 각각의 원소를 x1, x2, x3, x4에 할당해주는게 언패킹

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)
print()

# 패킹 & 언패킹
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)