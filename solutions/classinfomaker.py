tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

animals= ["Donkey", "Goat", "Guinea pig", "Horse", "Pig", "Rabbit", "Water buffalo", "Chicken", "Duck", "Goose", "Pigeon", "Turkey", "Aardvark", "Aardwolf", "Elephant", "Leopard", "Albatross", "Alligator", "Alpaca"]

superpowers= ["Super Strength", "Weather Control", "Flight", "X-ray Vision", "Helicopter Propulsion", "Invisibility", "Immobility", "Immutability", "Invulnerability", "Jet Propulsion", "Matter Ingestion", "Mobile Invulnerability", "Muscle Manipulation", "Nail Manipulation", "Needle Projection", "Organic Constructs", "Prehensile Hair", "Prehensile Tail", "Prehensile Tongue", "Regenerative Healing Factor", "Replication", "Self-Detonation", "Sharp Tail", "Spike Protrusion", "Structure Weakening"]

adj= ["admirable", "amazing", "astonishing", "awesome", "brilliant", "cool", "enjoyable", "excellent", "fabulous", "fantastic", "fine", "incredible", "magnificent", "marvelous", "outstanding", "phenomenal", "pleasant", "pleasing", "remarkable", "sensational", "strange", "superb", "surprising", "terrific", "tremendous", "wondrous"]


print("""
classinfo= {
    "all": [""")
for x in range(len(tlgstudents)):
    y= x-1
    z= (f"'name':'{tlgstudents[y]}','skill level':'{adj[y]}','spirit animal':'{animals[y]}','super power': '{superpowers[y]}'")
    print("{" + z + "},")
print("]")
print("}")
