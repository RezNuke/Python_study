objects = [1, 2, 2, 1, True]
goal = list()
ans = 0
i = 0
Uniq = False

while i < len(objects):
    j = i + 1
    Uniq = False
    while j < len(objects):
        if objects[i] is not objects[j]:
            Uniq = True
            break   
    if Uniq:
        goal.append(objects[i])
            
    i += 1        
    

print(goal[:])