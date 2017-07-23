# This line allows you to issue this script with arguments
from sys import argv

# The script name and the filename will be arguments to this program
script, filename = argv

# This variable will open the filename
txt = open(filename)

# This will print the name of our file and it will read it.
print "Here's your file %r." %filename
print txt.read()

# This will do the same as the above but will ask for your filename
print "Type the filename again."
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
