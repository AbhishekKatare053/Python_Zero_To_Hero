# Concept: List Slicing

'''
Slicing ka matlab hai list ka ek khaas hissa kaat kar nikaalna. Iska formula hai :

list[start : stop : step]

start: Kahan se shuru karna hai (Index 0 se).

stop: Kahan khatam karna hai (Lekin yaad rahe, yeh wala index shaamil nahi hota).

step: Kitne kadam chhalang maarni hai (Default 1 hota hai).

'''
servers = ["serv1", "serv2" ,"serv3","serv4" , "serv5","serv6","serv7","serv8","serv9","serv10","serv11" ]

# 1. Pehle 3 servers nikaalna (Index 0, 1, 2)
first_batch = servers[0:4]
print(first_batch)

# 2. Beech ke servers (Index 4 se 7 tak)
Middle_batch = servers[3:7]
print(Middle_batch)

# 3. Aakhri 2 servers (Negative indexing use karke)
last_two = servers[-2:]
print(last_two)

# 4. Har dusra server (Stepping)
alternate_server = servers[::2]
# OR
# alternater_server = server[0:11:2]
print(alternate_server)


'''

Line-by-Line Breakdown:
servers[0:3]: Yeh 0, 1, aur 2 index ke items uthayega. Index 3 par jo "SRV-04" hai, use chhod dega.

servers[4:8]: Yeh "SRV-05" (index 4) se shuru karega aur "SRV-08" (index 7) tak jayenge.

servers[-2:]: Jab : ke baad kuch na ho, toh uska matlab hai "thend tak". -2 se shuru karke aakhir tak ke saare items le aayega.

servers[::2]: Pehla : poori list select karta hai, aur dusra : ke baad ka 2 batata hai ki har 2nd item uthana hai.

'''