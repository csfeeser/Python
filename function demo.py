# POSITIONAL AND KEYWORD ARGUMENTS
def demo(name,adjective):
    print(f"{name} is {adjective} at Python programming!")

demo(Prarthana, awesome)
demo(amazing, Marc)
demo(adjective=amazing, name=Darrin)

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
**kwargs allows us to pass the variable length of keyword arguments to the function.

def demo(name="Chad", **stats):
    print(f"{name} statistics:")
    for key,value in stats.items():
        print(f"  • {key}: {value}")

demo(name="Chad", Age=37, Email="csfeeser@alta3.com", Country="United States")
