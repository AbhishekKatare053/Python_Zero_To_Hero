# Topic: List of Dictionaries
# Goal: Managing multiple network devices at once

# 1. Ek list banate hain jisme 3 routers ka data hai

inventory  = [
    {"name": "RT-01", "ip": "10.0.0.1", "status": "Up"},
    {"name": "RT-02", "ip": "10.0.0.2", "status": "Down"},
    {"name": "RT-03", "ip": "10.0.0.3", "status": "Up"}
]

# 2. Pehle router ka naam print karna
print(inventory[0]) # if we want only first inventory then we will try this 
print(inventory[0]['name']) # if we want in fist inventory "name" then we try this 

# 3. Saare devices ka status check karna (Loop + Dictionary)

for device in inventory :
    print(device["name"] , device["status"])



#Line-by-Line Breakdown:
'''
inventory = [ {..}, {..} ]:

Yeh ek List hai jiske andar Dictionaries hain.

Logic: Har {} ek router ki poori detail hai.

inventory[0]['name']:

Pehle [0] ne list ka pehla dabba (dictionary) uthaya.

Phir ['name'] ne us dabbe ke andar se "RT-01" nikaal liya.

for device in inventory::

Yeh loop ek-ek karke har dictionary ko device variable mein rakhta hai.

Phir device['status'] se hum uska status check kar lete hain.

'''