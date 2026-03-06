# accuracy_scores ek list hai jo ML model ki 5 alag tests ki accuracy bata rahi hai
accuracy_scores = [0.85, 0.90, 0.78, 0.92, 0.88]

for score in accuracy_scores:
    if score < 0.80:
        # Agar condition True hai, toh yeh warning print hogi
        print(f"this is low accuracy{score}")

    else:
        print(f"this is good performance{score}")