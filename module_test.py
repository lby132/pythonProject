# 모듈 사용 실습
import sys

# 모듈 경로 삽입 전
print(sys.path)

print(type(sys.path))

# 모듈 경로 삽입
sys.path.append('/Users/lby/PycharmProjects/pythonProject/MathTest')
# 모듈 경로 삽입 후
print(sys.path)

# import test_module