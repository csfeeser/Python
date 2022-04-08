## Followup Challenge

<img src="https://memegenerator.net/img/instances/75707830.jpg" width="300"/>

Check out the Cat Facts API at https://cat-fact.herokuapp.com/facts

Your mini challenge is to do the following:

- Return the JSON from this API and convert it into a Python list (use `requests.get()`)
- Loop through the data and print out the cat fact ONLY.
- **BONUS**: return a RANDOM cat fact every time the script runs! 

<details>
<summary>Help me get started!</summary>

```
import requests

url= "https://cat-fact.herokuapp.com/facts"

resp= requests.get(url).json()
```
</details>

<details>
<summary>Help me do a for loop!</summary>

```
import requests

url= "https://cat-fact.herokuapp.com/facts"

resp= requests.get(url).json()
  
for x in resp:
    print(x)
```
</details>

<details>
<summary>How can I randomize which fact I get?</summary>

Append the facts to a list. Then use random.choice(FACTLIST) to return a random fact!
</details>
