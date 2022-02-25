# LOOPING DICTIONARIES Challenge!

```
fruitcompanies= [{"name":"Zesty","employees":["Bryan", "Colin", "Erik", "Greg", "John"]},
                 {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Chad"]},
                 {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                 {"name":"JuiceGrove","employees":["Tim", "Travis", "Trung"]}]
```

### Part 1

• Write a for loop that returns all the employees from the company you "work" for!

### Part 2

• Ask a user to choose a company. Return the employees that belong to that group.

### Part 3

• Ask a user to choose a company (Zesty, Ripe.ly, FruitBee, or JuiceGrove) and return the employees... but DO NOT return "Chad" He got fired this morning.


## SOLUTIONS

```python
fruitcompanies= [{"name":"Zesty","employees":["Bryan", "Colin", "Erik", "Greg", "John"]},
                 {"name":"Ripe.ly","employees":["Kishor", "Leia", "Maria", "Chad"]},
                 {"name":"FruitBee","employees":["Monte", "Jarrad", "Pemba", "Don"]},
                 {"name":"JuiceGrove","employees":["Tim", "Travis", "Trung"]}]

# Write a for loop that returns all the employees from the company you "work" for!

for x in fruitcompanies[1]["employees"]:
    print(x)

# Ask a user to choose a company. Return the employees that belong to that group.

choice= input("Choose a company: Zesty, Ripe.ly, FruitBee, JuiceGrove\n>")

for company in fruitcompanies:
    if choice == company["name"]:
        print(company["employees"])

# Ask a user to choose a company (Zesty, Ripe.ly, FruitBee, or JuiceGrove) and return the employees... but DO NOT return "Chad" He got fired this morning.

x= 0
for company in fruitcompanies:
    x += 1
    print(f"{x}. {company['name']}")

choice= int(input("Choose your company!\n>"))

for x in fruitcompanies[choice - 1]["employees"]:
   if x != "Chad":
        print(x)
```
