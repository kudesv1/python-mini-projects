weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Введите ваш рост в см: "))

height_m = height_cm / 100
bmi = weight / (height_m**2)

print(f"Ваш ИМТ: {bmi:.1f}")

try:
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
except ValueError:
    ("Please enter a valid number.")
print(f"Category: {category}")