import re
def triple_double(num1, num2):
    pattern1=r"[0-9]{3}"
    pattern2=r"[0-9]{2}"
    if re.search(pattern1,num1) and re.search(pattern2,num2):
        return 1
    else:
        return 0

print(triple_double("1222345", "12345"))