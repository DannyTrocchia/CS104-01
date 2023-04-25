# "Tommy" , "Jimmy" , "Henry" , "Anthony Stabile" , "Freddy No Nose" , "Pete the Killer", "Mikey Franceze", "Johnny Two Times" , "Paulie Vario" , "Frankie the Wop"
names = []
for x in range (10):
    names.append (input("Enter Name: "))
print (names)

for x in range (10):
    print (names.pop(0))
if len(names)==0:
    print(names)
