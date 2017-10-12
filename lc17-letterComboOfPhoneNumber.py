class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_dict = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"],}
        queue = []
        
        if len(digits)==0:
            return queue
        
 
        index = 0
        length = 1
        for i, digit in enumerate(digits):
            if digit in dig_dict:
                queue = list(dig_dict[digit])
                index = i+1
                break
            
        # if it's full of 1 and 0 in digits
        if len(queue) == 0:
            return queue
        
        while True:
            if index == len(digits):
                break
            if digits[index] not in dig_dict:
                index += 1 
                continue
            else:
                while len(queue[0]) == length:
                    popped = queue.pop(0)
                    for entry in dig_dict[digits[index]]:
                        queue.append(popped+entry)
                length += 1
                index += 1 
        
        return queue
