import numpy as np
def clar_all_empty_values(data_frame):
    data_frame = data_frame.replace('nan', np.nan)
    return data_frame.replace('', np.nan)

def clear_invalid_data(data_frame, col):
    for rep in ['', 'NULL', '0', 0]:
        data_frame[col] = data_frame[col].replace(rep, np.nan)