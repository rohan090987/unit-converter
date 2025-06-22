import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(description="Temperature Unit Converter")

    parser.add_argument(
        "value",
        type=float,
        help="Temperature value to convert"
    )

    parser.add_argument(
        "--to",
        choices=["c", "f"],
        required=True,
        help="Convert to 'c' for Celsius or 'f' for Fahrenheit"
    )

    args = parser.parse_args()

    if args.to == "f":
        result = celsius_to_fahrenheit(args.value)
        print(f"{args.value}°C = {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.value)
        print(f"{args.value}°F = {result:.2f}°C")

if __name__ == "__main__":
    main()
