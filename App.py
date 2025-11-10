def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    try:
        w = float(input("Weight in kg: "))
        h = float(input("Height in meters: "))

        if w <= 0 or h <= 0:
            raise ValueError("height/weight must be positive >0")

        val = bmi(w, h)
        print(f"BMI = {val:.2f}")
        print("Category:", category(val))

    except Exception as e:
        print("Error:", e)
