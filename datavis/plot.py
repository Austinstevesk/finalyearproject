import plotly
import plotly.graph_objs as G

x = ['Alex', 'John', 'jacob', 'Steve']
y1 = [60, 55, 75, 95]
y2 = [80, 46, 87, 90]

trace = G.Bar(x=x, y=y1, name="Old sem")
trace1 = G.Bar(x=x, y=y2, name="New sem")

layout = G.Layout(title="Scatter plot", xaxis = dict(title="names"), yaxis = dict(title="marks"))
fig = G.Figure([trace, trace1], layout)
plotly.plot(fig, kind="bar")