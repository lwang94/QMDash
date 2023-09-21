from dash import Dash, html, dcc, Output, Input, callback
from ..potentials import Inf_Square_Well


def callbacks_graph(app):
    # callback for plotting animation

    @callback(
        Output("probability_graph", "fig"),
        Input("bound_input", "value"),
        Input("mass_input", "value"),
        Input("end_time_input", "value"),
        Input("n_particles_input", "value"),
        Input("components_table", "data")

    )
    def animate_probabilities(bound, mass, end_time, n_particles, components):
        