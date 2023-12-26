from dash import Dash, html, dcc, Output, Input, callback, dash_table
from dash.dash_table.Format import Format, Scheme, Trim
from dash_extensions.enrich import DashProxy, BlockingCallbackTransform
import dash_bootstrap_components as dbc
import numpy as np
from callbacks_graph import callbacks_graph
from callbacks_widgets import callbacks_widgets
from layout_infinite_square_well import isw_layout

app = DashProxy(transforms=[BlockingCallbackTransform(timeout=5)])

app.layout = html.Div([
    # isw_layout()
    html.Div([
            html.H1(
                children="Free Particle",
                style={"textAlign": "center"},
                className="one row"
            ),
            html.Div(
                children=[
                    dcc.ConfirmDialog(
                        id="invalid_custom_function",
                        message="Invalid Custom Function"
                    ),
                    html.Div(
                        children=[
                            html.Pre("BOUND", style={"font-size": "18px"}),
                            dcc.Input(
                                id="bound_input",
                                type="number",
                                placeholder="bound",
                                value=0.5,
                                min=0.05,
                                max=0.95,
                                step=0.05,
                                style={"width": "75%"}
                            ),
                            html.Pre("NUM PARTICLES", style={"font-size": "18px", "padding-top": "2%"}),
                            dcc.Input(
                                id="n_particles_input",
                                type="number",
                                placeholder="num particles",
                                value=10,
                                style={"width": "75%"}
                            )
                        ],
                        style={"margin-left": "8%"},
                        className="one half columns"
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="probability_graph"
                            )
                        ],
                        className="seven columns"
                    )
                ],
                className="one row"
            )
        ])
])

# callbacks_graph(app)
# callbacks_widgets(app)

if __name__ == '__main__':
    app.run(debug=True)