import re

file = open("6.txt","r").read().splitlines()
for line in file:
        orig_list = line.split("\\")[1:]
        for item in orig_list:
          index = orig_list.index(item)
          if item.count(".") == len(item) and len(item) != 0 :
	    start =  index- len(item) + 1
            
            if start>0:
              orig_list =  orig_list[0:start] + orig_list[index+1:]
            else:
              orig_list =  orig_list[index+1:]
          elif item == "*":
            orig_list = orig_list[index+1:]
          elif item == "":
            orig_list =  orig_list[0:index] + orig_list[index+1:]

        print "\\"+"\\".join(orig_list)
