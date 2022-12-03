# EZ  +ratio +u fell of +ligma
Input = """"""

score = 0

treeScore = 0

with open('day3.txt', 'r') as file:
    Input = file.read()

alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

v= Input.split("\n")


v= [a for a in v if a != '']

lr = [[s[:int(len(s)/2)],s[int(len(s)/2):]] for s in v]


for i,val in enumerate(lr):
    l = val[0]
    r = str(val[1])
    for _,let in enumerate(l):
        if r.find(let) != -1:
            print(f"{i}.{let} -> {alf.find(let) +1}")
            score += (alf.find(let) +1)
            break


print(score)

# second part2
print("second part2")

tree = [v[i:i+3] for i in range(0, len(v), 3)]
for i,val in enumerate(tree):
    l = val[0]
    m = str(val[1])
    r = str(val[2])
    for _,let in enumerate(l):
        if r.find(let) != -1 and m.find(let) != -1:
            print(f"{i}.{let} -> {alf.find(let) +1}")
            treeScore += (alf.find(let) +1)
            break


print(treeScore)
