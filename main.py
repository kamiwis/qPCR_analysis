import pandas as pd

df = pd.read_csv('20221207_MCF7-KB_TNC_reg_media.csv')

averages = df.groupby(['sample', 'target']).CT.mean().reset_index()
print(averages)
