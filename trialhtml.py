import pandas as pd

file=pd.read_csv("songs_list (3).csv")
file.to_html("SongsTable.html")