import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./data/coding-environment-exercise.csv')
data = df.to_numpy().T
plt.plot(data[0], data[1])
plt.savefig('plot.png', bbox_inches='tight')