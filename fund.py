import pickle as p
import pandas as pd

phil = "oppenheimerWebData.pkl"

df = pd.read_pickle(phil)
dimDF = len(df)

# column values
values = df.columns.values	
dimVal = len(values)

# extract data into list
visitorID = df['visitor-ids'].tolist()
userID = df['user-ids'].tolist()
time = df['timestamp'].tolist()
web = df['webpage'].tolist()
state = df['state'].tolist()
browser = df['browser'].tolist()
platform = df['platform'].tolist()

print("yo waddup")
