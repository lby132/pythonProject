# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정x, 삭제O) 파이썬 현재버전에서는 순서가 지켜짐

# 선언
# a = [] 리스트
# a = {} 튜플
# a = {} 딕셔너리
a = {'name': 'kim', 'phone': '01033332222', 'birth': '910123'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    "Name": 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
# 잘 사용하진 않지만 리스트[]안에 하나의 ()튜플로 넣어야 인식한다.
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ("Age", 33),
    ("Grade", 'A'),
    ("Status", True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
# a['name1'] 같은 없는 키를 출력하려고하면 keyError가 난다
print('a - ', a['name'])
# a.get('name1') 같이 없는 키를 출력하려고하면 키가 없을 경우 None이 나오기때문에 좀더 안정적으로 개발 수 있다
print('a - ', a.get('name'))
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 추가
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_keys, dict_values, dict_items : 반복문에서 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))

print()

# key, value 같이 리스트로 하나의 튜플형태로 가져옴
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)

print('a - ', c.pop('arr'))
print('c - ', c)

print()

# 아무거나 하나를 꺼내옴
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
# 다 꺼냇을땐 {} 빈값 출력
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'City' in d)

# 수정
a['test'] = 'test_dict'

print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a - ', a)