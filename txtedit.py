from sys import argv

script, filename = argv

print "Hi. I'm a text editor made in python."
print "I was created by Jus."
print "I will create/erase your file."
print "Hit enter to go do it. If not, please hit CTRL + C (^C)"

raw_input("> ")

print "Opening the file..."
target = open(filename, 'w')

print "Erasing all lines."
target.truncate()

print "Now, you have a max. of 15 lines."
print "Prompts will come up after this. Please type in all lines."
l1 = raw_input("l1> ")
l2 = raw_input("l2> ")
l3 = raw_input("l3> ")
l4 = raw_input("l4> ")
l5 = raw_input("l5> ")
l6 = raw_input("l6> ")
l7 = raw_input("l7> ")
l8 = raw_input("l8> ")
l9 = raw_input("l9> ")
l10 = raw_input ("l10> ")
l11 = raw_input ("l11> ")
l12 = raw_input ("l12> ")
l13 = raw_input ("l13> ")
l14 = raw_input ("l14> ")
l15 = raw_input ("l15> ")

print "Writing to file.."

fl = """ 
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
%r\n
""" % (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15)

target.write(fl)

print "Done. Now saving the file."
target.close
print "Goodbye."

