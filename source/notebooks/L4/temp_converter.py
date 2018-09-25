def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

def kelvinsToFahrenheit(tempKelvins):
    tempCelsius = kelvinsToCelsius(tempKelvins)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr

def tempCalculator(tempK, convertTo):
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.

    Parameters
    ----------
    tempK: <numerical>
        Temperature in Kelvins
    convertTo: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' | 'F'

    Returns
    -------
    <float>
        Converted temperature.
    """

    # Check if user wants the temperature in Celsius
    if convertTo == "C":
        # Convert the value to Celsius using the dedicated function for the task that we imported from another script
        convertedTemp = kelvinsToCelsius(tempKelvins=tempK)
    elif convertTo == "F":
        # Convert the value to Fahrenheit using the dedicated function for the task that we imported from another script
        convertedTemp = kelvinsToFahrenheit(tempKelvins=tempK)
    # Return the result
    return convertedTemp    