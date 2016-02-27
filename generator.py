'''
Created on Feb 19, 2016

@author: Sean
'''
from __builtin__ import str
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
