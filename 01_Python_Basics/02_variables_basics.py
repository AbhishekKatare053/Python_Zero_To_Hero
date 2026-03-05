'''Topic 1: Variables (Data ke Dabbe)

1. Kyun? (Why are we doing this?)
Machine Learning mein humein data (jaise salary, house prices, ya patient records) ko save karna padta hai. Variable woh jagah hai jahan hum ye data save karte hain taaki baad mein us par calculation kar sakein.

2. Concept:
Variable ko ek "Container" ya "Dabbe" ki tarah samjhiye. Aap us dabbe ka ek naam rakhte hain aur uske andar koi cheez (value) dal dete hain.

3. Data Types (Dabbe ke andar kya hai?):
Python khud samajh jata hai ki aapne kya dala hai, lekin aapko ye 4 pata hone chahiye:

Integer (int): Poore numbers (e.g., 21000)

Float: Decimal numbers (e.g., 10.5)

String (str): Text (e.g., "Arthur")

Boolean (bool): True ya False (Haan ya Naa)'''


# 1. Variables assign karna (Creating containers)
User_name = 'Abhishek Katare'
Current_salary = 2100
Hike_package = 15.5
is_learning_python = True

# 2. Output dikhana (Using f-strings for better formatting)
# f-string (f"...") humein variables ko text ke beech mein asani se dalne deta hai.

print(f"{User_name}")
print(f"{Current_salary}")
print(f"{Hike_package}")
print(f"{is_learning_python}")



# 3. Data Type check karna
# Hum 'type()' function ka use karke pata kar sakte hain ki dabba kis tarah ka hai.
print("\n--- Data Types Check ---")
print(type(User_name))
print(type(Current_salary))



# Kyun kar rahe hain? 
# ML mein agar hame pata nahi hoga ki data 'Number' hai ya 'Text', 
# toh ham math perform nahi kar payenge. Type pehchanna basic zaroorat hai.

