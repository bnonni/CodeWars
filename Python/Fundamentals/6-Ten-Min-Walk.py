"""def isValidWalk(walk):
    start = 0
    for i in walk:
      if 'n' or 'e' in walk:
        start+1
      else:
        start-1
    if start == 0:
      return True
    else:
      return False

print(isValidWalk(['n', 's','w,'w']))
                    1    2   3  4
print(isValidWalk(['n', 's','e','w','n', 's','e','w', 'n', 'w']))
                    1    -1  1   -1  1    -1  1   -1   1    -1             
print(isValidWalk( ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
                  #  -1   1    -1   1    1    -1   1    -1   1    -1
                  """
#n & e = 1
#s & w = -1
start = (0 + 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1 + 1 - 1)
print(start)