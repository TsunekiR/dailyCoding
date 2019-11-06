v = [1,2,3,4,5]
v2 = [0] * len(v)

for i in range(len(v)):
    resp = 1
    for j in range(len(v)):
        if j != i:
            resp = resp * v[j]
        
    v2[i] = resp

print(v2)