# Sortlist
# takes a text document file name in the command line
# takes the words from each line, sorts them alphabetically
# writes the resulting list out to the same file if no second arument
# or the file specified by the 2nd argument
# @author michaelsvanbeek@gmail.com

import sys
import string

if(len(sys.argv) > 1):
   fileinname = sys.argv[1]
   
   if(len(sys.argv) > 2):
      fileoutname = sys.argv[2]
   else:
      fileoutname = fileinname
   
   filein = open(fileinname,'r')
   list = []

   for line in filein:
      word = ' '.join(line.split())
      list.append(word)
   
   filein.close()

   list.sort()
   
   fileout = open(fileoutname, 'w')
   
   for item in list:
      if item:
         fileout.write(item + '\n')
      
   fileout.close()