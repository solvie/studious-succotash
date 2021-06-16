import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

x = ['A', 'B', 'C', 'D', 'E']
y = ['W', 'X', 'Y', 'Z']

#       x0    x1    x2    x3    x4
z = [[0.00, 0.00, 0.75, 0.75, 0.00],  # y0
     [0.00, 0.00, 0.75, 0.75, 0.00],  # y1
     [0.75, 0.75, 0.75, 0.75, 0.75],  # y2
     [0.00, 0.00, 0.00, 0.75, 0.00]]  # y3

annotations = []
for n, row in enumerate(z):
    for m, val in enumerate(row):
        annotations.append(dict(text=str(z[n][m]), x=x[m], y=y[n],
                            xref='x1', yref='y1', showarrow=False))

colorscale = [[0, '#3D9970'], [1, '#001f3f']]  # custom colorscale
trace = go.Heatmap(
    x=x, 
    y=y, 
    z=z, 
    colorscale=colorscale, 
    showscale=False,
    hovertemplate =
    '<i>Price</i>: %{y}'+
    '<br><b>Foo</b>: %{x}<br>'+
    '<b>Bar: %{z}</b>'+
    '<extra></extra>'
)

fig = go.Figure(
    data=trace
)
fig['layout'].update(
    title="Annotated Heatmap",
    xaxis=dict(title='something'),
    yaxis=dict(title='another thing'),
    annotations=annotations
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Medals included:"),
    dcc.Checklist(
        id='annotations',
        options=[{'label': 'annotations', 'value': 'true'}],
        value=['bar']
    ),
    dcc.Graph(
        id="graph"
    )
])

@app.callback(
    Output("graph", "figure"), 
    [Input("annotations", "value")])
def filter_heatmap(annot_value):
    print('cols')
    print(annot_value)
    fig = go.Figure(
        data=trace
    )
    if len(annot_value) == 2:
        fig['layout'].update(
            title="Annotated Heatmap",
            xaxis=dict(title='something'),
            yaxis=dict(title='another thing'),
            annotations=annotations
        )
    else:
        fig['layout'].update(
            title="Annotated Heatmap",
            xaxis=dict(title='something'),
            yaxis=dict(title='another thing'),
        )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)