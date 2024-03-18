def recurse_find_key(key, obj):
    if obj == None:
        return None
    else:
        if key in obj:
            return obj[key]
        if isinstance(obj, (dict, list)):
            for k, v in obj.items():
                if type(v) == dict:
                    result = recurse_find_key(key, v)
                    return result
                elif type(v) == list:
                    for el in range(range(len(v))):
                        result = recurse_find_key(key, v[el - 1])
                        return result

