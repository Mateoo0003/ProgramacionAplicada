W = 0
X = 0
Y = 0
Z = 0

array = [W, X, Y, Z]
equal = True

for i in range(2**(len(array))):
    b = bin(i)
    b = str(b).split('b')[1]
    b = list(b)
    b = list(map(lambda x: int(x), b))
    b = (len(array)-len(b))*[0]+b
    print(b)
    W, X, Y, Z = b
    eval1 = (X and (not Y and Z) or ((not X and not Y) and Z) or (not W and (X and Y)) or W and (not X and Y) or W and (X and Y))
    print(eval1,end='\n\n')