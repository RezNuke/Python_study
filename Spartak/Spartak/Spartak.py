stat = dict() 

for i in range(int(input())):
    s = input().split(';')
    for j in s:
        print(type(j))
        if type(j) == 'str':  #Поиск команды       
            if j not in stat:
                stat[j] = list()
            
print(s[:])    
for key in stat.keys():
    print(key, end = " ")    