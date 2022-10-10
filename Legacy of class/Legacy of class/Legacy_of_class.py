test = ['G : F', 'A', 'B : A', 'C : A', 'D : B C', 'E : D', 'F : D']

d = d1 = {i[0] : i[2:] for i in [test[j].split() for j in range(len(test))]}
print(d)
print(d1)
for i in d1:
    for j in d1[i]: 
        if d1[i] != []:
            for z in d1[j]:
                d1[i] += d[j] if z not in d1[i] else []
[print('Yes' if b == c or b in d1[c] else 'No') for b, c in [input().split() for _ in range(int(input()))]]