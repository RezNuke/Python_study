# Формирование словаря и подсчет слов
def word_init(lst, d):
    for i in lst:         
        # print(i.strip('\n'))        
        str_WaW = i.lower().split()
        #  print(str_WaW)
        for j in str_WaW:
            word_counter(d, j) 

# Счетчик слов
def word_counter(d, key):
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1            

a = 'D:\Programming\Stepik_course\Readable files\dataset_3363_3.txt'
lst_of_str_a = list()

# Чтоние файла
with open(a, 'r') as f:
    for str in f:
        lst_of_str_a += [str]

Word = dict()
word_init(lst_of_str_a, Word)

key_goal = ''
value_goal = 0


# Вывод словаря
#for key, value in Word.items():
#    print(key, value)

# Поиск самого распространненого слова    
for key, value in Word.items():
    if value > value_goal:
        key_goal = key
        value_goal = value
    elif value == value_goal and key < key_goal:
        key_goal = key
        value_goal = value
print(key_goal, value_goal)
