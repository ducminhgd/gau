from collections.abc import MutableMapping, MutableSequence


def flat(data, parent_key='', sep='.') -> dict:
    """
    Recursively flattens a nested dictionary or list into a single-level dictionary.

    Parameters:
        data (dict or list): The nested dictionary or list to be flattened.
        parent_key (str, optional): The key of the parent dictionary. Defaults to an empty string.
        sep (str, optional): The separator used to concatenate the keys. Defaults to '.'.

    Returns:
        dict: A single-level dictionary where the keys are the flattened keys from the nested dictionary or list, and the values are the corresponding values.

    Examples:
        >>> data = {'a': 1, 'b': {'c': 2, 'd': [3, 4]}}
        >>> flat(data)
        {'a': 1, 'b.c': 2, 'b.d.0': 3, 'b.d.1': 4}

        >>> data = [{'a': 1}, {'b': 2}]
        >>> flat(data)
        {'0.a': 1, '1.b': 2}
    """
    items = []
    if isinstance(data, MutableSequence):
        for i, value in enumerate(data):
            new_key = f'{parent_key}{sep}{i}' if parent_key else str(i)
            if isinstance(value, (MutableMapping, MutableSequence)):
                items.extend(flat(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
    elif isinstance(data, MutableMapping):
        for key, value in data.items():
            new_key = f'{parent_key}{sep}{key}' if parent_key else key
            if isinstance(value, (MutableMapping, MutableSequence)):
                items.extend(flat(value, new_key, sep=sep).items())
            else:
                items.append((new_key, value))
    return dict(items)
