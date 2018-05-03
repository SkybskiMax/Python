def revrot(string, sz):
    new = ""
    l=chunk(string,sz)
    for i in l:
        sum=0
        for j in i:
            sum+=int(j)**3
        if sum%2:
            new+=i[1::-1]+i[0]
        else:
            new+=i[::-1]
    return new

def chunk(str, num):
    out = []
    last = 0.0
    while last < len(str):
        out.append(str[int(last):int(last + num)])
        last += num
    if len(out[-1])!=len(out[0]):
        out.pop()
    return out

print(chunk("733049910872815764",3))
print(revrot("733049910872815764",3))

