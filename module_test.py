# 모듈 사용 실습
import sys

# 모듈 경로 삽입 전
print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
sys.path.append("/Users/lby/PycharmProjects/MathTest")
# 모듈 경로 삽입 후
print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10, 3))

import chapter06_02

# chapter06_02 의 코드가 자동으로 사용되지 않고 이렇게 호출해야만 사용할 수 있게 만들었다.
print(chapter06_02.add(10, 100000))