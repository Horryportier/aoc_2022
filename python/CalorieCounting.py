Input = """"""

with open('CalorieCounting.txt', 'r') as file:
    Input = file.read()


v= Input.split("\n\n")

a = [i.split("\n") for i in v if i != '']


i = [[int(j) for j in i if j ] for i in a]

b = [max(i[k]) for k in range(len(i)) if i[k] != []]

c = max(b)

#print(v)
#print(a)
#print(i)
print(b)
print(c)




