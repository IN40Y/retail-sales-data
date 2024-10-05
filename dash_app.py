import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load Data
df = pd.read_csv('retail_sales_data.csv')

# Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Retail Sales Dashboard"),
    
    dcc.Graph(id='sales_trend'),
    dcc.Graph(id='sales_by_category'),
    dcc.Graph(id='region_performance')
])

# Sales Trend Graph
@app.callback(
    dash.dependencies.Output('sales_trend', 'figure'),
    dash.dependencies.Input('sales_trend', 'id')
)
def update_sales_trend(_):
    fig = px.line(df, x='date', y='total_sales', title='Sales Trend Over Time')
    return fig

# Sales by Category Graph
@app.callback(
    dash.dependencies.Output('sales_by_category', 'figure'),
    dash.dependencies.Input('sales_by_category', 'id')
)
def update_sales_by_category(_):
    category_sales = df.groupby('category').agg({'total_sales': 'sum'}).reset_index()
    fig = px.bar(category_sales, x='category', y='total_sales', title='Sales by Category')
    return fig

# Regional Performance Graph
@app.callback(
    dash.dependencies.Output('region_performance', 'figure'),
    dash.dependencies.Input('region_performance', 'id')
)
def update_region_performance(_):
    region_sales = df.groupby('region').agg({'total_sales': 'sum'}).reset_index()
    fig = px.pie(region_sales, names='region', values='total_sales', title='Regional Performance')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
