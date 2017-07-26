def looper(k,b,c):
    numbers = []
    i = b
    while i < k:
        print "At the top i is %d" % i
        numbers.append(i)
        i += c
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
        print "-----------------------------------"
    print "The numbers:"
    for num in numbers:
        print num

looper(input("List length>>>>"),input("List start>>>>"),input("List interval>>>>"))

def for_looper(k,b,c):
    numbers = []
    for i in range(b,k,c):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
        print "-----------------------------------"
    print "The numbers:"
    for num in numbers:
        print num
for_looper(input("List length>>>>"),input("List start>>>>"),input("List interval>>>>"))
