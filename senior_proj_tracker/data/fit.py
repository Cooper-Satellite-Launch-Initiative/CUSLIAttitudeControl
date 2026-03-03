import numpy as np
from scipy.optimize import curve_fit, minimize_scalar
from scipy.integrate import solve_ivp
import pandas as pd
import matplotlib.pyplot as plt

# ===== INPUTS =====
I = 2.83e-5  # moment of inertia (kg·m²) — estimated
B = 22138.61023e-9  # magnetic field (T)
theta_north = np.radians(167.0715)  # north direction (rad)

off_file = "off_data_trimmed.txt"
on_file = "on_data_trimmed.txt"

# ===== PARSE DATA =====
def load(file):
    df = pd.read_csv(file, skiprows=2, header=None)
    t = pd.to_numeric(df[0], errors='coerce').values
    theta = np.radians(pd.to_numeric(df[4], errors='coerce').values)
    mask = ~np.isnan(t) & ~np.isnan(theta)
    return t[mask], theta[mask]

SPEED_FACTOR = 20

t_off, theta_off = load(off_file)
t_on, theta_on = load(on_file)
t_off *= SPEED_FACTOR
t_on *= SPEED_FACTOR

# ===== OFF ANALYSIS: fit damped sinusoid =====
def damped(t, theta0, A, n, wd, phi):
    return theta0 + A * np.exp(-n * t) * np.cos(wd * t + phi)

p0 = [np.mean(theta_off), np.ptp(theta_off)/2, 0.1, 2*np.pi/2, 0]
popt, _ = curve_fit(damped, t_off, theta_off, p0=p0, maxfev=50000)
theta0, A_fit, n, wd, phi = popt

b = 2 * I * n
k = I * (wd**2 + n**2)

print("=== OFF ANALYSIS ===")
print(f"theta0 = {np.degrees(theta0):.4f} deg")
print(f"n = {n:.6f} s⁻¹")
print(f"wd = {wd:.6f} rad/s")
print(f"b = {b:.6e}")
print(f"k = {k:.6e}")

plt.figure()
plt.plot(t_off, np.degrees(theta_off), 'b.', markersize=2, label='Data')
t_fit = np.linspace(t_off[0], t_off[-1], 1000)
plt.plot(t_fit, np.degrees(damped(t_fit, *popt)), 'r-', label='Fit')
plt.xlabel('Time (s)')
plt.ylabel('θ (deg)')
plt.title('OFF Analysis')
plt.legend()
plt.tight_layout()
plt.savefig('off_fit.png', dpi=150)
plt.show()

# ===== ON ANALYSIS =====
theta_eq = np.mean(theta_on[-len(theta_on)//35:])
m_ss = -k * (theta_eq - theta0) / (B * np.sin(theta_eq - theta_north))

print("\n=== ON ANALYSIS: STEADY STATE ===")
print(f"theta_eq = {np.degrees(theta_eq):.4f} deg")
print(f"m = {m_ss:.6e} A·m²")

def simulate(m):
    def ode(t, y):
        th, thdot = y
        thddot = (-b * thdot - k * (th - theta0) - m * B * np.sin(th - theta_north)) / I
        return [thdot, thddot]
    sol = solve_ivp(ode, [t_on[0], t_on[-1]], [theta_on[0], 0], t_eval=t_on, max_step=0.01)
    return sol.y[0]

def error(m):
    th_sim = simulate(m)
    return np.sum((th_sim - theta_on)**2)

res = minimize_scalar(error, bounds=(-m_ss*100, m_ss*100), method='bounded')
m_ode = res.x

print("\n=== ON ANALYSIS: ODE FIT ===")
print(f"m = {m_ode:.6e} A·m²")

plt.figure()
plt.plot(t_on, np.degrees(theta_on), 'b.', markersize=2, label='Data')
plt.plot(t_on, np.degrees(simulate(m_ss)), 'r-', label=f'Steady state m={m_ss:.4e}')
plt.plot(t_on, np.degrees(simulate(m_ode)), 'g--', label=f'ODE fit m={m_ode:.4e}')
plt.xlabel('Time (s)')
plt.ylabel('θ (deg)')
plt.title('ON Analysis')
plt.legend()
plt.tight_layout()
plt.savefig('on_fit.png', dpi=150)
plt.show()