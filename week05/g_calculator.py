print("Enter your score in 5 Subjects: ")

gradeOne = int(input('English 101: '))
gradeTwo = int(input('Math: '))
gradeThree = int(input('WDD: '))
gradeFour = int(input('Intro to Python: '))
gradeFive = int(input('Career Development: '))

score = gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive
avg = score / 5

if avg>=90 and avg<=100:
    print("Your Grade is A, Congratulations! You passed the class!")
elif avg>=80 and avg<90:
    print("Your Grade is B+, Great work!")
elif avg>=70 and avg<80:
    print("Your Grade is B, Very Good!")
elif avg>=60 and avg<70:
    print("Your Grade is C+, Good Work!")
elif avg>=50 and avg<60:
    print("Your Grade is C, you qualified!")
elif avg>=40 and avg<50:
    print("Your Grade is C-, you can still improve!")
elif avg>=33 and avg<41:
    print("Your Grade is D, Sorry, Final grade is C-!")
elif avg>=21 and avg<33:
    print("Your Grade is E1, Sorry you didn't pass!")
elif avg>=0 and avg<21:
    print("Your Grade is E2, Sorry you failed!")
else:
    print("Invalid Input!")

    print(f'\n')

# questionOne = input('Are you male? ')
# questionTwo = input('Are you female? ')
# absent = input('Do you complete your class? ')



# print(f'')
# print('Yes, I am a (questionOne)')
# print('Yes, I am a (questionTwo)')
    


# #     if student < 0:
# #         print("Absent")
# #     else:
# #         print("You're welcome")
# # if student == male:
# #      print('You are a male')
# # else:
# #     print("You're Homo") 
# # if student == female:
# #     print('You are a female')
# # else:
# #     print('You are a gay')


           
