

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams
from Class.dataG import DataG
import pandas

test = DataG

df = pandas.read_csv('Data/DEMOGRAPHICS.csv')
df.head()
df.isnull().any()
df.dtypes
print(df)
#fig = plt.figure(figsize=(12, 6))
#sqft = fig.add_subplot(121)
#cost = fig.add_subplot(122)

#sqft.hist(df.sqft_living, bins=80)
#sqft.set_xlabel('Ft^2')
#sqft.set_title("Histogram of House Square Footage")

#cost.hist(df.price, bins=80)
#cost.set_xlabel('Price ($)')
#cost.set_title("Histogram of Housing Prices")

#plt.show()

