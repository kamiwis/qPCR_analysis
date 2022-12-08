import pandas as pd
from helpers import find_dCT, find_value

HOUSEKEEPING_GENE = 'ACTB'
TARGET = 'TNC2'

# Load data.
df = pd.read_csv('20221207_MCF7-KB_TNC_reg_media.csv')

# Find average CT for each sample and target.
averages = df.groupby(['sample', 'target']).CT.mean().reset_index()
# print(averages)

# Populate list of all samples in dataset.
samples = averages['sample'].unique()
controls = [c for c in samples if c[:3] == 'SCR']
#print(controls)

# Calculate dCT values and save as list of dicts.
all_dCTs_list = []
for sample in samples:
    dCT = find_dCT(averages, HOUSEKEEPING_GENE, sample, TARGET)
    all_dCTs_list.append(dCT)
# Save all dCTs as DataFrame.
all_dCTs = pd.DataFrame(all_dCTs_list)
print(all_dCTs.head(5))

# Find average of control sample dCTs.
total_control_dCT = 0
for control in controls:
    curr_dCT = all_dCTs[(all_dCTs['sample'] == control)].reset_index().iloc[0].dCT
    total_control_dCT += curr_dCT
control_dCT = total_control_dCT / len(controls)
# print(control_dCT)

# all_ddCTs_list = []
# for sample in samples:
#     ddCT = find_ddCT(all_dCTs, sample, TARGET)
#     all_ddCTs_list.append(ddCT)
# all_ddCTs = pd.DataFrame(all_ddCTs_list)
