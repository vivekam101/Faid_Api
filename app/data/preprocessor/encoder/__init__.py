from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from pandas.api.types import CategoricalDtype

class ML_Encoder(object):
    def __init__(self):
        self.encoder = None
        self.dtype = None
        self.default_value = None

    def encode(self, df):
        pass
    def transform(self, value):
        pass

class ML_Label_Encoder(ML_Encoder):
    def __init__(self):
        super(ML_Label_Encoder, self).__init__()
        self.encoders = {}
        self.columns = []

    def encode(self, df, target):
        _columns = df.select_dtypes([object,]).columns.tolist()
        if len(_columns) > 0:
            self.columns = _columns
            for _col in self.columns:
                if _col == target:
                    self.columns.remove(target)
                    continue
                df[_col] = df[_col].apply(str).fillna(self.default_value).astype(object)
                _encoder = LabelEncoder()
                self.encoders[_col] = _encoder
                _encoder.fit(list(df[_col].values)+[self.default_value])
                df[_col]=_encoder.transform(df[_col])

    def transform(self, df):
        for _col in self.columns:
            _encoder = self.encoders[_col]
            if not _col in df.columns:
                continue
            
            df[_col] = df[_col].apply(str).fillna(self.default_value).astype(object)
            _new_classes = [_cl for _cl in df[_col] if not _cl in _encoder.classes_]
            if len(_new_classes) >0:
                df[_col] = df[_col].apply(lambda x: self.default_value if x in _new_classes else x)
            df[_col]=_encoder.transform(df[_col])
