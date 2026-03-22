# Topic: Functions
# Goal: Create reusable blocks of code

def check_model_health(accuracy , loss):
    if accuracy > 0.80 and loss < 0.20 :
        return "Model is healthy"
    
    else:
        return "model is unhealthy"

result1 = check_model_health(0.70 , 0.35)
result2 = check_model_health(0.85 , 0.15)

print(result1)
print(result2)
'''

Line-by-Line Breakdown:

def check_model_health(accuracy, loss):

def: Iska matlab hai "Define". Aap Python ko bata rahe ho ki main ek naya function bana raha hoon.

check_model_health: Yeh aapki machine ka naam hai.

(accuracy, loss): Inhe Arguments kehte hain. Yeh wo "Raw Material" hai jo function ko chahiye kaam karne ke liye.

return "...":

Yeh function ka Output hai. print sirf screen par dikhata hai, par return us result ko save karne ke liye bahar bhejta hai.

result1 = check_model_health(0.85, 0.15):

Yahan humne function ko "Call" kiya aur values di. Ab result1 mein wo string save ho jayegi jo function ne return ki.
'''