## FRIDAY CHALLENGE
### Fix a broken function

0. Create a text file to house a list of insults!

`student@napya-000-bchd:~$` `vim ~/mycode/insults.txt`

0. Paste the following into your insults list:

```
artless, base-court apple-john
bawdy, bat-fowling baggage
beslubbering, beef-witted barnacle
bootless, beetle-headed bladder
churlish, boil-brained boar-pig
cockered, clapper-clawed bugbear
clouted, clay-brained bum-bailey
craven, common-kissing canker-blossom
currish, crook-pated clack-dish
dankish, dismal-dreaming clotpole
dissembling, dizzy-eyed coxcomb
droning, doghearted codpiece
errant, dread-bolted death-token
fawning, earth-vexing dewberry
fobbing, elf-skinned flap-dragon
froward, fat-kidneyed flax-wench
frothy, fen-sucked flirt-gill
gleeking, flap-mouthed foot-licker
goatish, fly-bitten fustilarian
gorbellied, folly-fallen giglet
```
0. Create a new Python script.

`student@napya-000-bchd:~$` `vim ~/mycode/broken_function_challenge.py`

0. Paste the following script into vim.

```
#!/usr/bin/env python3
import random

num= (input("How many Shakespearean insults would you like?")

insult_list= open("/home/student/mycode/insults.txt", "r")

def insult_generator(num):
    print("You are a", end="")
    for x in num:
      print(random.choice(insults))

insult_generator()
```

0. This function has multiple errors that prevents it from returning a list of insults! You should be able to enter a number and receive that number of insults back. Troubleshoot and get it working!
