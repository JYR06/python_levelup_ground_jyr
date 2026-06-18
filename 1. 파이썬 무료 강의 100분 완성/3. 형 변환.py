# 문자 -> 정수, 실수
print(int("2"))       # 2
print(float("1.5"))   # 1.5

# 숫자 -> 문자
print(str(2))         # "2"

# 실수 -> 정수 (버림 발생)
print(int(2.5))       # 2

# (10:03 구간) 불리안(Boolean) 변환
print(bool("hello"))  # True (값이 있음)
print(bool(""))       # False (값이 없음)
print(bool(1))        # True (0이 아닌 숫자)
print(bool(0))        # False (0)
print(bool(None))     # False (값이 없음)