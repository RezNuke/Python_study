a = 'D:\Programming\Stepik_course\Readable files\dataset_3363_4.txt'
b = 'D:\Programming\Stepik_course\Readable files\Aver_dataset_3363_4.txt'
lst_of_str_a = list()

with open(a, 'r') as f:
    for string in f:
        lst_of_str_a += [string.strip('\n').split(';')]

#for i in lst_of_str_a: 
#    print(i)        


with open(b, 'w') as f:
    aver_math = 0
    aver_ph = 0
    aver_rus = 0
    for elem in lst_of_str_a:
        aver = 0  
        aver_math += int(elem[1])
        aver_ph += int(elem[2])
        aver_rus += int(elem[3])
        for j in range(1,len(elem)):
            aver += int(elem[j])
        aver /= len(elem)
        aver = str(aver)
        f.write(elem[0] + '; ' + aver + '\n')
    aver_math /= len(lst_of_str_a)
    aver_ph /= len(lst_of_str_a)
    aver_rus /= len(lst_of_str_a)
    f.write(str(aver_math) + ' ' +  str(aver_ph) + ' ' + str(aver_rus))