# Come on its so ez
Input = """"""

with open('day4.txt', 'r') as file:
    Input = file.read()


v= Input.split("\n")

v = v[:-1]

containing = 0


lr = [a.split(",") for a in v]

for _,val in  enumerate(lr):
    l= val[0].split("-")
    r= val[1].split("-")
    if int(l[0]) <= int(r[0]) and int(l[1]) >= int(r[1]) or int(l[0]) >= int(r[0]) and int(l[1]) <= int(r[1]) or not int(l[1]) < int(r[0]) and not int(l[0]) > int(r[1]):
        print(l)
        print(r)
        containing = containing + 1

print(containing)
