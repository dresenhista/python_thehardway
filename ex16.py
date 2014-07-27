from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
#ctrl c is the command to stop any command in the command line to run
print "If you don't want that, hit CTRL-C (^C)."
#you don't actually have to type return, you can type anything and the script keeps running
print "If you do want that, hit RETURN."

raw_input("?")

#it opens the file and attach to the variable target
print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()