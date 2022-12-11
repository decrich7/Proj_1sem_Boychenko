

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknig = {'Грибоедов', 'Толстой', 'Пушкин', 'Чехов'}
bookmarket = {'Маяковский', 'Достоевский', 'Пушкин'}
galereja = {'Чехов', 'Тютчев', 'Пушкин'}

print(f'Полный список книг - {magistr | domknig | bookmarket | galereja}')
print(f'Книги которые есть во всех магазинах - {magistr & domknig & bookmarket & galereja}')
print(f'Книга котора есть не во всех магазинах - {magistr - domknig - bookmarket - galereja}')

