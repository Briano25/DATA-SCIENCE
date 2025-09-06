import numpy as np

rolls = np.random.randint(1, 7, size=10000)  # 10,000 rolls
prob_4 = np.mean(rolls == 4)
prob_even = np.mean((rolls % 2) == 0)

print(f"Estimated P(rolling a 4): {prob_4}")
print(f"Estimated P(rolling even): {prob_even}")
