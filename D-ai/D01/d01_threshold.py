# D01 실습: "사람이 정한 규칙" vs "데이터로 학습한 규칙" — 바다/선박 화소 분류
# 실행: python d01_threshold.py   (numpy, matplotlib 필요)
import numpy as np                      # 배열 계산 라이브러리
import matplotlib.pyplot as plt         # 그래프 라이브러리

rng = np.random.default_rng(seed=0)     # 난수 생성기. seed를 고정하면 매번 같은 결과가 나옴

# ---------- 1) 데이터 만들기 (가짜 SAR 화소 진폭) ----------
def make_data(m, sea_scale=1.0, ship_scale=2.5, ship_ratio=0.3):
    """m개의 화소를 만든다. 반환: x(진폭), y(정답: 0=바다, 1=선박)"""
    m_ship = int(m * ship_ratio)                              # 선박 화소 개수
    m_sea = m - m_ship                                        # 바다 화소 개수
    x_sea = rng.rayleigh(scale=sea_scale, size=m_sea)         # 바다: 약한 진폭 (레일리 분포는 A50에서 배움)
    x_ship = rng.rayleigh(scale=ship_scale, size=m_ship)      # 선박: 더 강한 진폭
    x = np.concatenate([x_sea, x_ship])                       # 입력 x 하나로 합침
    y = np.concatenate([np.zeros(m_sea, int), np.ones(m_ship, int)])  # 정답 y
    return x, y

x_train, y_train = make_data(2000)      # 학습용 데이터 (모델이 "보고 배우는" 예제)
x_test, y_test = make_data(2000)        # 시험용 데이터 (학습 때 한 번도 안 본 새 데이터)

# ---------- 2) 모델: 임계값 하나로 분류 ----------
def model(x, theta):
    """f(x; θ): 진폭이 θ보다 크면 선박(1), 아니면 바다(0). 파라미터는 θ 하나뿐."""
    return (x > theta).astype(int)

def loss(y_hat, y):
    """손실 L: 틀린 비율(0~1). 작을수록 좋음."""
    return np.mean(y_hat != y)

# ---------- 3) 규칙 기반: 사람이 θ를 정함 ----------
theta_rule = 4.0                        # "진폭 4 넘으면 선박" — 사람이 감으로 정한 값
print(f"[rule]    theta = {theta_rule:.2f}, test error = {loss(model(x_test, theta_rule), y_test):.3f}")

# ---------- 4) 학습: 데이터를 보고 손실이 가장 작은 θ를 찾음 ----------
candidates = np.linspace(0, 8, 801)                         # 후보 θ: 0.00, 0.01, ..., 8.00
train_losses = np.array([loss(model(x_train, t), y_train) for t in candidates])  # 후보마다 학습 손실 계산
theta_star = candidates[np.argmin(train_losses)]            # 손실이 최소인 θ = θ*
print(f"[learned] theta* = {theta_star:.2f}, train error = {train_losses.min():.3f}, "
      f"test error = {loss(model(x_test, theta_star), y_test):.3f}")

# ---------- 5) 추론: θ*를 고정하고 새 화소 몇 개를 분류 ----------
x_new = np.array([0.5, 1.8, 2.6, 5.0])                      # 새로 들어온 화소 진폭
print("[inference] x_new =", x_new, "-> y_hat =", model(x_new, theta_star))

# ---------- 6) 분포가 바뀌면? (파도가 높은 날: 바다가 더 밝아짐) ----------
x_storm, y_storm = make_data(2000, sea_scale=1.6)           # 학습 때와 다른 조건
print(f"[storm]   theta* = {theta_star:.2f}, test error = {loss(model(x_storm, theta_star), y_storm):.3f}")

# ---------- 7) 그림 4 ----------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
bins = np.linspace(0, 9, 60)
ax1.hist(x_train[y_train == 0], bins, alpha=0.6, label="sea (y=0)", color="tab:blue")
ax1.hist(x_train[y_train == 1], bins, alpha=0.6, label="ship (y=1)", color="tab:orange")
ax1.axvline(theta_rule, color="gray", ls="--", label=f"rule θ = {theta_rule:.1f}")
ax1.axvline(theta_star, color="red", label=f"learned θ* = {theta_star:.2f}")
ax1.set_xlabel("pixel amplitude x"); ax1.set_ylabel("count"); ax1.set_title("(a) training data")
ax1.legend()
ax2.plot(candidates, train_losses, color="tab:purple")
ax2.axvline(theta_star, color="red")
ax2.set_xlabel("threshold θ"); ax2.set_ylabel("training loss L(θ) = error rate")
ax2.set_title("(b) training = find θ with the lowest loss")
fig.suptitle("Figure 4. Learning a single parameter from data")
plt.tight_layout(); plt.savefig("fig4_threshold.png", dpi=150)
print("saved fig4_threshold.png")