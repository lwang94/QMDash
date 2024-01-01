from dash import Dash, html, dcc, Output, Input, callback
from potentials import FreeParticle
import util as u
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def callbacks_graph(app):
    # callback for plotting animation

    @callback(
        Output("momentum_position_graph", "figure"),
        Input("localization_slider", "value")
    )
    def momentum_space(localization):
        a = 2 * np.pi
        x = u.hartree_length(np.linspace(-a, a, 1000))

        fp = FreeParticle(x)
        x, wf_x, p, wf_p = fp.approximate_localization(u.hartree_length(localization * a))
        
        momentum_dict = {p[i]: wf_p[i] for i in range(len(p))}

        p = np.sort(p)
        p = p[250:750]
        wf_p = np.array([momentum_dict[p[i]] for i in range(len(p))])

        fig = make_subplots(rows=2, cols=1)
        fig.add_trace(row=1, col=1, trace=go.Scatter(x=x, y=wf_x.real))
        fig.add_trace(row=2, col=1, trace=go.Scatter(x=p, y=wf_p.real))
        return go.Figure(fig)