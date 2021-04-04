# i = 0
# lowest = 1000
# lowestYear = 1000
# lowestCountry = ""

# # i = 1
# # highest = 2000
# # highestYear = 2000
# # highestCountry = ""

# choiceYears = float(input("Enter your years of interest: "))

# average = 0
# max_year = -1

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

# if max_year > year:
#     year = max_year
#     choiceYears = max_year

# print(f"")



with open("life-expectancy.csv") as data_set:
    # data_set = csv.reader(data_set)
    for line in data_set:

    # for entity, code, year, life_expectancy in data_set:
    #     year = int(year)
    #     life_expectancy = float(life_expectancy)
        clean_line = line.strip()
        line_list = clean_line.split(",")

        entity = str(line_list[0])
        code = str(line_list[1])
        year = float(line_list[2])
        life_expectancy = float(line_list[3])

        year_lookup = input("Enter the year of interest: ")

        min_life = min(line_list[3])
        max_life = max(line_list[3])
        avg_life = avg_life(line_list[3])

        max_life = 0
        if (line_list[3]) > float(max(max_life)):
            max_year = str(line_list[0])
            max_country = int(line_list[2])
        print(f"The overall max life expectancy is:{max_life} from {max_country} in {max_year}.")

        min_data = 0
        if (line_list[3]) > float(min(min_life)):
            min_year = str(line_list[0])
            min_country = str(line_list[2])
        print(f"The overall max life expectancy is:{min_life} from {min_country} in {min_year}.")
