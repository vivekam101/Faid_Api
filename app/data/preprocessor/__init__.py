from app.data.preprocessor.tranformer import transform
from app.data.utils import print_columns

def preprocess(df, tasks):
    _df = df
    if not tasks:
        return _df
    for _task in tasks:
        _df = _preprocess(_df, _task)
    return _df

def _preprocess(df, task):
    _df =df
    if not task:
        return _df
    _type = task.get("type")
    if not _type:
        return _df
    _column = task.get("column")
    _target = task.get("target", _column)
    _command = task.get("command")
    print("{}: Preprocessing \"{}\" with command \"{}\" to {}".format(_column, _type, _command, _target))
    if (not type(_column) is list) and _column not in _df:
        _df[_column] = None
    if _type == "apply":
        _df[_target] = _df[_column].apply(_command, axis=1)
    elif _type == "transform":
        _df[_target] = transform(_df, _column, _command)
    return _df