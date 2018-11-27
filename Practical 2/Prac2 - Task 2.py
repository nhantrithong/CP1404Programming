in_file = open("name.txt","r")
name = in_file.read().strip()
print("Print your name is",name)
in_file.close()