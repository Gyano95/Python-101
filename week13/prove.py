def main():    
    def wind_chill(temp, wind_speed):
        return 35.74 + (0.6215 * temp) - 35.75 * (wind_speed ** 0.16) \
            + 0.4275 * temp * (wind_speed ** 0.16)

    heading = '  '
    for temp in range(-20, 70, 10):
        heading += "{:>7d}".format(temp)
    print(heading + "\n   " + "-" * 62)   
    for wind_speed in range (0, 35, 5):
        output_line = "{:>2d}".format(wind_speed)
        for temp in range(-20, 70, 10):
            output_line += "{:>7.1f}".format(wind_chill(temp, wind_speed))
        print(output_line)

main()





