# reverse_geocoder module

Reverse geocoding is the process of finding a place or a location address from a given pair of geographic coordinates(latitude and longitude).

You'll need to install reverse_geocoder first!

`python3 -m pip install reverse_geocoder`

Below is example code that demonstrates reverse_geocoder's use:

```python
import reverse_geocoder as rg

lat= 28.613939
lon= 77.209023

# reverse_geocoder MUST be passed a tuple as the argument!
coords_tuple= (lat, lon)

result = rg.search(coords_tuple)
```

The `rg.search()` function will return a **list** that looks like this (technically it's an *ordered dictionary*, but you may treat it like the example you see below). Slice the value of `result` to get the data you need!

```
[{'admin1': 'NCT',
  'admin2': 'New Delhi',
  'cc': 'IN',
  'lat': '28.63576',
  'lon': '77.22445',
  'name': 'New Delhi'}]
```
