import re

class Tracker():

  def __init__(self):
    self.servers = {}

  def next_server_number(self, numbers):
    index = 1
    while True:
      if index in numbers:
        index += 1
      else:
        return index
  
  def allocate(self, serverName):
    if serverName not in self.servers:
      self.servers[serverName] = [1]
      return serverName + "1"
    else:
      next_avail_number = self.next_server_number(self.servers[serverName])
      self.servers[serverName].append(next_avail_number)
      return serverName + str(next_avail_number)

  def deallocate(self, serverName):
    serverName_strip = re.search("([a-zA-Z]+)([0-9]+)", serverName).group(1)
    num = re.search("([a-zA-Z]+)([0-9]+)", serverName).group(2)
    if serverName_strip in self.servers:
       if int(num) in self.servers[serverName_strip]:
         self.servers[serverName_strip].remove(int(num))
       else:
         return False
    else:
       return False
'''
test_case1 = [5, 3 ,1]
print next_server_number(test_case1)
test_case1 = []
print next_server_number(test_case1)
test_case1 = [2, 3 ,1]
print next_server_number(test_case1)
test_case2 = [x for x in range(1000)]
print next_server_number(test_case2)
test_case2 = [x for x in range(1000) if x != 300]
print next_server_number(test_case2)
'''
tracker = Tracker()
print tracker.allocate("apibox")
print tracker.allocate("apibox")
print tracker.allocate("apibox")
print tracker.allocate("apibin")

#deallocate test
tracker.deallocate("apibox1")
tracker.deallocate("apibox2")
print tracker.allocate("apibox")
print tracker.allocate("apibox")
