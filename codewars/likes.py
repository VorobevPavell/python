def likes(names):
    if len(names) == 4:
        return(", ".join(names[:2]) + ' and 2 others like this ')
    if len(names) == 3:
        return(", ".join(names[:2])+ ' and ' +names[-1]+ ' like this')
    if len(names) == 2:
        return(" ".join(names[0])+ ' and ' +names[1]+ ' like this')
    if len(names) == 1:
        return(" ".join(names[0])+' like this')
    if len(names) == 0:
        return "no one likes this"
