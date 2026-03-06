# File: 05_type_casting_ml.py

# 1. Messy Data from a CSV (Initial state)
input_price = "1250.75"  # Ye string hai kyunki quotes "" mein hai
input_tax = "250"       # Ye bhi string hai

print(f"Before Conversion: {type(input_price)}, {type(input_tax)}")

# 2. Conversion (The Core of ML Preprocessing)
# Hum 'float' use karte hain kyunki price points mein ho sakta hai
clean_price = float(input_price) 
clean_tax = int(input_tax)      # Agar humein pata hai tax humesha whole number hoga

# 3. Math Operation (Ab ye possible hai)
total_cost = clean_price + clean_tax

print("-" * 30)
print(f"Total Cost: {total_cost}")
print(f"After Conversion: {type(clean_price)}, {type(clean_tax)}")
print("-" * 30)

# 4. Professional Tip: Handling Errors
# Agar data mein galti se "Abhishek" likha aa gaya toh float() crash ho jayega.
# ML engineers hamesha check karte hain:
try:
    invalid_data = float("N/A") # Ye error dega
except ValueError:
    print("Warning: Data is not a number! Setting it to 0.")
    invalid_data = 0.0
    