# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : r, 바이너리 모드 : b
# 상대 경로('../, ./'), 절대 경로('/Users/pythonProject/python_basic')

# 파일 읽기(read)
# 예제1

# f = open('/Users/lby/PycharmProjects/pythonProject/resource/it_news.txt') # 절대경로
f = open('./resource/it_news.txt', 'rt', encoding='UTF-8') # rt: 텍스트로 읽기, rb: 바이너리로 읽기. t는 디폴트여서 r만 써주면 rt가 됨
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 파일 읽어오기
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    # 위의 예제를 with을 써서 더 간결하게 표현할 수 있다.
    # 들여쓰기 안에서 open한 파일의 정보를 편하게 읽어올 수 있고 close() 함수를 호출하지 않아도 자동으로 닫힌다.
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10Byte 읽기
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()

# 예제4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
print('===============')
print()

# 예제5
# readLines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'rt', encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')

print()


# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')


# 예제2
with open('./resource/contents1.txt', 'a') as f: # 기존 파일에 append 됨
    f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents1.txt', 'w') as f:
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents3.txt', 'w') as f:
    # print()함수 안에 있는 글이 콘솔이 아닌 contents3.txt 파일에 출력된다..
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)