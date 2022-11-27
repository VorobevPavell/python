def get_filter(a,filter= None):
    if filter is None:
        return a
    

    res = []
    for x in a:
        if filter(x):
            res.append(x)
    return res


r = get_filter([1,2,3,-5,6],lambda x : x > 0)
print(r)