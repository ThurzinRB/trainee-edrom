from os import listdir
import os.path
#from os.path import isfile, join, dirname


# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Join the script directory with the 'datasetlabels' directory using a relative path
mypath = os.path.join(script_dir, 'datasetlabels')

# print(mypath)


fileNames = [f for f in listdir(mypath) if os.path.isfile(os.path.join(mypath,f))]
for fileName in fileNames[1:]:
    f = open(os.path.join(mypath, fileName), 'r')
    fileString = f.read()
    fileString = '1 ' + ' '.join(fileString.split(' ')[1:])
    print(fileString)
    f.close()
    f = open(os.path.join(mypath, fileName), 'w')
    f.write(fileString)

    

# print (fileNames)