# bytecode.py — Python 소스가 내부적으로 어떤 바이트코드로 바뀌는지 보기
import dis  # disassembler: 바이트코드를 사람이 읽을 수 있게 출력

def add_one(a):
    b = a + 1   # 더하기 한 번
    return b    # 결과 반환

dis.dis(add_one)                             # 바이트코드 명령 목록 출력
print("raw bytes:", add_one.__code__.co_code[:8], "...")  # 실제로는 바이트 배열
print("상수 목록:", add_one.__code__.co_consts)        # 함수 안에서 쓰인 상수
print("지역 변수:", add_one.__code__.co_varnames)      # 지역 변수 이름
