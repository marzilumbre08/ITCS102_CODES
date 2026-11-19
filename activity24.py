#dictionary
#key, value
colors_d = {"blood":"red","fruit":"orange","lemon":"yellow","leaves":"green","sky":"blue","grapes":"purple"}

print(colors_d["leaves"])

# traversing a dictionary
for x, y in colors_d.items():
    print("key is ",x,"-- value is ",y)