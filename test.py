





from LazyCartesianProduct import LazyCartesianProduct
from cmdGen import cmdGen 

def example():


  cmd = "testCMD "
  attr = ["-CPU:", "-MEM:", "-POWER:", "OPTION:", "OPTION:", "arg1:", "arg2:"]

  cpu = [ 1, 2, 3, 4, 5 ]
  mem = [ 'foo', 'bar' ]
  power = [ 'x', 'y', 'z' ]
  option = [ '-a', '-b', '-c' ]
  option1 = ['--settingTwoArg=']
  arg1 = ['test11', 'test12']
  arg2 = ['test21', 'test22']

  sets = [ cpu, mem, power, option, option1, arg1, arg2 ]




  

  commandGenerator = cmdGen()

  cp = LazyCartesianProduct(sets)

  fp = open("foo.txt", "wb")
  commandGenerator.clearStr()

  for i in range(0, cp.maxSize):
    result = cp.entryAt(i)
    commandGenerator.clearStr()
    for j in range(len(result)):
      commandGenerator.addToken(str(attr[j]) + str(result[j]) + ", ")
      #fp.write(str(attr[j]) + str(result[j]) + ", ")
    out = commandGenerator.parse()
    fp.write(cmd + out + "\n");

  fp.close()



example()
