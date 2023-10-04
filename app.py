from dash import Dash, html, dcc, Output, Input, callback, dash_table
import dash_bootstrap_components as dbc
import numpy as np
from callbacks_graph import callbacks_graph
from callbacks_widgets import callbacks_widgets

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        children="Infinite Square Well",
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
                    html.Pre("MASS", style={"font-size": "18px", "padding-top": "2%"}),
                    dcc.Input(
                        id="mass_input",
                        type="number",
                        placeholder="mass",
                        value=1,
                        min=0.5,
                        step=0.5,
                        style={"width": "75%"}
                    ),
                    html.Pre("END TIME", style={"font-size": "18px", "padding-top": "2%"}),
                    dcc.Input(
                        id="end_time_input",
                        type="number",
                        placeholder="end time",
                        value=100,
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
            ),
            html.Div(
                children=[
                    html.Pre("EIGENSTATES", style={"font-size": "18px", "padding-top": "10%"}),
                    dash_table.DataTable(
                        id="components_table",
                        style_table={"width": "100%", "padding-top": "2%"},
                        style_cell={"textAlign": "center"},
                        style_cell_conditional=[
                            {
                                "if": {"column_id": "components_table_c"},
                                "width": "50%"
                            },
                            {
                                "if": {"column_id": "components_table_eigenstate"},
                                "width": "50%"
                            }
                        ],
                        columns=[
                            {
                                "name": "C",
                                "id": "components_table_c",
                                "type": "numeric"
                            },
                            {
                                "name": "EIGENSTATE",
                                "id": "components_table_eigenstate",
                                "type": "numeric"
                            }
                        ],
                        data=[
                            {
                                "components_table_c": 1/np.sqrt(2),
                                "components_table_eigenstate": 1
                            },
                            {
                                "components_table_c": 1/np.sqrt(2),
                                "components_table_eigenstate": 2
                            }
                        ],
                        editable=True,
                        row_deletable=True
                    ),
                    html.Button(
                        "Add Eigenstate",
                        id="add_eigenstate_button"
                    ),
                    dcc.Input(
                        id="custom_function_input",
                        type="text",
                        placeholder="custom function",
                        style={"margin-top": "20%"}
                    ),
                    dbc.Tooltip(
                        [
                            html.P("ALLOWED VARIABLES: "),
                            html.P("x (the variable the function acts on)"),
                            html.P("bound (a constant representing the bound of the infinite square well)"),
                            html.P("NOTE: The function will be normalized such that it's integral is 1")
                        ],
                        target="custom_function_input",
                        placement="left",
                        style={"font-size": "10px"}
                    ),
                    html.Button(
                        "Submit",
                        id="custom_function_submit"
                    )
                ],
                className='two columns'
            )
        ],
        className="one row"
    )
])

callbacks_graph(app)
callbacks_widgets(app)

if __name__ == '__main__':
    app.run(debug=True)