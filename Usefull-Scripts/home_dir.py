''' Gets home folder path'''
from pathlib import Path
home = str(Path.home())
print(home)

''' Gets home folder name'''
import os
print(os.path.basename(home))

'''Alternative and smaller'''
import os
home = os.path.expanduser("~")
print(home)
print(os.path.basename(home))
