import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv('formated_data.csv')
df = df.sort_values(by='date')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1("Sales Data Visualizer"),

    dcc.Graph(
        id='line-chart',
        figure=px.line(df, x='date', y='sales', color='region', title='Sales Over Time')
    )
])


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
