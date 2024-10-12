
def calculate_area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area


def calculate_total_due(amount, tax_rate):
    total = amount + (amount * tax_rate)
    return total


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius


def main():

    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area_of_circle(radius)
    print(f"The area of the circle is: {area:.2f}")


    amount = float(input("Enter the amount: "))
    tax_rate = float(input("Enter the tax rate as a decimal (e.g., 0.06 for 6%): "))
    total = calculate_total_due(amount, tax_rate)
    print(f"The total amount due is: {total:.2f}")


    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.2f}")

if __name__ == "__main__":
    main()
