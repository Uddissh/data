import pandas as pd
import plotly.express as px
data=pd.read_csv("/content/dataop.csv")
fig=px.line(data, x="date", y="cases", color="country")
fig.show()