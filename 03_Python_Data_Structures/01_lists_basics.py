# Topic: Python Lists
# Goal: Store and manipulate multiple data points

# 1. List banana (e.g., Network Devices)
devices = ["Router_A", "Switch_B", "Firewall_C", "Load_Balancer"]

# 2. List Access karna (Index 0 se start hota hai)
print(f"First device: {devices[0]}")
print(f"Last device: {devices[-1]}")

# 3. List mein naya item add karna
devices.append("Router_D")

# 4. List ki length check karna
print(f"Total devices in network: {len(devices)}")


'''
devices = ["Router_A", "Switch_B", "Firewall_C", "Load_Balancer"]

Logic: Yahan hum ek List bana rahe hain. Python mein [] (square brackets) ka matlab hota hai ek collection.

Analogy: Ek rack ki tarah samjho jisme 4 alag-alag devices rakhe hain. Har device ki ek fix jagah hai.

print(f"First device: {devices[0]}")

Logic: Programming mein counting 0 se shuru hoti hai. Isliye devices[0] ka matlab hai pehla item ("Router_A").

Pro-Tip: Agar aap devices[1] likhte, toh wo "Switch_B" dikhata.

print(f"Last device: {devices[-1]}")

Logic: Python mein ek cool feature hai—Negative Indexing. -1 ka matlab hai "piche se pehla" (Last item).

Network Use Case: Jab aapko pata na ho ki list kitni lambi hai par aapko sabse naya added device dekhna ho, toh -1 kaam aata hai.

devices.append("Router_D")

Logic: append() ek built-in function hai jo list ke aakhir (end) mein ek naya item jod deta hai.

Result: Ab aapki list mein 4 ki jagah 5 devices ho gaye hain.

print(f"Total devices in network: {len(devices)}")

Logic: len() ka matlab hai Length. Yeh function ginta (counts) hai ki list ke andar total kitne items hain.

Output: Yeh 5 print karega kyunki humne abhi ek "Router_D" add kiya hai.
'''