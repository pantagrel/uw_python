#-------------------------------------------------------------
#ex. 14.0

import os 
# fout = open('output.txt', 'w')
# #print fout
# 
# x = 53
# fout.write(str(x))

###store local/relative current working directory as path in cwd 
cwd = os.getcwd()
###same as above, but find and return the global/absolute path
owd = os.path.abspath('exerciseTeens.py')
#print owd
print cwd

#-------------------------------------------------------------
#ex. 14.1
def walk(dirname):
#for every file inside the parent directory 
  for name in os.listdir(dirname):
##put filename and it's parent directory path variable
    path = os.path.join(dirname, name)
##if there is a file to join, that is...
    if os.path.isfile(path):
      print path
##otherwise, keep looking recursively  
    else:
      walk(path)

#walk(cwd)

# trail = os.walk('python_class/uw_python', topdown = False)
# print trail

#-------------------------------------------------------------
#ex. 14.2

