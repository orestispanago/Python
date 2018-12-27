''' Gets WIFI SSID and IP using system commands (Linux)'''

import os

ssid = os.popen("iwgetid").readlines()
local_ip = os.popen("hostname -I").readlines()
print(*ssid,*local_ip) # * means print all items in list
