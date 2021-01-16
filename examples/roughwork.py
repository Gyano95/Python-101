# Create user input

first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
email_address = input('what is you email address: ')
phone_number = input('What is your phone number: ')
job_title = input('What is your job title: ')
ID_number = input('What is your ID number: ')

hair_color = input('hair color: ')
eyes_color = input('eyes color: ')
month = input('Month start: ')
training = input('completed training? ')

# Request output from the user
print('{1}, {0} '.format(first_name, last_name.upper()))
print(email_address)
print(phone_number)
print(job_title.title())
print(ID_number)
print(f'Hair: {hair_color:15} Eyes: {eyes_color}')
print(f"Month: {month: 14} Training: {training} ")

#------------Data Type and Numbers----------#

birthday = int(input('When is your next birthday: '))
next_age = birthday + 1
print(f'Your age would be {next_age}')


age = int(input('What is your age '))
print(f"On your next birthday, you will be, {age + 1}!.")
print('\n')

carton = int(input('How many egg cartons do you have? '))
print(f'You have {carton * 12} of eggs.')
print('\n')

cookies = input('How many cookies do you have?: ')
people = input('How many people are there? ')
print(f"Each person may have {int(float(cookies)) / int(float(people))} cookie.")
