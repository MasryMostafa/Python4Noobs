print "Let's practicee everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t\tThe lovely world
\twith logic so firmly planted
\tcannot discern\n\tthe needs of love
\tnor comprehend passion from intuition
\tand requires an explanation
\n\t\t\t\twhere there is none.
"""

print "\t\t\t~~~~~~~~~~~~~"
print "\t\t-----------------------------"
print poem
print "\t\t-----------------------------"
print "\t\t\t~~~~~~~~~~~~~"


five = 10 - 2 + 3 - 6
print "This should be five: %s" %five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" %start_point
print "We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula (start_point)
