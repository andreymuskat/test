lines = ["Hello world!"]
with open(r"C:\Users\User\Desktop\Hello world.txt", "w") as file:
    for  line in lines:
        file.write(line)
print(line)