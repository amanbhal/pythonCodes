from sys import argv

script, in_file, to_file = argv

file_1 = open(to_file)

data_1 = file_1.read()

print "length of %s is %d bytes." % (to_file,len(data_1))

file_2 = open(in_file, 'w')

file_2.write(data_1)
file_2.close()

file_2 = open(in_file)
print file_2.read()

file_1.close()
file_2.close()