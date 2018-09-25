def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

def kelvinsToFahrenheit(tempKelvins):
    tempCelsius = kelvinsToCelsius(tempKelvins)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr