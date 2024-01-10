from dash import html, dcc

def l_fp():
    return html.Div([
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
                                0.01,
                                0.91,
                                0.02,
                                value=0.06,
                                marks=None,
                                id="localization_slider"
                            )
                        ],
                        style={"margin-left": "8%"},
                        className="five columns"
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(id="uncertainty_simulation_graph")
                        ],
                        className="four columns"
                    ),
                    html.Div(
                        children=[
                            html.Pre("NUM PARTICLES", style={"font-size": "18px", "padding-top": "2%"}),
                            dcc.Input(
                                id="n_free_particles_input",
                                type="number",
                                placeholder="num particles",
                                value=10,
                                style={"width": "150%"}
                            )                           
                        ],
                        className='one columns'
                    )
                ],
                className="one row"
            )
        ])