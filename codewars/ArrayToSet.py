def words_to_object(s):
    if len(s)==0:
        return '[]'
    s=s.split(' ')
    l=[]
    for i in range(len(s))[::2]:
        d = {'name': s[i], 'id': s[i+1]}
        l.append(d)
    l = str(l).replace("'name'", 'name ')
    l = str(l).replace("'id'", 'id ')
    return l


print(words_to_object("red 1 yellow 2 black 3 white 4"))
#print(words_to_object("1 red 2 white 3 violet 4 green"))
#"[{name : 'red', id : '1'}, {name : 'yellow', id : '2'}, {name : 'black', id : '3'}, {name : 'white', id : '4'}]")