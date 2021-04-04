i = 0
lowest = 1000
lowestYear = 1000
lowestCountry = ""

# i = 1
# highest = 2000
# highestYear = 2000
# highestCountry = ""

choiceYears = float(input("Enter your years of interest: "))

average = 0
max_year = -1

with open("life-expectancy.csv") as lifeFile:
    for line in lifeFile:
        i = i + 1
        cleanLine = line.strip()
        words = cleanLine.split(",")
        if i > 1:
            country = words[0]
            code = words[1]
            year = int(words[2])
            lifeExp = float(words[3])

            if  lowest > lifeExp:
                lowest > lifeExp
                lowestYear = year
                lowestCountry = country
            if  choiceYears == year:
                print(f"{year} - {country} - {lifeExp}")
                average = average + lifeExp
           
    average = average / choiceYears       
print(f"{lowest} - {lowestYear} - {lowestCountry}")

if max_year > year:
    year = max_year
    choiceYears = max_year

print(f"")