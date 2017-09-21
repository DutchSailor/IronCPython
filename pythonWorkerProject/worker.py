import sys
import json
import time

inputObject = json.load(open('C:/Users/Bart/Documents/Visual Studio 2017/Projects/IronPythonApplication1/IronPythonApplication1/' + sys.argv[1]))

if inputObject['operatie'] == 'vermenigvuldigen':
    print(inputObject['nummer1'] * inputObject['nummer2'])
else:
    print('not implemented :-(')
    print(inputObject)