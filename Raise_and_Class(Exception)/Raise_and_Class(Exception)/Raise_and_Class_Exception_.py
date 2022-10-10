class NonPositiveError(Exception):
    def __init__(self, Num):
        print(str(Num) + ' is not positive number')
    

class PositiveList(list):
    def append(self, Num):
        if Num > 0:
            super(PositiveList, self).append(Num)
        else:
            raise NonPositiveError(Num)

lst = PositiveList()
try:
    lst.append(int(input()))
except NonPositiveError:
    print('Please Enter positive number!!!')
print(lst)