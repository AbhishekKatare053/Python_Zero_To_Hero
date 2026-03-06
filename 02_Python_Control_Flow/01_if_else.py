# Threshold wo value hai jo decide karti hai ki decision kya lena hai
threshold = 0.5 
# Prediction score wo hai jo ML model calculate karta hai
prediction_score = 0.7 

# Condition check: Kya score threshold se bada hai?
if prediction_score > threshold:
    # Agar haan, toh ye block chalega
    print("Decision: Positive Class (Accept)")
else:
    # Agar nahi, toh ye block chalega
    print("Decision: Negative Class (Reject)")




'''
threshold = 0.5: Ye ek benchmark hai. ML mein humein decision lene ke liye ek point set karna padta hai.

prediction_score = 0.7: Ye humara data point hai.

if prediction_score > threshold::

Kyun?: Hum check kar rahe hain ki kya 0.7, 0.5 se bada hai.

Na karein toh?: Agar hum ye condition nahi lagayenge, toh computer ko pata hi nahi chalega ki result "Positive" hai ya "Negative".

'''