from dash import html
from dash_extensions.enrich import DashProxy, BlockingCallbackTransform

import callbacks_graph_infinite_square_well as cg_isw
import callbacks_widgets_infinite_square_well as cw_isw
import callbacks_graph_free_particle as cg_fp
from layout_infinite_square_well import l_isw
from layout_free_particle import l_fp

app = DashProxy(transforms=[BlockingCallbackTransform(timeout=5)])

app.layout = html.Div([
    l_isw(),
    html.Hr(),
    l_fp()
])

cg_fp.callbacks_graph(app)
cg_isw.callbacks_graph(app)
cw_isw.callbacks_widgets(app)

if __name__ == '__main__':
    app.run(debug=True)