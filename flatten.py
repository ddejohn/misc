def flatten(data: list) -> list:
    """Recursively flatten 'data' into a 1D list"""
    data = sum(data, [])
    if not isinstance(data[0], list):
        return data
    return flatten(data)
# end