class multifilter:
    def judge_any(pos, neg):
        return pos >= 1
    
    def judge_half(pos, neg):
        return pos >= neg
    
    def judge_all(pos, neg):
        return neg == 0
        
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iter_order = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for el in self.iter_order:
            pos = neg = 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el

                
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0
        
a = [x for x in range(10)]

lst = list(multifilter(a, mul2, mul3, mul5))
print(lst) 

