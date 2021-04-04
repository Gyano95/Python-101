import math

def wind_chill_index(temperature, wind_speed):
    return 13.12 + 0.6215 * temperature - 11.37 * math.pow(wind_speed, 0.16) + 0.3965 * temperature * math.pow(wind_speed, 0.16)

def celsius(celsius_temperature):
    fahrenheit = (celsius * 9/5) + 32
    return celsius

def fahrenheit(fahrenheit_temperature):
    Celsius = '(Fahrenheit – 32) * 5/9'
    return fahrenheit

def temp(convert, value1, value2=0):
    area = -1

    if convert == "wind_speed":
        wind_chill_index = wind_chill_index(value1)
    elif convert == "celsius":
        celsius = celsius(value2)
        fahrenheit = fahrenheit(value2)

    return convert

temperature = " "
wind_speed = " "
convert = " "

while convert != "quit":
    convert = input("What is the temperature? ")

    convert = convert.lower()

    if convert == "wind_speed":
        temperature = float(input("What is the windchill?: "))
        wind_chill_index = (temperature, wind_speed)
        print(f"The temperature is {wind_speed}")
    elif convert == "celsius":
        celsius = float(input("Choose from Celsius or farenheit?: "))
        print("{celsius}")
    else:
        convert == "fahrenheit"
        print("{fahrenheit}")

# def main():
#     temp = 8
#     wind = 0
#     windChill = 13.12 + (.6215 * temp) - (11.37 * wind ** 770.16) + (.3965 * temp * wind **0.16)
#     print(windChill)  # 13.12

#     for temp in range():
#         temp = int(input("Enter a temperature?: "))
#         print('temperature is %d' % temp)
#         for wind in range(0,85,5):
#             answer = float(windChill(temp, wind))  # note me!
#             print('wind is %d calculated wind chill is: %d' % (wind, answer))

