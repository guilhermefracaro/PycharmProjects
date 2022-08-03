celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * (9/5) + 32)
kelvin = celsius + 273.15
print('A temperatura de {:.1f}°C coresponde a {:.1f}°F e {:.1f}K'.format(celsius, fahrenheit, kelvin))
