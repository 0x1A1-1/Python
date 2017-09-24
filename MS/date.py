import re

file = open("3.txt","r").readlines()
for line in file:
        try: 
          date, orig, fmt = line.split()
        except:
          break
        orig_symbol = re.search("[^a-z]", orig).group(0)
        new_symbol  = re.search("[^a-z]", fmt).group(0)

        orig_seq = orig.split(orig_symbol)
        orig_number = date.split(orig_symbol)
        new_seq = fmt.split(new_symbol)

        result = [0, 0, 0]
        for i in range(0,3):
          result[i] = orig_number[orig_seq.index(new_seq[i])]

        print new_symbol.join(result)
