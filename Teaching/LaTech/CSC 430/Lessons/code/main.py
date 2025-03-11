file = open('data.txt', 'r')
contents = file.read()
file.close()
data = contents.split(':')
name = data[0]
age = data[1]
favNum = data[2]
print(name)
print(age)
print(favNum)