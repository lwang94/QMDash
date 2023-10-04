from dash import Dash, html, dcc, Output, Input, State, callback
import numpy as np
import util as u
from potentials import Inf_Square_Well


def callbacks_widgets(app):

    @callback(
        Output("components_table", "data"),
        Input("add_eigenstate_button", "n_clicks"),
        State("components_table", "data"),
        State("components_table", "columns")
    )
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c["id"]: "" for c in columns})
        return rows


    @callback(
        Output("invalid_custom_function", "displayed"),
        Input("custom_function_submit", "n_clicks"),
        State("custom_function_input", "value"),
        State("bound_input", "value"),
        prevent_initial_call=True
    )
    def invalid_custom_function_error(n_clicks, expression, bound): 
        if expression is None:
            return True

        x = np.linspace(0, u.hartree_length(1), 200)
        a = u.hartree_length(bound)
        expression = expression.replace("bound", f"{a}")

        inf_square_well = Inf_Square_Well(a, x)
        try:
            approx_func_constants = inf_square_well.constants_to_approx_custom_func(expression)
            return False
        except:
            return True
        
    
    @callback(
        Output("components_table", "data", allow_duplicate=True),
        Input("custom_function_submit", "n_clicks"),
        State("custom_function_input", "value"),
        State("bound_input", "value"),
        prevent_initial_call=True
    )
    def fill_datatable_with_approx_func(n_clicks, expression, bound):
        x = np.linspace(0, u.hartree_length(1), 200)
        a = u.hartree_length(bound)
        expression = expression.replace("bound", f"{a}")

        inf_square_well = Inf_Square_Well(a, x)
        approx_func_constants = inf_square_well.constants_to_approx_custom_func(expression)
        norm = np.sum([
            approx_func_constants[eigenstate] ** 2 for eigenstate in approx_func_constants
        ])
        norm = 1 / np.sqrt(norm)
        return [
            {
                "components_table_c": norm * approx_func_constants[eigenstate],
                "components_table_eigenstate": eigenstate
            } for eigenstate in approx_func_constants
        ]