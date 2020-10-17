from datetime  import datetime
while True:
   now = datetime.now()
   t = now.strftime("%H:%M:%S") 
   print(t)