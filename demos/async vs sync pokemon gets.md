# SYNCHRONOUS SCRIPT- syncversion.py

```python
#!/usr/bin/python3

# standard library
import time

# python3 -m pip install requests
import requests

def main():
    # start a timer
    start_time = time.time()

    with open("syncpokelist.txt", "w") as foo:
        # typical loop
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            resp = requests.get(url)
            pokemon = resp.json()
            name= pokemon["name"]
            id_num= pokemon["id"]
            print(f"{id_num}. {name}", file=foo)

        print("--- %s seconds ---" % (time.time() - start_time))

# call our script if it was not imported
if __name__ == "__main__":
    main()
```


# ASYNCHRONOUS SCRIPT- imports syncversion.py
```python
#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Demonstrating how to use the asyncio library by utilizing the pokeapi.co
   to perform 150 HTTP GET lookups"""

# standard library
import asyncio
import time
from pprint import pprint
import json
import syncversion
# python3 -m pip install aiohttp
import aiohttp

# GLOBAL VARIABLE
pokedict= {}


async def filemaker():
    with open("asyncpokedex.txt", "w") as bar:
        for key in sorted(pokedict):
            print("{}. {}".format(key, pokedict[key]), file=bar)

async def make_request(session, pokemon_url):
    global pokedict
    # the coroutine we are defining should be run async with an event loop
    async with session.get(pokemon_url) as resp:
        response = await resp.json()
        name= response["name"]
        id_num= response["id"]
        entry= {id_num: name}
        pokedict.update(entry)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 151):
            # Create a task for each of our requests
            task = asyncio.create_task(
                make_request(session, f"https://pokeapi.co/api/v2/pokemon/{number}")
            )
            tasks.append(task)

        # Run awaitable objects (tasks) concurrently
        await asyncio.gather(*tasks)
        await filemaker()

if __name__ == "__main__":
    syncversion.main()
    start_time = time.time()
    asyncio.run(main())
    print("ASYNC VERSION TIME: --- %s seconds ---" % (time.time() - start_time))
```
