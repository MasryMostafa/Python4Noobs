print "Welcome to the grocery list generator."
glist = []
a = 1

while a < 2
    i = raw_input("Enter new grocery item >>>")
    glist.append(i)
    print "Alright I've got it. Type 1 + RETURN to continue, or 2 + RETURN to end"
    a = input(">>>")

print "OK here's your list of groceries:"

for element in glist:
    print element
