def name_map(names:list):
    names_length = {}
    for name in names:
        names_length[name] = len(name)
    return names_length
print(name_map(['Amin', 'Sara', 'Luna', 'jef']))