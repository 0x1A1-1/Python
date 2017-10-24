# Mirror a string
# o => o
# b => d 
# wood => boow 
# ee

def mirror_string(string1):
  if len(string1) == 0:
    return ""

  mirror_dict = {"A":"A", "H":"H", "I":"I", "M":"M", "O":"O","T":"T", "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y", "b":"d", "d":"b", "i":"i", "l":"l", "m":"m", "n":"n","o":"o", "p":"q", "q":"p", "u":"u", "v":"v", "w":"w","x":"x"}
  mirrored = []

  for letter in string1:
    if letter not in mirror_dict:
      return False
    else:
      mirrored.append(mirror_dict[letter])

  return "".join(mirrored[::-1])

print mirror_string("wood")
print mirror_string("baaa")
print mirror_string("AMOT")
print mirror_string("")
print mirror_string("bdpqA")
