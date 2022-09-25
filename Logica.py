A = 0
B = 0
C = 0
D = 0

array = [A, B, C, D]
equal = True

for i in range(2**(len(array))):
    b = bin(i)
    b = str(b).split('b')[1]
    b = list(b)
    b = list(map(lambda x: int(x), b))
    b = (len(array)-len(b))*[0]+b
    print(b)
    A, B, C, D = b
    eval1 = not A and ((B or (not C and D)) or C and B)
    eval2 = not A and ((A or B) or not C and D)

    equal = equal and eval1 == eval2

print("Same condition: "+str(equal))