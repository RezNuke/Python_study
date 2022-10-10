class ExtendedStack(list):
    def sum(self):
        # �������� ��������
        a = self.pop()
        b = self.pop()
        return self.append(a + b)

    def sub(self):
        # �������� ���������
        a = self.pop()
        b = self.pop()
        return self.append(a - b)
    
    def mul(self):
        # �������� ���������
        a = self.pop()
        b = self.pop()
        return self.append(a * b)
        
    def div(self):
        # �������� �������������� �������
        a = self.pop()
        b = self.pop()
        return self.append(a // b)
    
ex_stack = ExtendedStack([1, 2, 3, 43, 2])
print(ex_stack.sum())
print(ex_stack.mul())
