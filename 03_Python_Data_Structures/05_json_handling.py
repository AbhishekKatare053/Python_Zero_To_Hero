import json # 1. JSON library ko import karna

# 2. Hamari Dictionary (Python Object)
network_config = {
    "device_id": "ND-9921",
    "interfaces": ["Gig0/0", "Gig0/1"],
    "is_active": True,
    "vlan": 10
}

# 3. Dictionary ko JSON String mein badalna (Dumps = Dump String)
json_data = json.dumps(network_config , indent = 4)

print("--- This is JSON Data (String) ---")
print(json_data)


# 4. Check karna ki type kya hai
print(f"Type of network_config: {type(network_config)}")
print(f"Type of json_data: {type(json_data)}")



'''
Line-by-Line Breakdown:

import json:

Yeh Python ki inbuilt library hai jo JSON data ke saath khelne mein madad karti hai.

json.dumps(network_config, indent=4):

dumps: Iska matlab hai "Dump String". Yeh Dictionary ko ek "Text String" mein badal deta hai.

indent=4: Yeh data ko sundar aur readable banata hai (spaces add karke), warna sab ek hi line mein chipak jata.

type():

Aap dekhoge ki network_config ka type dict hai, lekin json_data ka type str (string) hai.

Logic: API ko hum hamesha "String" bhejte hain, Dictionary nahi.

'''