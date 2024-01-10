from dash import Output, Input, callback
from potentials import Inf_Square_Well
import util as u
import numpy as np
import plotly.graph_objects as go


def callbacks_graph(app):
    # callback for plotting animation

    @callback(
        Output("probability_graph", "figure"),
        Input("bound_input", "value"),
        Input("mass_input", "value"),
        Input("end_time_input", "value"),
        Input("n_particles_input", "value"),
        Input("components_table", "data"),
        blocking=True
    )
    def animate_probabilities(bound, mass, end_time, n_particles, components):
        # components check
        components = [
            component for component in components 
            if component["components_table_c"] != "" 
            and component["components_table_eigenstate"] != ""
        ]
        c_sum = 0
        for component in components:
            if component["components_table_eigenstate"] % 1 != 0:
                return go.Figure(go.Scatter(
                    x=[0],
                    y=[0],
                    mode="markers+text",
                    text=["Eigenstates can only be integer values"],
                    textposition="top center"
                ))
            c_sum += component["components_table_c_squared"]
            
        if c_sum > 1.00000001 or c_sum < 0.9999999:
            return go.Figure(go.Scatter(
                x=[0],
                y=[0],
                mode="markers+text",
                text=["Make sure the square of all constants add to 1"],
                textposition="top center" 
            ))


        # create potential
        x = np.linspace(0, u.hartree_length(1), 200)
        a = u.hartree_length(bound)

        inf_square_well = Inf_Square_Well(a, x)

        # define t and m
        t = np.apply_along_axis(u.hartree_time, 0, np.linspace(0, end_time, 50))
        m = u.hartree_mass(mass)

        # create eigenstate dictionary
        eigenstate_dict = {}
        for comp in components:
            eigenstate_dict[comp["components_table_eigenstate"]] = u.eigenstate_dictionary(
                inf_square_well,
                comp["components_table_eigenstate"],
                comp["components_table_c"],
                m,
                t
            )
        
        # create time dependent wavefunctions and probability density functions
        probability_densities = []
        for time_index in range(len(t)):
            wf = np.zeros(len(x), dtype=np.complex128)
            for eigenstate in eigenstate_dict:
                wf += (
                    eigenstate_dict[eigenstate]["c"]
                    * eigenstate_dict[eigenstate]["y"]
                    * eigenstate_dict[eigenstate]["t"][time_index]
                )
            probability_densities.append(np.conjugate(wf) * wf)
        
        # simulate probability of measuring particle at (x, t)
        positions = [(x[i + 1] + x[i]) / 2 for i in range(len(x) - 1)]
        choices = []
        for pdf in probability_densities:
            probabilities = [
                u.find_area(x[i], x[i + 1], pdf[i], pdf[i + 1]) 
                for i in range(len(x) - 1) 
            ]
            choice = np.random.choice(
                positions, 
                size=n_particles, 
                p=probabilities/np.sum(probabilities)
            )
            choices.append(choice)

        # define layout
        layout = {
            "xaxis": dict(range=[x.min(), x.max()], autorange=False),
            "yaxis": dict(
                range=[
                    -probability_densities[0].real.max(),
                    probability_densities[0].real.max()
                ],
                autorange=False
            ),
            "showlegend": False,
            "margin": {
                "l": 10,
                "r": 10,
                "b": 10,
                "t": 10
            },
            "updatemenus": [
                dict(
                    type="buttons",
                    x=0.08,
                    y=1.15,
                    buttons=[dict(
                        label="Play",
                        method="animate",
                        args=[None]
                    )]
                )
            ]
        }

        # define frames
        frames = []
        for i in range(len(t)):
            data = [
                {
                    "x": x,
                    "y": probability_densities[i].real,
                    "mode": "markers",
                    "marker": dict(opacity=0.15)
                },
                {
                    "x": [a, a],
                    "y": [0, probability_densities[0].real.max()],
                    "mode": "lines",
                    "opacity": 0.5,
                    "marker": dict(color="red")

                },
                {
                    "x": [x[1], x[1]],
                    "y": [0, probability_densities[0].real.max()],
                    "mode": "lines",
                    "opacity": 0.5,
                    "marker": dict(color="red")
                }
            ]
            for j in range(n_particles):
                data.append({
                    "x": [choices[i][j]],
                    "y": [j * probability_densities[0].real.max() / 50],
                    "mode": "markers",
                    "marker": dict(size=12)
                })
            frames.append({
                "data": data,
                "name": str(t[i])
            })
        
        # define slider
        sliders_dict = {
            "active": 0,
            "yanchor": "top",
            "xanchor": "left",
            "currentvalue": {
                "visible": True,
                "xanchor": "right"
            },
            "transition": {"duration": 0.1, "easing": "cubic-in-out"},
            "pad": {"t": 20},
            "len": 0.9,
            "x": 0.05,
            "y": 0,
            "steps": [{
                "args": [
                    [t[i]],
                    {
                        "frame": {"duration": 0.1, "redraw": False},
                        "mode": "immediate",
                        "transition": {"duration": 0.1}
                    }
                ],
                "method": "animate"
            } for i in range(len(t))]
        }
        layout["sliders"] = [sliders_dict]

        # make figure
        fig_dict = {
            "data": data,
            "layout": layout,
            "frames": frames
        }
        return go.Figure(fig_dict)