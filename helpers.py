import pandas as pd

def find_value(df: pd.DataFrame, sample: str, target: str, val_to_find: str):
    '''Returns specific value of interested from df.'''
    try:
        data = df[(df['sample'] == sample) & (df['target'] == target)].reset_index()
    except KeyError:
        print('Sample or target not found in data frame.')
    else:
        try:
            if val_to_find == 'CT':
                value = round(data.iloc[0].CT, 3)
            elif val_to_find == 'dCT':
                value = round(data.iloc[0].dCT, 3)
            elif val_to_find == 'ddCT':
                value = round(data.iloc[0].ddCT, 3)
        except (KeyError, IndexError):
            print('Value of interest not found in data frame.')
        else:
            return value


def find_dCT(averages: pd.DataFrame, housekeeping_gene: str,
             sample: str, target: str) -> dict:
    """Returns dictionary containing deltaCT result."""
    # Get CT value for housekeeping gene.
    hk_ct = find_value(averages, sample, housekeeping_gene, 'CT')

    # Get CT value for target gene.
    target_ct = find_value(averages, sample, target, 'CT')

    dCT = target_ct - hk_ct
    # print(dCT)
    return {'sample': sample, 'target': target, 'dCT': dCT}


def find_ddCT(all_dCTs, sample, TARGET):
    """Returns dictionary containing delta delta CT results."""
