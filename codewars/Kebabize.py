import re
def kebabize(string):
    string = re.sub("[0-9]","",string)
    print(string)
    if string[0].isalpha():
        str=string[0]
    else:
        str=""
    for i in string[1::]:
        if i.isalpha():
            if i.isupper():
                str+="-"+i.lower()
            else:
                str+=i
    return str.lower()
print(kebabize("Hello World"))