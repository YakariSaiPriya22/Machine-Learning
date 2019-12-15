import os
import pandas as pd

os.getcwd()

data = pd.read_csv("C:\\Users\\mojotics\\Desktop\\mtcars.csv")

data.head()

data['len_of_cars'] = data['Car_model'].str.len()

data[data['len_of_cars'] == max(data['Car_model'].str.len())]