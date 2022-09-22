import os
import sys

def AddModulePath(isDebug: bool = False):
    pwd:str = os.path.dirname(os.path.abspath(__file__))
    sourcePath = os.path.sep.join(pwd.split(os.path.sep)[:-1])
    sys.path.append(os.path.join(sourcePath, 'src'))
    if isDebug:
        pwd:str = os.path.dirname(os.path.abspath(__file__))
        print(f'pwd:{pwd}')
        print(f'os.path.sep:{os.path.sep}')
        pwdDirectorys = pwd.split(os.path.sep)
        print(pwdDirectorys)
        print(sys.path)
