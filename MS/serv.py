import re

file = open("7.txt","r").read().splitlines()
servlist = {}        
for line in file:


        inp, output, time = line.replace("->",":").split(":")
     
        for i in output:
          unit  = servlist[inp[0]]/len(inp) if len(inp)>0 else 1
          if i not in servlist:
            servlist[i] = unit 
          else:
            servlist[i] += unit

        if inp == "":
          print time
          continue
        else:
          print servlist[inp[0]]*int(time)/len(inp)

