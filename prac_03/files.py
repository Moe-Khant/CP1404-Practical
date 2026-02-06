"""DO from scratch"""

# Ex. 1
out_file = open("name.txt",'w')
name = input("Enter name: ")
print(name,file=out_file)
out_file.close()