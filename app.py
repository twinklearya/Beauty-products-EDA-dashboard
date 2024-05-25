import base64
import io
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

# Load initial dataset
df = pd.read_csv('beauty_products.csv')

# Initialize Dash app
app = Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.Div([
        html.H1("Beauty Products EDA Dashboard"),
    ], style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='feature-dropdown',
                options=[{'label': col, 'value': col} for col in df.columns if col not in ['product_name', 'brand']],
                value='rating'
            ),
        ], style={'width': '70%', 'display': 'inline-block'}),
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Button('Upload CSV File'),
                multiple=False
            ),
            html.Div(id='output-data-upload'),
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'right'}),
    ], style={'padding': '10px'}),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='histogram'),
    dcc.Graph(id='box-plot')
])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        else:
            return html.Div(['Unsupported file format. Please upload a CSV file.'])
    except Exception as e:
        return html.Div(['There was an error processing this file.'])
    return df

# Callback to update data based on file upload
@app.callback(
    Output('output-data-upload', 'children'),
    Output('feature-dropdown', 'options'),
    Output('feature-dropdown', 'value'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is not None:
        global df
        df = parse_contents(contents, filename)
        options = [{'label': col, 'value': col} for col in df.columns if col not in ['product_name', 'brand']]
        return html.Div([html.H5(filename)]), options, options[0]['value'] if options else None
    return html.Div(), [{'label': col, 'value': col} for col in df.columns if col not in ['product_name', 'brand']], 'rating'

# Callbacks for interactivity
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_scatter(selected_feature):
    return px.scatter(df, x='price', y=selected_feature, color='category', hover_data=['product_name', 'brand'])

@app.callback(
    Output('histogram', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_histogram(selected_feature):
    return px.histogram(df, x=selected_feature, color='category', nbins=50)

@app.callback(
    Output('box-plot', 'figure'),
    Input('feature-dropdown', 'value')
)
def update_boxplot(selected_feature):
    return px.box(df, x='category', y=selected_feature)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
