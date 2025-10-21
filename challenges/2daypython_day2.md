# 🐍 Day 2 Warm-Up: Fix the Broken Horoscope Program

<img src="https://github.com/user-attachments/assets/ce56b883-ea7b-4dc0-a036-cab8fda35c5b" width="300">

Today’s challenge is to debug a short Python script!
The code is supposed to tell you your Python class horoscope based on your zodiac sign, but something’s wrong.
It has **three errors**, and your job is to find and fix them.

## Procedure

1. Open your file:

   ```bash
   vim ~/mycode/day2warmup.py
   ```

2. Copy the broken code below and paste it into that file.

3. Run it with:

   ```bash
   python3 ~/mycode/day2warmup.py
   ```

4. You’ll get errors. That’s expected!
   **Fix all three** so the program:

   * Prompts for your zodiac sign
   * Prints your horoscope (if the sign is valid)
   * Repeats prompting if you keep typing in an invalid sign

## 💥 Broken Code (Needs Fixing)

> Line numbers start at 1 for the first line of this code block.

```python
def horoscope()
    horoscopes = {
        "aries": "You're going to crush today’s Python class! LOOPS WILL FEAR YOU!",
        "taurus": "Your persistence will pay off when debugging that tricky syntax error.",
        "gemini": "Your curiosity will lead to some awesome discoveries in Python today.",
        "cancer": "Your creativity will shine when writing your first function.",
        "leo": "Everyone will admire your confidence when your code runs perfectly!",
        "virgo": "Your attention to detail will make your program flawless.",
        "libra": "You’ll find perfect balance between print statements and logic today.",
        "scorpio": "Your focus will help you master the while loop like a pro.",
        "sagittarius": "Adventure awaits! You’ll explore new Python concepts fearlessly!",
        "capricorn": "Your discipline will make today’s lesson look easy.",
        "aquarius": "You’ll have a brilliant idea that makes everyone say WHOA!",
        "pisces": "Your imagination will make your Python code surprisingly elegant."
    }

    while True:
        sign = input("Enter your zodiac sign: ").lower()

        if sign in horoscope:
            print(horoscopes[sign])
            brake
        else:
            print("That’s not a valid sign! Try again.\n")

# Run the function
horoscope()
```

## 🔍 Hints (Click to Expand)

<details>
<summary>Hint for Line 1</summary>
Functions in Python need a special character at the end of their definition line. It’s easy to forget!
</details>

<details>
<summary>Hint for Line 27/20</summary>
You’re checking against a variable that doesn’t exist! Compare it with the dictionary name above.
</details>

<details>
<summary>Hint for Line 27/22</summary>
The command to stop a loop is almost spelled like what you see, but not quite.
</details>

## ✅ Full Solution (Click to Reveal)

<details>
<summary>Show the fixed version</summary>

```python
def horoscope():  # FIX 1: Added missing colon
    horoscopes = {
        "aries": "You're going to crush today’s Python class — loops will fear you!",
        "taurus": "Your persistence will pay off when debugging that tricky syntax error.",
        "gemini": "Your curiosity will lead to some awesome discoveries in Python today.",
        "cancer": "Your creativity will shine when writing your first function.",
        "leo": "Everyone will admire your confidence when your code runs perfectly!",
        "virgo": "Your attention to detail will make your program flawless.",
        "libra": "You’ll find perfect balance between print statements and logic today.",
        "scorpio": "Your focus will help you master the while loop like a pro.",
        "sagittarius": "Adventure awaits — you’ll explore new Python concepts fearlessly!",
        "capricorn": "Your discipline will make today’s lesson look easy.",
        "aquarius": "You’ll have a brilliant idea that makes everyone say ‘whoa!’",
        "pisces": "Your imagination will make your Python code surprisingly elegant."
    }

    while True:
        sign = input("Enter your zodiac sign: ").lower()

        if sign in horoscopes:  # FIX 2: Correct variable name
            print(horoscopes[sign])
            break               # FIX 3: Correct keyword spelling
        else:
            print("That’s not a valid sign! Try again.\n")

# Run the function
horoscope()
```

</details>
