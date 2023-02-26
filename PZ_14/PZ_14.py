# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например, 86532547891), а во второй с некорректными номерами телефонов. Посчитать полученные строки в каждом файле.


import re


f = open('hotline.txt')
data = f.read()
cor_number = re.findall(r'\b\d{11}\b', data)
no_cor_number = re.findall(r'\b\d{1,10}\b|\b\d{12,}\b', data)

file1 = open('cor_num.txt', 'w')
file1.write('\n'.join(cor_number))

file2 = open('no_cor_num.txt', 'w')
file2.write('\n'.join(no_cor_number))
print(f'Кол-во строк в файле no_cor_num.txt - {len(no_cor_number)}')
print(f'Кол-во строк в файле cor_num.txt - {len(cor_number)}')