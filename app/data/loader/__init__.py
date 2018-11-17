import pandas as pd

def load_from_file(file_path):
    if file_path.endswith('.json'):
        return pd.read_json(file_path)
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path,encoding='ISO-8859-1',error_bad_lines=False)
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    if file_path.endswith('.pkl'):
        return pd.read_pickle(file_path)
    raise ValueError('Invalid file type')

def load_object(obj):
    return pd.DataFrame([obj,])