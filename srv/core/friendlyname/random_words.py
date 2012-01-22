# Random Words
# takes n files on the command line
# selects a random line from each file
# @author michaelsvanbeek@gmail.com

import sys
import random

def random_username(list1, list2, list3):
    abs_dir = "/home/ubuntu/dev/Studygasm/srv/core/friendlyname/"
    output = ""

    for i in (list1, list2, list3):
       word_list = []
       with open(abs_dir + i,'r') as f:
          for line in f:
             word = ' '.join(line.split())
             word_list.append(word)
          if i == list2:
             output += random.choice(word_list) + '<br />'
          else:
             output += random.choice(word_list) + ' '
    return output
