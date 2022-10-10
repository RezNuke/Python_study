# n = int(input())
# del parent
parent = {'global': 'None', 'a': 'global', 'b': 'a'}  # Ключ - NameSpace, значение - Родитель
var = {'b': ['level']}  # Ключ - NameSpace, значение - [переменные]

# Функция возвращает True, если namespace существует внутри родителя par (Словарь parent)
# возвращает False, если namespace не существует внутри родителя par (Словарь parent)
# Вход - пространство имен и его родитель
# Выход - существует или нет
def check_NS(namespace): 
    status = False
    for key in parent.keys():   
        if namespace == key:
            status = True
            break
        else:
            status = False
    return status

# Функция возвращает True, если arg существует внутри родителя namespace (Словарь var)
# возвращает False, если arg не существует внутри родителя namespace (Словарь var)
# Вход - пространство имен и переменная
# Выход - существует или нет
def check_var(namespace, arg): 
    status = False
    for key, value in var.items():
        if key != namespace:
            continue
        for el in value:
            if arg == el:
                status = True
                break
            else:
                status = False
    return status
    
# Функция возвращает родителя 
def find_parent(namespace):
    for key, value in parent.items():   
        if namespace == key:
            return value
    return 'None'    
    
# Функция создает пространство имен NameSpace внутри пространства par (Словарь parent)
def create(namespace, par):
    if not check_NS(namespace):
        parent[namespace] = par
        var[namespace] = list()
    else:
        print('Namespace is existed')

# Функция создает внутри пространства имен namespace (Словарь var) переменную var
def add(namespace, arg):
    if not check_var(namespace, arg) and check_NS(namespace):
        var[namespace].append(arg)
    else:
        if not check_NS(namespace): 
            print('Namespace is not existed')
        else:
            print('Var is existed')

# Функция возвращает пространство имен, в котором находится переменная arg
def get(namespace, arg):
    if check_var(namespace, arg):
        return print(namespace)
    elif namespace == "None":
        print('None')
        return 
    else:
        return get(find_parent(namespace), arg)
            
#_______________________________
#
#       ОСНОВНАЯ ПРОГРАММА
#_______________________________

n = int(input())
del parent
parent = {'global': 'None'}  # Ключ - NameSpace, значение - Родитель
var = {'global': []}  # Ключ - NameSpace, значение - [переменные]

for i in range(n):
    com, NS, v = input().split()
    if com == 'create':
        create(NS, v)
    elif com == 'add':
        add(NS, v)
    elif com == 'get':
        get(NS, v)
    else:
        print("Command is not correct")

# for key, value in parent.items():
#     print(key + ':', value)
    




# for i in range(n):
#     com, NS, var = input().split()
    