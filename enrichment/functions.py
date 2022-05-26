#!/usr/bin/env python3

# POSITIONAL & KEYWORD ARGUMENTS

def positional(name,adjective):
    return f"{name} is {adjective} at Python programming!"


# DEFAULT ARGUMENTS

def positional(adjective="...ok" , name="Chad"):
    return f"{name} is {adjective} at Python programming!"


# *args
# any number of extra arguments can be tacked on to your parameters (even zero extra arguments)
# passing in an args is like passing in a list

def argsdemo(name, *adjectives):
    print(name + " is a", end= "")
    # think of it as a list
    for adj in adjectives:
        print(adj, end=" ")
    print(" Python programmer!")

argsdemo("Darrin","awesome","wonderful","fantastic","stupendous")


# **kwargs
# allows us to pass in as many keyword arguments as we want (or none)
# like passing in a dictionary

def slappy(name, **kwargs):
    print(f"Facts about {name}:")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

florgledorgle= {"Age":37,
        "email": "csfeeser@alta3.com",
        "Country": "United States"}

slappy("Chad", **florgledorgle)
slappy("Chad", Age=37, email="csfeeser@alta3.com", Country="United States")

# advantage: instead of writing a function call with all your arguments, you can just basically pass in a dictionary of key/value pairs
