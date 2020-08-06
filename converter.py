#Converts_Temp_From_Celsius_To_Fahrenheit

print('Welcome to our temp. converter\n')
c = input('Enter the temp. in Celsius: ')
c = float(c)

def temp_converter(c):
    #calculation
    f = ((c*9)/5)+32
    return "{}°C is {}F in Fahrenheit.".format(c,f)

print(temp_converter(c))
