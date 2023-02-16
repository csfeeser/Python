challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

e= challenge[num][num]
g= challenge[num][num]
n= challenge[num]

print(f"My {e}! The {g} do {n}!")
# ======================================================================
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

e= trial[num][str]
g= trial[num][str]
n= trial[num]

print(f"My {e}! The {g} do {n}!")
# =====================================================================
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e= nightmare[num][str][str][str]
g= nightmare[num][str]
n= nightmare[num][str]

print(f"My {e}! The {g} do {n}!")
