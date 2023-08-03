# YAML Conversion Challenge

![yaml is teh funneh](https://i.redd.it/i4v9op0chrc51.jpg)

Run the following command:

`student@bchd:~$` `wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/favs.json`

[Here's what you just downloaded!](https://github.com/csfeeser/Python/blob/master/data%20sets/favs.json)

Do the following:

- Import the json file as a file object
- Add yourself and your favorites to this list!
- Output the data as a YAML file.

## SOLUTION

<details>
<summary>Click here to see a possible solution!</summary>
    
```python
import json
import yaml

# open file with json, convert to python object
with open("classdata.json","r") as jsonfile:
    x= json.load(jsonfile)

# create new python dictionary to be added
new= {
      "name":"Chad",
      "movie":"The Shawshank Redemption",
      "ice cream":"salted caramel",
      "color":"red"}
     }

# add to data read in from json file
x.append(new)

# open a yaml file and dump the changed data inside it
with open("classdataedit.yml","w") as yamlfile:
    yaml.dump(x, yamlfile)
```

</details>
