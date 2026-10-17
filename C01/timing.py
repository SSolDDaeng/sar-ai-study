# timing.py — 같은 계산을 "Python 반복문" vs "C로 작성된 내장 함수"로 비교
import time  # 시간 측정용 표준 모듈

N = 10_000_000  # 1천만. 숫자 사이 _ 는 가독성용 구분자(값에는 영향 없음)

t0 = time.perf_counter()   # 고해상도 타이머 시작
total = 0
for i in range(N):         # 0, 1, ..., N-1 을 하나씩 꺼냄
    total += i             # 매 반복마다 바이트코드 여러 개가 인터프리터에서 해석됨
t1 = time.perf_counter()

total2 = sum(range(N))     # 반복을 C 코드 안에서 처리
t2 = time.perf_counter()

print("반복문 결과:", total, f"({t1 - t0:.3f} s)")
print("sum() 결과 :", total2, f"({t2 - t1:.3f} s)")
print("공식 N(N-1)/2:", N * (N - 1) // 2)  # 손계산과 비교
print("속도 비:", round((t1 - t0) / (t2 - t1), 1), "배")
