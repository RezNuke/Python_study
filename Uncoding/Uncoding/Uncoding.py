
# ��������� ���������� ���� 'a' 

a = 'D:\Programming\Stepik_course\Readable files\dataset_3363_2.txt'
b = 'D:\Programming\Stepik_course\Readable files\code_dataset_3363_2.txt'
Num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
Count = '0'
Ch = '0'
str_goal = ''  # ��� ����� ����������


# ������ �����
with open(a) as my_file:
    s = my_file.readline()
# print(s)

for i in s:
    if i in Num:
        Count += i 
    else:
        if Count != '0':
            str_goal += Ch * int(Count)
        Ch = i
        Count = '0'
        
print(str_goal)

# ������ � ����
with open(b, 'w') as my_file:
    my_file.write(str_goal)

    