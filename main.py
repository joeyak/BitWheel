import random
import sys

import pyperclip

count = 1
if len(sys.argv) > 1:
    try:
        count = int(sys.argv[1])
    except ValueError:
        pass

a = [
    "Cheer", "bday", "Kappa", "HeyGuys", "TriHard", "Kreygasm", "4Head",
    "SwiftRage", "NotLikeThis", "FailFish", "VoHiYo", "PJSalt",
    "MrDestructoid", "bitboss", "muxy", "streamlabs", "DoodleCheer",
    "RipCheer", "Shamrock", "EleGiggle", "DansGame", "FrankerZ", "SeemsGood",
    "Party", "Pride", "Goal", "HolidayCheer", "ShowLove"
]

b = []

for i in range(5):
    choice = random.choice(a)
    a.remove(choice)
    b.append(choice + str(count))

s = ' '.join(b)
print(s)
pyperclip.copy(s)
