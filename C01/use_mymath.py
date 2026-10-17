# use_mymath.py — 모듈을 import 하면 __pycache__/ 에 .pyc(바이트코드 캐시)가 생김
import mymath   # 처음 import 할 때 mymath.py 전체가 위에서부터 실행됨
import mymath   # 두 번째 import는 이미 불러온 모듈을 재사용 → 다시 실행되지 않음

print("square(7) =", mymath.square(7))
