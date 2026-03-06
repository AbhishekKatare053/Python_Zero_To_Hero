# Topic: String Formatting & Methods
# ML Importance: Cleaning text data (Removing spaces, changing case)

raw_data = "   Machine Learning is FUTURE   "

# 1. Cleaning Spaces (Very important for data entry)
clean_data = raw_data.strip()
print(f"Cleaned: '{clean_data}'")

# 2. Case Normalization (Sab kuch ek jaisa karne ke liye)
print(f"Lowercase: {clean_data.lower()}")
print(f"Uppercase: {clean_data.upper()}")

# 3. Replacing characters (Cleaning special symbols)
messy_phone = "+91-987-654-3210"
clean_phone = messy_phone.replace("-", "")
print(f"Formatted Phone: {clean_phone}")

# 4. F-Strings (The Professional way to print results)
name = "Abhishek"
stage = "Phase 1"
print(f"Engineer: {name} | Progress: {stage}")