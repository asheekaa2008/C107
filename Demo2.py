import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
studentDf=df.loc[df['student_id']=="TRL_987"]
print(studentDf.groupby('level')['attempt'].mean())
figure=go.Figure(go.Bar(x=studentDf.groupby("level")["attempt"].mean(),y=["level1","level2","level3","level4"],orientation='h'))
figure.show()