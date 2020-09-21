def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi
if __name__ == "__main__":
    weight = float(input('Enter weight in Kgs = '))
    height = float(input('Enter height in meters = '))
    bmi = calculate_BMI(weight, height)
    print(bmi)
