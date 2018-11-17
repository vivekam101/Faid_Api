def has_data(df, col):
    return ~df[col].isnull()

COMMAND_MAP = {
    "has_data": has_data
}

def transform(df, col, command):
    _map_fn = COMMAND_MAP.get(command)
    if not _map_fn:
        return df[col]

    return _map_fn(df, col)
