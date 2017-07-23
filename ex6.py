# We define x as a string with a statement
x = "There are %d types of people." % 10
# we define this variable as a string
binary = "binary"
# We define this variable as a string
do_not = "don't"
# We define this variable as a string that included two other variable that were strings
y = "Those who know %s and those who %s." %(binary, do_not)

# We print both x and y, which are strings
print x
print y

# We pring this string that calls for x, a string
print "I said: %r." % x
print "I also said: '%s'." % y

# We set this varable as a boolean
hilarious = True
# We set this variable as a string with an uncalled component
joke_evaluation = "Isn't that joke so funny?! %r"

# We print joke_evaluation and make sure to include it's component, hilarious
print joke_evaluation % hilarious

# We define two strings, and then add the two string together
w = "This is the left side of..."
e = "a string with a right side."
print w + e
