from pandas import Series
import pandas as pd
file = "oppenheimerWebData.pkl"
inv = pd.read_pickle(file)
values = inv.columns.values
print(values)
id1 = inv['visitor-ids']
id2 = inv['user-ids']
time = inv['timestamp']
web = inv['webpage']
state = inv['state']
platform = inv['platform']
print(inv)
print(inv)
