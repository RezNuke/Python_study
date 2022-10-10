# n = int(input())
# del parent
parent = {'global': 'None', 'a': 'global', 'b': 'a'}  # ���� - NameSpace, �������� - ��������
var = {'b': ['level']}  # ���� - NameSpace, �������� - [����������]

# ������� ���������� True, ���� namespace ���������� ������ �������� par (������� parent)
# ���������� False, ���� namespace �� ���������� ������ �������� par (������� parent)
# ���� - ������������ ���� � ��� ��������
# ����� - ���������� ��� ���
def check_NS(namespace): 
    status = False
    for key in parent.keys():   
        if namespace == key:
            status = True
            break
        else:
            status = False
    return status

# ������� ���������� True, ���� arg ���������� ������ �������� namespace (������� var)
# ���������� False, ���� arg �� ���������� ������ �������� namespace (������� var)
# ���� - ������������ ���� � ����������
# ����� - ���������� ��� ���
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
    
# ������� ���������� �������� 
def find_parent(namespace):
    for key, value in parent.items():   
        if namespace == key:
            return value
    return 'None'    
    
# ������� ������� ������������ ���� NameSpace ������ ������������ par (������� parent)
def create(namespace, par):
    if not check_NS(namespace):
        parent[namespace] = par
        var[namespace] = list()
    else:
        print('Namespace is existed')

# ������� ������� ������ ������������ ���� namespace (������� var) ���������� var
def add(namespace, arg):
    if not check_var(namespace, arg) and check_NS(namespace):
        var[namespace].append(arg)
    else:
        if not check_NS(namespace): 
            print('Namespace is not existed')
        else:
            print('Var is existed')

# ������� ���������� ������������ ����, � ������� ��������� ���������� arg
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
#       �������� ���������
#_______________________________

n = int(input())
del parent
parent = {'global': 'None'}  # ���� - NameSpace, �������� - ��������
var = {'global': []}  # ���� - NameSpace, �������� - [����������]

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
    