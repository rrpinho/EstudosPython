my_string1 = 'Monty python é muito bom!'
my_word1 = 'python'
if my_word1 in my_string1:
	print(True)
else:
	print(False)

print('\n############\n')

my_list1 = my_string1.split()
print(my_list1)

print('\n############\n')

my_list2 = ['Uma', 'pequena', 'frase', 'bem', 'aqui']
my_string2 = ' '.join(my_list2)
print(my_string2)