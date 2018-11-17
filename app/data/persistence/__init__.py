import pickle

def save_frame(data_frame, file_path):
    if file_path.endswith('.json'):
        data_frame.to_json(file_path)
    elif file_path.endswith('.csv'):
        data_frame.to_csv(file_path)
    elif file_path.endswith('.xlsx'):
        data_frame.to_excel(file_path)
    elif file_path.endswith('.pkl'):
        data_frame.to_pickle(file_path)
    else:
        data = data_frame.to_str()
        with open(file_path, mode='w') as f:
            f.write(data)

def dump(model, file_name):
    with open(file_name,"wb") as filehandler:
        pickle.dump(model, filehandler, protocol=2)
    
def load(file_name):
    with open(file_name,"rb") as filehandler:
        model = pickle.load(filehandler)
    return model