def print_columns(df, col_filter=None):
    for _col in df.columns.tolist():
        if col_filter is None or col_filter in _col:
            print(_col)