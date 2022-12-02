
# pls help me 
inputs = """"""

score: int = 0

with open('RockPaperScissors.txt', 'r') as file:
    inputs = file.read()
#inputs = """A Y
#B X
#C Z"""

#A,X -> 1
#B,Y -> 2
#C,Z -> 3

#AX -> 3 + 1 = 4, Second part 3
#AY -> 7 + 2 = 8, Second part 4
#AZ -> 0 + 3 = 3, Second part 8

#BX -> 0 + 1 = 1, Second part 1
#BY -> 3 + 2 = 5, Second part 5
#BZ -> 6 + 3 = 9, Second part 9

#CX -> 6 + 1 = 7, Second part 2
#CY -> 0 + 2 = 2, Second part 6
#CZ -> 3 + 3 = 6, Second part 7




c = {
        "AX":4, "AY":8 ,"AZ":3, "BX":1,"BY":5,"BZ":9,"CX":7,"CY":2,"CZ":6
     }

c2 = {
        "AX":3, "AY":4 ,"AZ":8, "BX":1,"BY":5,"BZ":9,"CX":2,"CY":6,"CZ":7
     }
rounds = inputs.split('\n')

rounds = [a for a in rounds if a != '']


for _,val in enumerate(rounds):
    lr = val.replace(" ", "")
    print(f"{lr} -> {c[lr]}")
    score += c2[lr]
    


print(score)
