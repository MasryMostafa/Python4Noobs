print "Welcome to the grocery list generator."
glist = []
a = input("How many items do you have today?")
b = 0

while b < a:
    i = raw_input("Enter new grocery item >>> ")
    glist.append(i)
    b += 1

print "OK here's your list of groceries:"

for element in glist:
    print "* %s" % element
