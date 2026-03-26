#Topic: Tuples 

'''
Ye Topic Kya Hai?

Tuple ek aisa collection hai jo Ordered (ek sequence mein) hota hai lekin Immutable hota hai. Immutable ka 
matlab hai—ek baar ban gaya, toh ise badla nahi ja sakta. Na delete, na add, na change.

Agar ye na karein toh kya hoga?

Machine Learning mein humein kayi baar "Constant Data" (jo kabhi na badle) ki zaroorat hoti hai. Agar 
aapne model ke parameters (jaise image ka size 224x224) List mein rakhe, toh code mein kahin bhi galti 
se wo change ho sakte hain. Isse aapka poora AI model crash ho jayega ya galat result dega. Tuple wahan 
"Security Guard" ka kaam karta hai.
'''

# 1. Tuple Define karna (Round Brackets '()' use hote hain)
# Maan lo ye ek ML model ki settings hain

model_config = ("resnet50" , 0.01 , 32 )
#          (Model Name, Learning Rate, Batch Size)


# 2. Accessing Data (Bilkul List ki tarah indexing)
print(  "Model name ",model_config[0])
print("model learning rate " , model_config[1])

# 3. Immutability Check (Yahan logic samajhna hai)

try:
    model_config[1] = 0.05


except TypeError as e:
    print(f"\n[ERROR]: {e}")
    print("Logic: Tuple ko banne ke baad badla nahi ja sakta!")


    # 4. Tuple Unpacking (Python Developer special trick)
name, lr, batch = model_config
print(f"\nUnpacked Data: Name={name}, LR={lr}, Batch={batch}")


# 5. Length check
print(f"Total parameters in, {type(model_config)} , {len(model_config)}")