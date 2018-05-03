def spin_words(sentence):
    str=[]
    for i in sentence.split():
        if len(i)>=5:
            str.append(i[::-1])
        else:
            str.append(i)
    return " ".join(str)

print(spin_words("Hey fellow warriors"))