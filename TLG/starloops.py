# Chaynor
print_array = ["*"]
star = "*"
for i in range(9):
    print(" ".join(print_array))
    if (i < 4):
        print_array.append(star)
    else:
        print_array.pop()

# Julian
for num in range(1, 5):
    print("* " * num)
for num in range(5, 0, -1):
    print("* " * num)

# Wenhao
def construct_pattern(size):
  for i in range(1, size + 1):
    print("* " * i)
  for i in range(size - 1, 0, -1):
    print("* " * i)

construct_pattern(50)

# Patrick
def main():
    stars= ["*","* *","* * *","* * * *","* * * * *","* * * *","* * *","* *","*"]
    for x in range(len(stars)):
        print(stars[x])
main()

# Yichun
str="* "
for i in range(1,6):
    print(i*str)
for i in range(4,0,-1):
    print(i*str)

# Chaynor- PART 2: THE CHAYNORING
from math import floor
def create_asterisk_array(max_length=9.0):
    print_array = ["*"]
    star = "*"
    if max_length % 2 == 0:
        midpoint = max_length / 2 - 1
    else:
        midpoint = floor(max_length / 2)
    for i in range(max_length):
        print(" ".join(print_array))
        if (i < midpoint):
            print_array.append(star)
        elif (i >= midpoint and i < max_length - 1):
            print_array.pop()
create_asterisk_array(9)

# Julian- PART 2: RISE OF THE JULIANS
for num in [1, 2, 3, 4, 5, 4, 3, 2, 1]:
    print(("* " * num).strip())

# Xander
def printDots(num):
    for i in range(0, num):
        print('* ', end='')
def printStairs(num):
    for i in range(1, num):
        printDots(i)
        print()
    for i in range(num, 0, -1):
        printDots(i)
        print()

def dotsPrinting1(num):
    print(f"Solution # 1 - Printing dots: {num}")
    printStairs(num)

dotsPrinting1(5)

def printDotsDecrese(num):
    if num == 0:
        return
    else:
        printDots(num)
        print()
        printDotsDecrese(num-1)
def printDotsIncrease(num):
    if num == 0:
        return
    else:
        printDotsIncrease(num-1)
        printDots(num)
        print()
def dotsPrinting2(num):
    printDotsIncrease(num)
    printDotsDecrese(num-1)
dotsPrinting2(5)

# Seth
def starbuilder():
    starcount = [1,2,3,4,5]
    for star in starcount:
        counter = 0
        while counter < star:
            print('* ', end="")
            counter += 1
        print('')

def starremover():
    starcount = [4,3,2,1]
    for star in starcount:
        counter = 0
        while counter < star:
            print('* ', end="")
            counter += 1
        print('')

def main():
    starbuilder()
    starremover()

main()

# Rasoj
num = 5
for i in range(1, num+1):
    for j in range(1, i+1):
        print("* ",end="")
    print()
# reverse for loop
for i in range(num, 0, -1):
    for j in range(0, i):
        print("* ", end='')
    print("\r")

# Julian 3: ENDGAME

def pyramid(max):
    arr = [num for num in range(1, max)]
    arr.extend([num for num in range(max, 0, -1)])
    return arr

for num in pyramid(5):
    print(("* " * num).strip())

# Cristian

print_array = ['*']
new_star = '*'
def pyramid(height):
   mid = 0
   if height % 2 != 0:
       mid = (height - 1) / 2
   else:
       mid = height / 2
   for x in range(height):
       print(" ".join(print_array))
       if (x < mid):
           print_array.append(new_star)
       elif (x >= mid):
           print_array.pop()

pyramid(5)
