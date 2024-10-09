
def get_float_input(prompt):



    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def calculate_bmi(weight, height):

    
    return weight / (height ** 2)


def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("=== BMI Calculator ===\n")

    # Get user input
    weight = get_float_input("Enter your weight in kilograms (kg): ")
    height = get_float_input("Enter your height in meters (m): ")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display the result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
