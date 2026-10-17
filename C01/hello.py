import sys       # 인터프리터 자신에 대한 정보를 담은 표준 모듈
import platform  # 운영체제·CPU 정보를 담은 표준 모듈

print("Hello, Python!")                    # 화면에 문자열 출력
print("버전      :", sys.version.split()[0])  # 예: 3.12.x (공백 앞부분만)
print("실행 파일 :", sys.executable)          # 이 코드를 실행 중인 python 프로그램의 경로
print("운영체제  :", platform.system())       # Linux
print("구현      :", platform.python_implementation())  # CPython
