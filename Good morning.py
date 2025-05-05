import time
timestamp=time.strftime('%H: %M: %S')
print(timestamp)
timestamp=int(time.strftime('%H'))

if(timestamp>=4 and timestamp<=12):
    print("good morning")
elif(timestamp>=13 and timestamp<=16):
    print("good afternoon")
elif(timestamp>=17 and timestamp<=18):
    print("good evening")
else:
    print("good night")