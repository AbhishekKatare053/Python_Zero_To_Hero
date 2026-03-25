# Topic: Python Dictionaries
# Goal: Storing structured data (Network Device Example)

# 1. Dictionary Define karna (Curly Braces {})



router = {
    "hostname" : "katare-RT-01",
    "ip"     : "192.168.1.1",
    "model" : "Cisco ISR 4000",
    "status" : "active" 
}

# 2. Data Access karna (Key ka naam use karke)
n = router["hostname"]
r = router["ip"]
print(n , ", ip address = ", r)


# 3. Data Update karna
router["status"] = "maintenance"
print(router["status"])


# 4. Naya Key-Value pair add karna
router["location"] = "Gurgaon"
print(router["location"])





#Line-by-Line Breakdown:
'''
router = { ... }:

Python mein {} ka matlab Dictionary hai.

"hostname" yahan Key hai aur "KATARE-RT-01" uski Value.

router['hostname']:

List mein hum [0] likhte the, yahan hum 'key_name' likhte hain. Yeh zyada readable hai kyunki aapko pata hai aap kya mang rahe ho.

router["status"] = "Maintenance":

Agar Key pehle se maujood hai, toh Python uski value badal deta hai.

router["location"] = "Gurugram DC":

Agar Key pehle se nahi hai, toh Python use naya add kar deta hai.

'''