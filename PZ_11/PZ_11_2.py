import string

file = open('text18-3.txt', 'r')
content = file.read()
str_4 = '\n'.join(content.split('\n')[:4])
print(content)
print(f'Количество знаков препинания c 1 по 4 строку: {sum([1 for i in str_4 if i in string.punctuation])}')
file.close()
f = open('text18-3.txt', 'r')
data_list = f.read().split('\n')
data_list[2] = ' '.join([str(ord(i)) for i in data_list[2]])
f.close()
f = open('text18-3(2.0).txt', 'w')
f.writelines('\n'.join(data_list))
f.close()