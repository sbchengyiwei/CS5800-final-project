import numpy as np
import pandas as pd

distance = pd.read_csv("./distance.csv", header = None)
distance_arr = distance[2].to_numpy()

speed = pd.read_csv("./speed_factor.csv", header = None)
speed_arr = speed[2].to_numpy()

multiplied = distance_arr * speed_arr

def trunc(values, decs=0):
    return np.trunc(values*10**decs)/(10**decs)

distance[2] = trunc(multiplied, decs=0)

# df = pd.DataFrame(multiplied)

distance.to_csv("time.csv", index=False, header=None)