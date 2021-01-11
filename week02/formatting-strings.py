#Formatting Strings

first_name = 'Toba'
last_name = 'Obiwale'

first_name = input('What is your first_name: ')
last_name = input('What is your last_name: ')
print('Your name is {1} {0} {1}'.format(first_name, last_name + ','))
