# YAML Conversion Challenge

![yaml is teh funneh](https://i.redd.it/i4v9op0chrc51.jpg)


## Objective

There are certainly many tools out there that can make data conversion into and out of YAML a snap... but when you write YAML in Ansible, that doesn't help! Your objective is to successfully make conversions (by hand!) of the data objects below.

### CHALLENGE 1

Take this Python dictionary and convert it into YAML.

```json
{"brand": "Ford",  "model": "Mustang",  "year": 1964}
```

<details>
  <summary>Solution</summary>

```
brand: Ford
model: Mustang
year: 1964
```
    
</details>
    
### CHALLENGE 2

Take this YAML object and convert it into Python!

```yaml
- banana
- apple
- cherry
- kumquat
```

<details>
  <summary>Solution</summary>

```json
["banana", "apple", "cherry", "kumquat"]
```
    
</details>

### CHALLENGE 3

Take this Python dictionary and convert it into YAML.

```json
{
  "name": "Wolverine",
  "powers": [
    "claws",
    "regeneration",
    "cigars"
  ]
}
```

<details>
  <summary>Solution</summary>

```yaml
name: Wolverine
powers:
- claws
- regeneration
- cigars
```
    
</details>

### CHALLENGE 4

Take this YAML object and convert it into Python!

```yaml
metadata:
  name: Wade Wilson
  alias: Deadpool
  alive: True
powers:
  - regeneration
  - sass
```

<details>
  <summary>Solution</summary>

```json
{
  "metadata": {
    "name": "Wade Wilson",
    "alias": "Deadpool",
    "alive": True
  },
  "powers": [
    "regeneration",
    "sass"
  ]
}
```
    
</details>




