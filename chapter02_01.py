# print 사용법
print('P','Y','T','H','O','N', sep='-')
print()

# separator 옵션
print('python', 'google.com', sep='@')
print()

# end 옵션 으로 줄바꿈 하지 않고 하나의 라인 출력
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# file 옵션
import sys
print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.143423434343434))
print('%1.3f' % (3.143423434343434))
print('{:f}'.format(3.143423434343434))
print('%06.2f' % (3.143423434343434))
print('{:06.2f}'.format(3.143423434343434))

x = 50
y = 50
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3
print(f'n = {n}, s = {text}, sum = {x+y}')

# 구분기호
m = 100000000

print(f'm : {m:,}')

print()
print()

# 정렬
# ^ : 가운데 , < : 왼쪽정렬, > : 오른쪽정렬

t = 20

print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")

print()
print()

print(f"t center : {t:-^10}")
print(f"t center : {t:*^10}")
print(f"t center : {t:#<10}")
