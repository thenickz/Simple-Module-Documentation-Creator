from importlib import import_module

from nbformat import write

take = input(str('Python Module: '))
data = dir(take)
save = []
print('1')
for item in range(len(data)):
    word = data[item]
    help_discription = help(word)
    print('a')
    if word[:2] != '__':
        line = f'[{item}]: {help(word)}'
        print(f'2.{item}')
        save.append(line)

print('3')
t = open('doc.txt', 'w')
t.write(str(save))
t.close()
print('4 finish')
