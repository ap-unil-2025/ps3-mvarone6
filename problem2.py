"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    # TODO: Implement this function
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    # TODO: Implement this function
    return (fahrenheit - 32) * 5 / 9

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)

    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Is this in Celsius (C) or Fahrenheit (F)? ").strip().upper()

        if unit == "C" and temp >= -273.15:
            result = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C is {result:.2f}°F")

        elif unit == "F" and temp >= -459.67:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F is {result:.2f}°C")

        elif unit in {"C", "F"}:
            # Unité valide mais température physiquement impossible
            print("Error: Temperature below absolute zero (-273.15°C / -459.67°F).")

        else:
            # Unité invalide
            print("Invalid unit. Please enter C or F.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")



# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()