"""DO from scratch"""

# Ex.1
out_file = open("name.txt",'w')
name = input("Enter name: ")
print(name,file=out_file)
out_file.close()

# Ex.2
in_file = open("name.txt",'r')
line = in_file.read().strip()
print(f"Hi {line}!")
in_file.close()

# Ex.3
with open("numbers.txt",'r') as in_file:
    numbers = in_file.readlines()
for index in range(0,len(numbers)):
    result = int(numbers[0]) + int(numbers[1])
print(result)

# Ex.4
# numbers = []
# with open("numbers.txt",'r') as in_file:
#     for line in in_file:
#         number = int(line.strip())
#         numbers.append(number)
# print(sum(numbers))