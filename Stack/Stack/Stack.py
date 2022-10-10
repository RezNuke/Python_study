class ExtendedStack(list):
    def sum(self):
        # операция сложения
        a = self.pop()
        b = self.pop()
        return self.append(a + b)

    def sub(self):
        # операция вычитания
        a = self.pop()
        b = self.pop()
        return self.append(a - b)
    
    def mul(self):
        # операция умножения
        a = self.pop()
        b = self.pop()
        return self.append(a * b)
        
    def div(self):
        # операция целочисленного деления
        a = self.pop()
        b = self.pop()
        return self.append(a // b)
    
ex_stack = ExtendedStack([1, 2, 3, 43, 2])
print(ex_stack.sum())
print(ex_stack.mul())
