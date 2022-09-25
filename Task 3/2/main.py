import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')
df = df.replace(np.nan, -1)
df.to_csv('modified_dataset.csv')
