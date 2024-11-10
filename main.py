filename = input("Enter the path to the world (without '' !): ")

with open(filename, "rb") as r:
    file = r.read()

data = bytearray(file)

offset = 0x1AA

try:
    data[offset] = 0x11
    flag = True
except Exception as e:
    print(f"Error modifying data: {e}")
    flag = False

if flag == True:
    print("Your world sucсessfuly patched! ")
    with open(filename, "wb") as w:
        w.write(data)
if flag == False:
    print("Your world has not been successfully patched")