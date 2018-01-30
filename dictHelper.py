def increment(dict, key, value):
    if key in dict:
        dict[key] = dict[key] + value
    else:
        dict[key] = value
        
        