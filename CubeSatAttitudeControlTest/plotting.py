# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:24:04 2026

@author: Adin Sacho-Tanzer
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#%%
detumbling_df = pd.read_excel("WorkingDetumbling.xlsx")
nadir_df = pd.read_excel("WorkingPIDNadir.xlsx")
sun_df = pd.read_excel("WorkingPiDSun.xlsx")

#%%
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(1)"], label="x")
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(2)"], label="y")
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(3)"], label="z")
plt.title("Detumbling: angular velocity about each axis")
plt.ylabel("Angular velocity (deg/s)")
plt.xlabel("Time (min)")
plt.xlim(0, 120)
plt.grid()
plt.axhline(0.1, linestyle="--", label="0.1 deg/s")
plt.legend(loc="best")
plt.tight_layout()
plt.show()


plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(1,1)"]), label="x")
plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(2,1)"]), label="y")
plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(3,1)"]), label="z")
plt.title("Nadir pointing: error euler angle about each axis")
plt.ylabel("Error (deg)")
plt.xlabel("Time (hours)")
plt.grid()
plt.axhline(8, linestyle="--", label="8 deg")
plt.legend(loc="best")
plt.tight_layout()
plt.show()


plt.plot(sun_df["time.1"]/3600, sun_df["SunAngle"], label="Sun angle (deg)")
plt.title("Sun angle")
plt.ylabel("Sun angle (deg)")
plt.xlabel("Time (hours)")
plt.xlim(0, 4)
plt.grid()
plt.axhline(8, linestyle="--", label="8 deg")
plt.legend(loc="best")
plt.tight_layout()
plt.show()