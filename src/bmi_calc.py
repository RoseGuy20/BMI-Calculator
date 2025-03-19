import math 

def convertHeight(feet, inches):
    return inches + (feet * 12)

def calcBMI(total_feet, weight):
    weight *= 0.45 
    converted_feet = total_feet * 0.025
    converted_feet *= converted_feet
    bmi = weight / converted_feet
    return bmi 

def detBMICategory(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
def cli():  
    print("Welcome to the Command Line BMI Calculator")
    
    try:
        feet, inches = [int(x) for x in input("Please enter your height (feet, inches): ").split(', ')] 
        
        weight = float(input("Please enter your weight in pounds: "))
        
        if weight <= 0 or feet < 0 or inches < 0:
            print("Error: Height and weight must be positive values.")
            return
        
        total_feet = convertHeight(feet, inches)
        bmi = calcBMI(total_feet, weight)
        category = detBMICategory(bmi)
        
        print(f"BMI is {bmi:.2f}: {category}")
    except ValueError:
        print("Error: Please enter valid numbers for height and weight.")
    except Exception as e:
        print(f"An error occurred: {e}")


cli()
