### Making text appear one character at a time.

```python
import sys, time

def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print

print1by1("Hello there!")
```

### Put list into column output

```python
CATEGORIES= {9: 'General Knowledge', 10: 'Entertainment- Books', 11: 'Entertainment- Film', 12: 'Entertainment- Music', 13: 'Entertainment- Musicals & Theater', 14: 'Entertainment- Television', 15: 'Entertainment- Video Games', 16: 'Entertainment- Board Games', 17: 'Science- Nature', 18: 'Science- Computers', 19: 'Science- Mathematics', 20: 'Mythology', 21: 'Sports', 22: 'Geography', 23: 'History', 24: 'Politics', 25: 'Art', 26: 'Celebrities', 27: 'Animals', 28: 'Vehicles', 29: 'Entertainment- Comics', 30: 'Science- Gadgets', 31: 'Entertainment- - Japanese Anime & Manga', 32: 'Entertainment- - Cartoon Animations'}

# combine key/value pairs into list of strings ["23. History", "22. Geography"... ]
foolist = [f"{x}. {y}" for x, y in CATEGORIES.items()]

for a,b,c in zip(foolist[::3],foolist[1::3],foolist[2::3]):
    print('{:<50}{:<50}{:<}'.format(a,b,c))
```
### Make a string center-justified in your output

```python
import shutil

def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))

print_center("The center cannot hold. -Yeats")
```

### Fill screen with random colorful strings

```python
# python3 -m pip install asciimatics
from random import randint
from asciimatics.screen import Screen

def demo(screen):
    while True:
        screen.print_at('Hello world!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

Screen.wrapper(demo)
```
    
### Clear screen while still in program
    
```python
def clearScreen():
   # check and make call for specific operating system
   if os.name =='posix:
     os.system('clear')
   else:
     os.system('cls')
```
