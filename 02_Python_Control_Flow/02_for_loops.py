# accuracy_scores ek list hai jo ML model ki 5 alag tests ki accuracy bata rahi hai
accuracy_scores = [0.85, 0.90, 0.78, 0.92, 0.88]

for score in accuracy_scores:
    if score < 0.80:
        # Agar condition True hai, toh yeh warning print hogi
        print(f"this is low accuracy{score}")

    else:
        print(f"this is good performance{score}")
'''
1. accuracy_scores kya hai?
Yeh aapka Data Storage hai.
accuracy_scores = [0.85, 0.90, 0.78, 0.92, 0.88]
Yeh ek dibba (List) hai jiske andar 5 values padi hain.

2. for score in accuracy_scores:
Yahan score ek temporary container (variable) hai.

accuracy_scores wo poori list hai (5 values).

score wo naam hai jo aapne diya hai ki "jab loop ek-ek karke value uthaye, toh use is naam ke variable mein save kar dena."

Aap ise aise samjho:
Maan lo aap ek line mein khade 5 logo ko check kar rahe ho.

accuracy_scores = Poori line (line mein khade log).

score = Wo insaan jo abhi aapke saamne khada hai (ek baar mein ek).

Jab loop pehli baar chala, to score = 0.85.
Jab loop dusri baar chala, to score = 0.90.
...aur isi tarah aage.

3. if score < 0.80:
Yahan hum score hi kyun likh rahe hain?
Kyunki abhi loop ne jo value uthayi hai, wo score naam ke variable mein hi to rakhi hai! Agar aapne yahan score ki jagah kuch aur likha hota (jaise x), to aapko if x < 0.80 likhna padta.

Kyun accuracy_scores hi likha?
Kyunki aapne wahi naam (variable) upar define kiya hai.

Agar aapne upar likha hota mera_data = [...], to aapko niche for score in mera_data: likhna padta.


4. print(f"Alert: ..."):

Output: f ka matlab hota hai 'formatted string'. Yeh variable {score} ki value ko text mein inject kar deta hai.

'''