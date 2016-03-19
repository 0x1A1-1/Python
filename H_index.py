class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations==[]:
            return 0
        sortL = citations
        sortL.sort()
        sortL.reverse()
        print(sortL)
        h = len(sortL)
        if sortL[h-1]>=h:
            return h
        h-=1
        while h>0:
            if sortL[h-1]>=h and sortL[h]<=h:
                return h
            else:
                h-=1
        return h
