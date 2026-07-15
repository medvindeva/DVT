#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

df = pd.read_csv("fifa_world_cup_2026_player_performance.csv")

print(df.head())


# In[7]:


import pandas as pd

df = pd.read_csv("fifa_world_cup_2026_player_performance.csv")

df.to_csv("output.csv", index=False)

print("Data exported successfully")


# In[8]:


import pandas as pd

df = pd.read_excel("fifa_world_cup_2026_player_performance.xlsx")

print(df.head())


# In[9]:


import pandas as pd
import sqlite3

df = pd.read_csv("fifa_world_cup_2026_player_performance.csv")

print(df.head())

df.to_json("fifa_players.json", orient="records", indent=4)

df.to_excel("fifa_players.xlsx", index=False)

conn = sqlite3.connect("fifa_players.db")
df.to_sql("player_performance", conn, if_exists="replace", index=False)
conn.close()

print("CSV file imported successfully.")
print("JSON file created: fifa_players.json")
print("Excel file created: fifa_players.xlsx")
print("SQL database created: fifa_players.db")


# In[ ]:




