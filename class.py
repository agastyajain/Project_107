import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg

dataFrame = pd.read_csv("data.csv")
stList = list(set(dataFrame["student_id"]))
studentDf = dataFrame.loc[dataFrame['student_id']=="TRL_abc"]

print(stList)

groupedData = dataFrame.groupby("level")["attempt"].mean()
print(groupedData)

stgroupedData = studentDf.groupby("level")["attempt"].mean()
#print(stgroupedData)

figure = pg.Figure(pg.Bar(x=stList,y=groupedData))

#figure = pg.Figure(pg.Bar(x=["Level 1","Level 2","Level 3","Level 4"],y=stgroupedData))
figure.show()