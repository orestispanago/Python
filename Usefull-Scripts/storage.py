import os

storage = os.popen("df -m").readlines()
print(*storage) # * means print all items in list
