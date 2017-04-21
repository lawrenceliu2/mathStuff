def union (a,b):
    test = [x for x in a]
    test += [y for y in b if y not in test]
    return test

print union({1,2,3}, {2,3,4})

def intersection (a,b):
    test = [x for x in a if x in b]
    return test

print intersection({1,2,3}, {2,3,4})

def setDiff (a,b):
    test = [x for x in a if x not in b]
    return test

print setDiff({1,2,3}, {2,3,4})

def symDiff (a,b):
    test = setDiff(a,b) + setDiff(b,a)
    return test

print symDiff ({1,2,3}, {2,3,4})

def cartProd (a,b):
    test = [[x,y] for x in a for y in b]
    return test

print cartProd({1,2}, {'red','white'})
