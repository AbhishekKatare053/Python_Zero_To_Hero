# Topic : Operators (Math ke Hathiyar)

'''1. Kyun? (Why?)

Jab aap Machine Learning mein kisi ghar ki keemat (Price) predict karenge, toh dimaag mein math chal raha hota hai. Python mein wo math "Operators"
 ke zariya hota hai.

Salary Calculation: Bonus add karna (+).

Loss Calculation: Purani value aur nayi value ka difference (-).

Probability: Percentage nikalna.

2. Concept:

Python mein kuch special operators hain jo normal math se thode alag dikhte hain:

** : Exponentiation (Power nikalne ke liye, jaise $2^3 = 8$)

// : Floor Division (Divide karke sirf poora number dena, point ke baad ka hata dena)

% : Modulo (Divide karne ke baad jo "shesh-phal" ya remainder bachta hai)'''


# -------------------------------------------------------------------------
# TOPIC: ARITHMETIC OPERATORS
# PHASE: 01 (Python Foundations)
# DESCRIPTION: Python mein mathematical logic perform karna.
# -------------------------------------------------------------------------

# Do numbers le rahe hain
num1 = 10
num2 = 3

# 1. Basic Math
print(f"Addition: {num1 + num2}")        # 13
print(f"Subtraction: {num1 - num2}")     # 7
print(f"Multiplication: {num1 * num2}")  # 30
print(f"Division: {num1 / num2}")        # 3.333...

# 2. Advanced Math (ML mein bahut use hote hain)
print(f"Power (10^3): {num1 ** num2}")   # 10 * 10 * 10 = 1000
print(f"Floor Division: {num1 // num2}") # 3 (Sirf integer part dega)
print(f"Remainder (Modulo): {num1 % num2}") # 1 (10 ko 3 se divide karne par 1 bachta hai)

# 3. Assignment Operator (Salary Hike ka example)
salary = 150000
salary += 50000   # Iska matlab hai: salary = salary + 50000
print(f"New Salary after hike: {salary}")

# Kyun kar rahe hain?
# ML algorithms (jaise Optimization) piche se yahi logic use karte hain 
# data points ke beech ka distance nikalne ke liye.