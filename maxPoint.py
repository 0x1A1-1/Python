'''
Created on Feb 27, 2016

@author: Cigarent
'''
class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b
         
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxi=0
        if len(points) <= 1:
            return len(points)
        for i in range(len(points)):
            slope = []
            vert = 0;
            dup = 0
            for j in range(i+1, len(points)):
                if points[i].y==points[j].y and points[i].x==points[j].x:
                    dup+=1
                    break
                elif points[i].x==points[j].x:
                    vert+=1
                    continue
                slope.append((points[i].y-points[j].y)/(points[i].x-points[j].x))
            for x in slope:
                if slope.count(x)>maxi:
                    maxi=slope.count(x)
            print(dup, vert)
            maxi = max(maxi, vert)+dup
        return maxi+1
    ls = []
    ls.append( Point(1, 2) )
    ls.append( Point( 1, 3) )
    ls.append( Point( 1, 4) )
    ls.append( Point( 1, 5) )
    print(maxPoints(object, ls))
    
'''my verison still doesnt work'''