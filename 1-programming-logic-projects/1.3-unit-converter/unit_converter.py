# To detect the Operational System
import platform

# To clear the terminal
import os

# Length measurements
LENGTH_VALUES = {
    # Meter
    1: 1,
    # Mile
    2: 0.00062137,
    # Yard
    3: 1.0936132983,
}

# Weight measurements
WEIGHT_VALUES = {
    # Kilogram
    1: 1,
    # Pound
    2: 2.20462262185,
}

# Temperature measurements
TEMPERATURE_VALUES = {
    # Celsius
    1: 1,
    # Kelvin
    2: 1,
    # Fahrenheit
    3: 1.8,
}

# Clear the terminal
def clear_terminal():
    """Clear the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")


# Get measurements options
def get_unit_options(measurement: int):
    """Get measurement options

    Args:
        measurement (int): Selected measurement
            1 - length
            2 - weight
            3 - temperature

    Raises:
        ValueError: Invalid measurement

    Returns:
        str, int: Available measurements and counts

    """
    if measurement == 1:
        return (
            "\nAvailable length measurements: \n\n1 - Meter\n2 - Mile\n3 - Yard",
            len(LENGTH_VALUES),
        )
    elif measurement == 2:
        return "\nAvailable weight measurements: \n\n1 - Kilogram\n2 - Pound", len(
            WEIGHT_VALUES
        )
    elif measurement == 3:
        return (
            "\nAvailable temperature measurements: \n\n1 - Celsius\n2 - Kelvin\n3 - Fahrenheit",
            len(TEMPERATURE_VALUES),
        )
    else:
        raise ValueError("Invalid measurement")


# Get the inputs
def receive_values():
    """Receive input values

    Returns:
        dict: related input data
    """
    while True:
        try:
            # Get the measurement
            measurement = int(
                input(
                    "Measurements: \n\n1 - length\n2 - weight\n3 - temperature\n\nSelected measurement: "
                )
            )

            # Validate the measurement
            if measurement not in [1, 2, 3]:
                raise ValueError("Invalid measurement")

            # Get the measurements options text
            options, options_counts = get_unit_options(measurement=measurement)

            # Get the FROM measurements
            received_type = int(input(f"{options}\n\nSelect the FROM measurement: "))
            # Validate the FROM measurement
            if received_type not in [i for i in range(1, options_counts + 1)]:
                raise ValueError("Invalid FROM measurement")

            # Get the TO measurements
            target_type = int(input(f"{options}\n\nSelect the TO measurement: "))
            # Validate the TO measurement
            if target_type not in [i for i in range(1, options_counts + 1)]:
                raise ValueError("Invalid TO measurement")

            # Input the value to convert
            received_value = float(input("\nInsert the value: "))

            return {
                "measurement": measurement,
                "received_value": received_value,
                "received_type": received_type,
                "target_type": target_type,
            }
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print("An unexpected error occurred")
            print(e)


# Unit convert definition
def unit_convert(number: float, measurement: int, received_type: int, target_type: int):
    """Unit convert

    Args:
        number (float): Received value
        measurement (int): Selected measurement
            1 - length
            2 - weight
            3 - temperature
        received_type (int): Received measurement
        target_type (int): Target measurement

    Raises:
        Exception: Invalid operation

    Returns:
        float: Result of the operation
    """

    # Length
    if measurement == 1:
        return number / LENGTH_VALUES[received_type] * LENGTH_VALUES[target_type]

    # Weight
    if measurement == 2:
        return number / WEIGHT_VALUES[received_type] * WEIGHT_VALUES[target_type]

    # Temperature
    if measurement == 3:
        temperature_static = 0

        # Kelvin
        if received_type == 2:
            temperature_static = 273.15
        # Fahren
        if received_type == 3:
            temperature_static = 32

        return (
            (number - temperature_static)
            / TEMPERATURE_VALUES[received_type]
            * TEMPERATURE_VALUES[target_type]
        )

    # Raise invalid operation exception
    else:
        raise ValueError("Invalid operation")


def main():
    """Main program"""
    while True:
        # Clear the terminal
        clear_terminal()

        # Get related inputs
        values = receive_values()

        # Get the converted value
        result = unit_convert(
            number=values["received_value"],
            measurement=values["measurement"],
            received_type=values["received_type"],
            target_type=values["target_type"],
        )

        # Show the results
        print(f"Result: {result:.6f}")

        # Re-run looping
        if input("\nDo you want to run again? (y/n): ").lower() not in ["y", "yes"]:
            break


if __name__ == "__main__":
    # Run the program
    main()
