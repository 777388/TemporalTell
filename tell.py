import sys
import math
import time
import pyttsx3
engine = pyttsx3.init()
be = 0
for char in sys.argv[1]:
    be += int(ord(char))
times = math.ceil(time.time() + be) % 100
system = lambda time: (time - math.fabs(time))
tell = []
for i in range(times):
    tell.append(i)
print(list(map(system, tell)))
engine.say(list(map(system, tell)))
engine.runAndWait()