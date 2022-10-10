objects = [1, 2, 3, 3, 3, 1, False, True]
ans = 0
index = 0
objects.sort()

while index < len(objects):
    for j in range(index + 1, len(objects)):
        if objects[index] is not objects[j]:
            ans += 1
            index = j
            break
            
print(ans)            