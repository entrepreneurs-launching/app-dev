#!/usr/local/bin/python3

filename = 'lastline.txt'

f1 = open(filename, 'r')
line = int(f1.readline())
f1.close()

print (line)
line += 1

f2 = open(filename, 'w')
print (f2.writelines([str(line)]))
f2.close()

