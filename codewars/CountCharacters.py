def count(string):
    dict={}
    for i in string:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

print(count("AbcdAbcd"))