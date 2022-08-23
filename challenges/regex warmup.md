## REGEX Warmup!

<img src=https://miro.medium.com/max/1200/1*ZVlIZ1ZYC6rASz-dYPzhZQ.jpeg alt="drawing" width="300"/>

### Part 1:

Take a look at the following string:

```
919.367.7887
898*982*9304
6308520397
786-307-3615
789
123765
1-1-1
+982
```

Can you devise a regular expression that would match the first four lines (phone numbers) but ignore the rest?

**SUGGESTION:** Use [Regex101](https://regex101.com/) to test your expression as you build it!

Here are some of the REGEX special characters/quantifiers we learned about yesterday (plus a few new ones you might like to try)!

```
.     - Any character (except new line)
\d    - Digit (0-9)

[]    - Matches characters in brackets
|     - Either/Or
( )   - Group

Quantifiers:
*     - 0 or more
+     - 1 or more
?     - 0 or one
{3}   - Exact amount of prior character
{3,4} - Range of prior character(s) amount {min, max}
```

### Part 2:

Now try it with Python! Try out a new `re` module function this morning: `findall()`

The findall() function returns a list containing all matches.
```
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
```

Use this function against the string above using the regular expression you wrote and return all those phone numbers!
