my_dict = {'Mihail': 1998, 'Stas': 1988, 'Alex': 1992}
print(my_dict)
print(my_dict.get('Mihail'))
print(my_dict.get('Anton'))
my_dict.update({'Stefan': 1999, 'Adam': 1997})
print(my_dict.pop('Stas'))
print(my_dict)

print('-----------------------')

my_set = {1, 1, 1, 'a', 'a', 'a', (1, 2), (1, 2), (1, 2)}
print(my_set)
my_set.add(2)
my_set.add(5)
my_set.pop()
print(my_set)