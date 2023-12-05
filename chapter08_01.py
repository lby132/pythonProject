# 내장(Built-in) 함수
# 자주 사용하는 함수 위주
# str(), int(), tuple() 등

# 절대값
# abs()

print(abs(-3))

# all : iterable 요소 검사(참, 거짓)
print(all([1,2,''])) # 모두 true여야 true를 반환함 and
print(any([1,2,0])) # 하나라도 true이면 true를 반환 or

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6]))) # lambda 식으로 변경

# id : 객체의 주소값(래퍼런스) 반환
print(id(int(5)))
print(id(4))

# len : 요소의 길이를 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7]))

# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('pythonstudy'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_pos(x):
    return abs(x)

print(list(map(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))

