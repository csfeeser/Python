### PYPLOT

```
from matplotlib import pyplot as plt
import pandas as pd

data= pd.read_csv("annualcheeseconsumed.txt")

year= data["Year"] # pandas SERIES
cheddar= data["Cheddar"]
swiss= data["Swiss"]
muenster= data["Muenster"]

# adding two different pieces of data to the plot
plt.plot(year, 
         cheddar, 
         label="Avg. Cheddar Consumed")
plt.plot(year, 
         swiss, 
         label="Avg. Swiss Consumed")
plt.plot(year, 
         muenster, 
         label="Avg. Muenster Consumed")

plt.legend()
plt.grid()

plt.xlabel("Year")
plt.ylabel("Cheese Consumed in Pounds Per Year")
plt.title("AMERICANS LOVE CHEESE!")

plt.show()
```

### SUBPLOT

```
from matplotlib import pyplot as plt
import pandas as pd

data= pd.read_csv("annualcheeseconsumed.txt")

year= data["Year"] # pandas SERIES
cheddar= data["Cheddar"]
swiss= data["Swiss"]

# NEW
fig, (ax1, ax2)= plt.subplots(nrows=2, ncols=1, sharey=True)


# adding two different pieces of data to the plot
ax1.plot(year, 
         cheddar, 
         label="Avg. Cheddar Consumed")
ax2.plot(year, 
         swiss, 
         label="Avg. Swiss Consumed")

ax1.legend()
ax1.set_title("American Cheese Consumption Trends")
ax1.set_ylabel("Avg. Pounds Consumed Per American")

ax2.legend()


plt.show()
```
