import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('off_data.txt', skiprows=2)
df = pd.read_csv('off_data.txt', skiprows=2)

t = df['t']

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# theta
axes[0].plot(t, df.iloc[:, 4], label='Mass A')
axes[0].plot(t, df.iloc[:, 11], label='Mass B')
axes[0].set_ylabel('theta (deg)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# omega
axes[1].plot(t, df.iloc[:, 5], label='Mass A')
axes[1].plot(t, df.iloc[:, 12], label='Mass B')
axes[1].set_ylabel('omega (deg/s)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# alpha
axes[2].plot(t, df.iloc[:, 6], label='Mass A')
axes[2].plot(t, df.iloc[:, 13], label='Mass B')
axes[2].set_ylabel('alpha (deg/s²)')
axes[2].set_xlabel('Time (s)')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()