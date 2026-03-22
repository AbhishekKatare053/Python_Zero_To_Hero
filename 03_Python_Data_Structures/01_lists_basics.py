# Topic: Python Lists
# Goal: Store and manipulate multiple data points

devices = ["router a" , "router b", "router c" ," firewall"]

print(devices[0])
print(devices[-1])


devices.append("router D")
print(f"Total devices in network: {len(devices)}")