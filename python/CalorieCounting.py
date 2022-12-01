Input = """"""

with open('CalorieCounting.txt', 'r') as file:
    Input = file.read()


v= Input.split("\n")
print(v)



elfs = []
elf = []


for i in range(len(v)):
    if v[i] != "":
        elf.append(int(v[i]))
    if v[i] == "" or i == len(v)-1:
        elfs.append(elf)
        elf = []

print(elfs)

sums = [sum(i) for i in elfs]

print(sums)

maximum = 0
index = 0
for i, item in enumerate(sums):
    if item > maximum:
        index = i
        maximum = item


print(i)
print(" ")
print(maximum)

