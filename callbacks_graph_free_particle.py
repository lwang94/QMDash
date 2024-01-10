from dash import Output, Input, callback
from potentials import FreeParticle
import util as u
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def callbacks_graph(app):
    # callback for plotting animation
    @callback(
        Output("uncertainty_simulation_graph", "figure"),
        Input("momentum_position_graph", "figure"),
        Input("n_free_particles_input", "value")
    )
    def simulate_uncertainty(momentum_position, num_particles):
        x = momentum_position["data"][0]["x"]
        p = momentum_position["data"][1]["x"]
        prob_x = momentum_position["data"][0]["y"]
        prob_p = momentum_position["data"][1]["y"]
        
        choices_x = np.random.choice(x, size=num_particles, p=prob_x/np.sum(prob_x))
        choices_p = np.random.choice(p, size=num_particles, p=prob_p/np.sum(prob_p))

        t = 21
        disp = np.zeros(num_particles)
        height = 0 * choices_x
        heights = [0 * choices_x]
        for i in range(t):
            if i > (t / 4) and i < (3 * t / 4):
                disp = -choices_p / 21
            else:
                disp = choices_p / 21
            height += disp
            heights.append(height.copy())
        layout = {
            "xaxis": dict(range=[min(x), max(x)], autorange=False),
            "yaxis": dict(range=[-max(choices_p), max(choices_p)], autorange=False),
            "title": "Free Particle",
            "updatemenus": [dict(
                type="buttons",
                buttons=[dict(
                    label="Play",
                    method="animate",
                    args=[None]
                )]
            )]
        }
        frames = []
        for i in range(t):
            data = [{
                "x": choices_x,
                "y": heights[i],
                "mode": "markers"
            }]
            frames.append({
                "data": data,
                "name": str(i)
            })
        sliders_dict = {
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Time:",
                "visible": True,
                "xanchor": "right"
            },
            "transition": {"duration": 0},
            "pad": {"b": 10, "t": 50},
            "len": 0.9,
            "x": 0.1,
            "y": 0,
            "steps": [{
                "args": [
                    [i],
                    {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate",
                        "transition": {"duration": 0}
                    }
                ],
                "method": "animate"  
            } for i in range(t)]
        }
        layout["sliders"] = [sliders_dict]
        fig_dict = {
            "data": data,
            "layout": layout,
            "frames": frames
        }

        fig = go.Figure(fig_dict)
        return fig



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
        p = p[400:600]
        wf_p = np.array([momentum_dict[p[i]] for i in range(len(p))])

        prob_x = np.conjugate(wf_x) * wf_x
        prob_p = np.conjugate(wf_p) * wf_p

        fig = make_subplots(
            rows=2, 
            cols=1,
            subplot_titles=("Position","Momentum")
        )
        fig.add_trace(row=1, col=1, trace=go.Scatter(x=x, y=prob_x.real))
        fig.add_trace(row=2, col=1, trace=go.Scatter(x=p, y=prob_p.real))

        fig.update_layout(
            margin=dict(l=10, r=10, t=20, b=10),
            showlegend=False
        )

        fig.update_yaxes(showticklabels=False) 
        return go.Figure(fig)