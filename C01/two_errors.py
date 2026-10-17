# two_errors.py — Python은 "실행하는 순간" 줄 단위로 오류를 발견함
print("1번 줄 실행")          # 정상 실행

def never_called():
    return undefined_name + 1  # 정의되지 않은 이름. 하지만 이 함수는 호출되지 않음

x = 10                       # x는 정수(int)를 가리킴
print("x의 타입:", type(x))
x = "열"                     # 같은 이름 x가 이제 문자열(str)을 가리킴 — C++에선 불가능
print("x의 타입:", type(x))

print("곧 오류가 납니다")
y = x + 1                    # str + int → TypeError가 "이 줄을 실행할 때" 발생
print("이 줄은 실행되지 않음")
