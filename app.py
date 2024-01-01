from dash import Dash, html, dcc, Output, Input, callback, dash_table
from dash.dash_table.Format import Format, Scheme, Trim
from dash_extensions.enrich import DashProxy, BlockingCallbackTransform
import dash_bootstrap_components as dbc
import numpy as np
from callbacks_graph_infinite_square_well import callbacks_graph
from callbacks_widgets_infinite_square_well import callbacks_widgets

import callbacks_graph_free_particle as cgfp
from layout_infinite_square_well import isw_layout

app = DashProxy(transforms=[BlockingCallbackTransform(timeout=5)])

app.layout = html.Div([
    # isw_layout(),
    html.Div([
            html.H1(
                children="Free Particle",
                style={"textAlign": "center"},
                className="one row"
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            dcc.Graph(id="momentum_position_graph"),
                            html.Pre("LOCALIZATION", style={"font-size": "18px"}),
                            dcc.Slider(
                                0.03,
                                0.78,
                                0.05,
                                value=0.43,
                                marks=None,
                                id="localization_slider"
                            )
                        ],
                        style={"margin-left": "8%"},
                        className="five columns"
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(id="probability_graph"),
                            html.Pre("NUM PARTICLES", style={"font-size": "18px", "padding-top": "2%"}),
                            dcc.Input(
                                id="n_particles_input",
                                type="number",
                                placeholder="num particles",
                                value=10,
                                style={"width": "75%"}
                            )
                        ],
                        className="five columns"
                    )
                ],
                className="one row"
            )
        ])
])

cgfp.callbacks_graph(app)
# callbacks_graph(app)
# callbacks_widgets(app)

if __name__ == '__main__':
    app.run(debug=True)