from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('formated_data.csv')
df = df.sort_values(by='date')

# Initialize the Dash app
app = Dash(__name__)


app.layout = html.Div(children=[
    html.Div(
            html.H1("Sales Data Visualizer", style={'border': '3.5px solid #ddd', 'padding': '10px',
                                                                 'border-radius': '3px', 'display': 'inline-block'}),
            style={'text-align': 'center'},
            id='header'
    ),
    dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'All Regions', 'value': 'All'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},

            ],
            value='All',
            labelStyle={'display': 'inline-block', 'margin-right': '20px', 'border': '3.5px solid #ddd','padding': '10px', 'border-radius': '5px'},  # Display options horizontally with spacing
            style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'center'},  # Center the group and add a box around it
        ),
    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x='date', y='sales').update_layout(title_text='Sales Over Time', title_x=0.5)
    )
])


@app.callback(Output('line-chart', 'figure'), [Input('region-radio', 'value')])
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', title='Sales Over Time')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
