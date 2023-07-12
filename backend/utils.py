# returns the key of a dict that has a given value
def get_keys_with_value(dictionary: dict, value):
    keys = []
    for (k, v) in dictionary.items():
        if v == value:
            keys.append(k)
    return keys