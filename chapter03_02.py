# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
# I'm B

print("I'm B")
print("I\'m B")

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력
multi_str = \
"""
String
Multi line
Test
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple!"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # y가 포함되어 있는지 확인
print('i' in str_o1)
print('P' not in str_o2) # 대문자 P가 포함되어 있지 않은지 확인

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫번째 글자를 대문자로변환
print("endswith?: ", str_o2.endswith("!"))
print("replace", str_o1.replace("thon", ' Good'))
print("sorted:", sorted(str_o1))
print("split:", str_o4.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))

# 슬라이싱 연습
print(str_s1[0:3])
print(str_s1[5:11])
print(str_s1[:len(str_s1)]) # 0부터 str_s1의 길이 까지
print(str_s1[:len(str_s1)-1])
print(str_s1[1:4:2]) # 1부터 4인덱스 까지 2칸씩 점프해서 가져옴
print(str_s1[-5:])
print(str_s1[1:-2]) # 1부터 맨끝에서 -2만큼 출력
print(str_s1[::2]) # 처음부터 끝까지 2칸 간격으로 점프해서 가져옴 str_s1[0:0:2] 와 같다
print(str_s1[::-1]) # 음수는 오른쪽에서 왼쪽으로 출력

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # 아스키코드로
print(chr(122)) # 문자로