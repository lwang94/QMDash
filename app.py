from dash import Dash, html, dcc, Output, Input, callback, dash_table
from dash.dash_table.Format import Format, Scheme, Trim
from dash_extensions.enrich import DashProxy, BlockingCallbackTransform
import dash_bootstrap_components as dbc
import numpy as np
from callbacks_graph_infinite_square_well import callbacks_graph
from callbacks_widgets_infinite_square_well import callbacks_widgets
from layout_infinite_square_well import isw_layout

app = DashProxy(transforms=[BlockingCallbackTransform(timeout=5)])

app.layout = html.Div([
    isw_layout()
])

callbacks_graph(app)
callbacks_widgets(app)

if __name__ == '__main__':
    app.run(debug=True)