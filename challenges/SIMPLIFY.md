# Simplifying Code

<img src="https://images.squarespace-cdn.com/content/v1/56e0aa00a3360c10606c90b8/1467855766712-J37RID0B92VM6OQL2LE0/keeping-it-simple-project-plan-from-point-a-to-point-b.jpg" alt="drawing" width="500"/>

### If it works, it works! But as we get more and more proficient with Python, writing code that is SHORT and EFFICIENT is easier to read, easier to write, easier to reuse!

Below is code that WORKS, but it needs trimmed down!

```
#!/usr/bin/env python3

def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            
    if usr_date in [2011, 1999, 1987, 1975, 1963]:
        print(f"{usr_name} your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.")
    elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]:
        print(f"{usr_name} your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.")
    elif usr_date in [2010, 1998, 1986, 1974, 1962]:
        print(f"{usr_name} your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.")
    elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]:
        print(f"{user_name} your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.")
    elif usr_data in [2012, 2000, 1988, 1976, 1964]:    
        print(f"{usr_name} your zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.")
    elif usr_date in [2013, 2001, 1989, 1977, 1965]:
        print(f"{usr_name} your zodiac sign is Snake, you are wise, like to work alone, and determined.")
    elif usr_date in [2014, 2002, 1990, 1978, 1966]:
        print(f"{usr_name} your zodiac sign is Horse, you are animated, active, and energetic.")
    elif usr_date in [2015, 2003, 1991, 1979, 1967]:
        print(f"{usr_name} your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.")
    elif usr_date in [2016, 2004, 1992, 1980, 1968]:
        print(f"{usr_name} your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.")
    elif usr_date in [2017, 2005, 1993, 1981, 1969]:
        print(f"{usr_name} your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.")
    elif usr_date in [2018, 2006, 1994, 1982, 1970]:
        print(f"{usr_name} your zodiac sign is Dog, you are loyal, honest, cautious, and kind.")
    elif usr_date in [2019, 2007, 1995, 1983, 1971]:
        print(f"{usr_name} your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.")


main()
```

## SOLUTION 1

```python
#!/usr/bin/env python3
  
def main():
    usr_name = input("Please enter your name:\n>").title()
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    sign= usr_date % 12
    zodiac= [
      "your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.",
      "your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.",
      "your zodiac sign is Dog, you are loyal, honest, cautious, and kind.",
      "your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.",
      "your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.",
      "your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.",
      "your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
      "your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
      "your zodiac sign is Dragon, you are talented, powerful, lucky, and successful.",
      "your zodiac sign is Snake, you are wise, like to work alone, and determined.",
      "your zodiac sign is Horse, you are animated, active, and energetic.",
      "your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy."
    ]

    print(f"{usr_name}, {zodiac[sign]}")

main()
```

## SOLUTION 2

![]([image.png](https://github.com/MNM-Nick/scripts-png/blob/main/for%20loop%20used%20by%20mike,shamain,maurice.png?raw=true))

