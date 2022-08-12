def demo(name,adjective):
    print(f"{name} is {adjective} at Python programming!")

# POSITIONAL ARGUMENTS-- where the order (position) matters
# whatever the first argument is will be the first parameter, "name"
# whatever the second argument is will be the second parameter, "adjective"
demo("Prarthana", "awesome")
demo("amazing", "Marc")

# KEYWORD ARGUMENTS-- where the value of parameters are stated DIRECTLY
# "adjective" and "name" are being defined directly, so it doesn't matter
# in what order these arguments are made
demo(adjective="amazing", name="Darrin")

# DEFAULT ARGUMENTS
def demo(name="Chad",adjective="...ok"):
    print(f"{name} is {adjective} at Python programming!")

# *args
"""With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments)"""

def demo(name="Chad", *adjectives):
    print(f"{name} is a ", end= "")
    words= []
    for adj in adjectives:
        words.append(adj)
    print(", ".join(words), end= " ")
    print("Python programmer!")

demo()
demo("Phil","feisty", "zippy", "slappy")

# **kwargs
#**kwargs allows us to pass any number of keyword arguments to the function.

# **KWARGS (keyword arguments)
def demo(**stats):
    print(f"{stats['name']} statistics:")
    print(f"  • Age: {stats['age']}")
    print(f"  • Email: {stats['email']}")
    print(f"  • Country: {stats['country']}")

# writing a ton of arguments in one line (yuck)
demo(name="Chad", age=37, email="csfeeser@alta3.com", country="United States")

# putting those arguments in a dictionary...
data= {"name": "Chad",
       "age": 37,
       "email": "csfeeser@alta3.com",
       "country": "United States"}

# ...and passing all those key:value pairs as
# keyword arguments to the function
demo(**data)
