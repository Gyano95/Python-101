# i = 0
# lowest = 1000
# lowestYear = 1000
# lowestCountry = ""

# choiceYears = float(input("Enter your years of interest: "))

# average = 0

# with open("life-expectancy.csv") as lifeFile:
#     for line in lifeFile:
#         i = i + 1
#         cleanLine = line.strip()
#         words = cleanLine.split(",")
#         if i > 1:
#             country = words[0]
#             code = words[1]
#             year = int(words[2])
#             lifeExp = float(words[3])

#             if  lowest > lifeExp:
#                 lowest > lifeExp
#                 lowestYear = year
#                 lowestCountry = country
#             if  choiceYears == year:
#                 print(f"{year} - {country} - {lifeExp}")
#                 average = average + lifeExp
           
#     average = average / choiceYears       
# print(f"{lowest} - {lowestYear} - {lowestCountry}")


choiceYears = float(input("Enter your years of interest: "))
with open('life-expectancy.csv') as life_expectancy:
    next(life_expectancy)
    
    ## Create an empty list
    output = []
    
    for data in life_expectancy:
        clean_data = data.strip()
        split_data = clean_data.split(',')

        entity = split_data[0]
        code = split_data[1]
        year = split_data[2]
        expectancy = float(split_data[3])
      
        ## Append to the list
        output.append([entity, code, year, expectancy])

max_life = max(output, key=lambda x: x[3])
min_life = min(output, key=lambda x: x[3])

#['Monaco', 'MCO', '2019', 86.751]
#['Iceland', 'ISL', '1882', 17.76]

print(f'The overall max life expectancy is {max_life[3]} in {max_life[0]}')    
print(f'The overall min life expectancy is {min_life[3]} in {min_life[0]}')

