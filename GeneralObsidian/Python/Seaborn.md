# Intro

- Note : we have to use seaborn with pandas and matplotlib becuz it works like that.

- Seaborn is a data visualization library built on top of the matplot lib and pandas data structures.
- graphs in matplotlib are very simple whereas in seaborn graphs are already butifool.
- Dependencies of seaborn 
	- python :-)
	- numpy 
	- scipy
	- matplotlib
	- pandas
- pip install seaborn
- import seaborn as sns

# Line Plot

- seaborn works on datasets, so it wont show graph of the following code.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var=[1,2,3,4,5,6,7]
var_1=[2,3,1,5,2,7,3]

sns.lineplot(x="var",y="var_1")



# Do following to plot
# Because seaborn works with pandas data structures

# Here in data=panda dataframe

x_1=pd.Dataframe({"var":var,"var_1":var_1})
sns.lineplot(x="var",y="var_1",data=x_1)

```

```python
import seaborn as sns

import matplotlib.pyplot as plt

data=sns.load_dataset(r"penguins")
# these are some of the inbuilt datasets

# data=sns.load_dataset(r"diamonds").head()
# like pandas

# print(data)

sns.lineplot(x="carat",y="price",data=data,style="sex",pallete="viridis",markers=["o",">"],dashes=False,legend=False)


plt.grid()
plt.title("Title")
plt.show()
```

Parameters
- hue
- size
- style
- palette
	- colorbar in matplotlib
	- selects the colors
- markers
- dashes
- legend=False to remove legend
	- auto 
	- brief
	- full
	- boolean





# Histogram

```python
data=pd.read_csv(".\data\penguins.csv")

sns.displot(var["bill_length_mm"],bins=[170,180,190,200,210,220,230,240],kde=True,rug=True,color="b",log_scale=True)
plt.show()

```

Parameters
- bins
- kde 
	- kernel density value
- rug
	- shows kernel density in graph
- color
- log_scale


# Bar chart

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=pd.read_csv(".\data\penguins.csv")
sns.barplot(x=data,y=var.bill.island)
# sns.barplot(x=var.island)
# equivalent to sns.barplot(x="island",data=data)

```

Parameters
- hue
- order=\[list in order you want to display\]
- hue_order=\[list to set order in hue\]
- ci
- n_boot
- orient="v" or "h"
- color
- pallete
- saturation : color of the plot