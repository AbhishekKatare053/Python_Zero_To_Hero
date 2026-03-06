# Topic: While Loops
# Goal: Run the loop until the target condition is met

accuracy = 0.50  # Model ki starting accuracy
target = 0.90    # Humein yahan tak pahunchna hai

while accuracy < target:
   print(f"Current accuracy: {accuracy:.2f} - Still learning...")
   accuracy += 0.10

print("target is achieved model is ready")

'''
accuracy = 0.50: Humara starting point.

while accuracy < target:: Yeh Python ko bol raha hai—"Jab tak accuracy 0.90 se choti hai, tab tak ye niche wala code repeat karte raho."

print(...): Yeh humein dikhata hai ki model kitna seekh chuka hai. {accuracy:.2f} ka matlab hai "sirf 2 decimal points tak dikhao."

accuracy += 0.10: Yeh sabse zaroori line hai. Agar ye nahi likhenge, toh accuracy kabhi 0.50 se upar 
nahi badhegi aur loop infinite (kabhi khatam na hone wala) ho jayega. Ise "Increment" kehte hain.


:.2f ka Logic
Jab hum f-strings ka use karte hain, toh :  ke baad hum formatting batate hain. :.2f ka breakdown kuch aisa hai:

: : Yeh Python ko batata hai ki ab hum formatting rules batane wale hain.

.2 : Yeh batata hai ki decimal point ke baad sirf 2 digits dikhaane hain.

f : Yeh 'fixed-point' number ke liye hai (matlab decimal number).

'''