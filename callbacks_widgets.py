from dash import Dash, html, dcc, Output, Input, State, callback


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