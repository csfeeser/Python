```
networklists = ['ios','ios-xr','junos','eos']

for networks in networklists:
    print(x)
```
| Syntax      | Terminology |
| ----------- | ----------- |
|'ios','ios-xr','junos','eos'|**elements** in the list `networklists`|
|networks|variable|
|networklists *(in for loop)*|iterable|
> the class of `networks` in this example is "string"
---

```
x= "string"
x.lower()
x.__add__
x.startswith("Eth")
```
| Syntax      | Terminology |
| ----------- | ----------- |
|\_\_add\_\_|string **attribute**|
|*x*|**variable**|
|*"string"*|**value** of the variable|
|*.lower()*|**method** (specifically, string method)|
|("Eth")|argument|
> The *x* variable belongs to the **string class**

### Importing/Reusing Code!

Inside of the same directory, create two files.

`vim module1.py`

```
#MODULE1
import module2

def funkytown():
    print("MODULE 1 is the best!")

funkytown()
module2.shindigville()
```

`vim module2.py`

```
#MODULE2
  
def shindigville():
    print("MODULE 2 is awesome!")
```

Once finished, run module1! Notice that it will import and run module2 as well.

`python3 module1`
