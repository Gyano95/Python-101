print("Enter Toba's Obtained in 5 Subjects: ")
gradeOne = int(input('English 101: '))
gradeTwo = int(input('Math: '))
gradeThree = int(input('WDD: '))
gradeFour = int(input('Intro to Python: '))
gradeFive = int(input('Career Development: '))

score = gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive
avg = score / 5

if avg>=91 and avg<=100:
    print("Your Grade is A+, Excelent!")
elif avg>=81 and avg<91:
    print("Your Grade is A-, Great work!")
elif avg>=71 and avg<81:
    print("Your Grade is B+, Very Good!")
elif avg>=61 and avg<71:
    print("Your Grade is B-, Good Work!")
elif avg>=51 and avg<61:
    print("Your Grade is C+, you qualified!")
elif avg>=41 and avg<51:
    print("Your Grade is C-, you can still improve!")
elif avg>=33 and avg<41:
    print("Your Grade is D, Sorry, Final grade is C-!")
elif avg>=21 and avg<33:
    print("Your Grade is E1, Sorry you didn't pass!")
elif avg>=0 and avg<21:
    print("Your Grade is E2, Sorry you failed!")
else:
    print("Invalid Input!")