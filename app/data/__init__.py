from sklearn.model_selection import train_test_split

def random_split(data_frame, train_size, seed = 0):
    train_set, test_set, train_y, test_y = train_test_split(data_frame, data_frame, train_size= train_size, random_state = seed)
    return train_set, test_set

def concat(df1, df2, columns_names=None):
    if(columns_names):
        return df1[columns_names].append(df2[columns_names])