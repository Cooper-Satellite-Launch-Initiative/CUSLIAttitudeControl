# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:24:04 2026

@author: Adin Sacho-Tanzer
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


detumbling_df = pd.read_excel("WorkingDetumbling.xlsx")
nadir_df = pd.read_excel("WorkingPIDNadir.xlsx")

#%%
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(1)"], label="x")
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(2)"], label="y")
plt.plot(detumbling_df["time.1"]/60, detumbling_df["Spacecraft Dynamics:4(3)"], label="z")
plt.title("Detumbling: angular velocity about each axis")
plt.ylabel("Angular velocity (deg/s)")
plt.xlabel("Time (min)")
plt.xlim(0, 120)
plt.grid()
plt.legend(loc="best")
plt.axhline(1, linestyle="--")
plt.show()


plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(1,1)"]), label="x")
plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(2,1)"]), label="y")
plt.plot(nadir_df["time"]/3600, np.rad2deg(nadir_df["Attitude Control:1(3,1)"]), label="z")
plt.title("Nadir pointing: error euler angle about each axis")
plt.ylabel("Error (deg)")
plt.xlabel("Time (hours)")
plt.grid()
plt.legend(loc="best")
plt.axhline(8, linestyle="--")
plt.show()
