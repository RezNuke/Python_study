# test = ['A : B C', 'B : D', 'C : D', 'D : E', 'E']
# test_stack = ['E', 'A', 'B', 'C', 'D']


Error_d = Error_d2 = {i[0] : i[2:] for i in [input().split() for _ in range(int(input()))]} # Наследник:Родитель
for i in Error_d:
    for j in Error_d[i]: 
        if Error_d[i] != []:
            for z in Error_d[j]:
                Error_d[i] += Error_d2[j] if z not in Error_d[i] else []

# Error_d = Error_d2 = {i[0] : i[2:] for i in [test[j].split() for j in range(len(test))]} # Наследник:Родитель
# for i in Error_d:
#     for j in Error_d[i]: 
#         if Error_d[i] != []:
#             for z in Error_d[j]:
#                 Error_d[i] += Error_d2[j] if z not in Error_d[i] else []
# print(Error_d)

stack = []

for _ in range(int(input())):
    ch = input()
    stack.append(ch)
    for par in Error_d[ch]:
        if par in stack[0:stack.index(ch)]:
            print(ch)
            break


# for ch in test_stack:
#     for par in Error_d[ch]:
#         if par in test_stack[0:test_stack.index(ch)]:
#             print(ch)


# print(Error_d)
