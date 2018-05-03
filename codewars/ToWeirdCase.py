def to_weird_case(string):
    s=string.split()
    new=""
    for i in s:
        counter = 1
        for j in i:
            if counter%2:
                new+=j.upper()
            else:
                new += j
            counter+=1
        new +=" "
    return new.strip()
print(to_weird_case('should return the correct value for multiple words'))