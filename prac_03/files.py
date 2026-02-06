"""DO from scratch"""
from fileinput import close

# Ex. 1
out_file = open("name.txt",'w')
name = input("Enter name: ")
print(name,file=out_file)
out_file.close()

in_file = open("name.txt",'r')
line = in_file.read().strip()
print(f"Hi {line}!")
in_file.close()