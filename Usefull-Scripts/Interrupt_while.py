import datetime,time

t = datetime.datetime.now()
print(t)

try:
   while True:
       print(t)
       time.sleep(1)
except KeyboardInterrupt:
   print('interrupted!')