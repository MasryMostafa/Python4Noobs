from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" %len(indata)

if exists(to_file) == False:
    print "The output file does not exist, but I'll make it!"
else:
    print "We're ready to go! hit RETURN to continue!"

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
