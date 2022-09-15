from dash import Dash, Input, Output, callback, dcc, html, register_page

register_page(__name__)

layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "x: ",
        x_input := dcc.Input(type='number')
    ]),
    html.Div([
        "y: ",
        y_input := dcc.Input(type='number')
    ]),
    html.Br(),
    output := html.Div(),

])

@callback(
    Output(output, component_property='children'),
    Input(x_input, component_property='value'),
    Input(y_input, component_property='value')
)
def update_output_div(x_input, y_input):
    if x_input and y_input:
        return f'x * y = {x_input * y_input}'
    return html.H6("Both inputs are required.", style={"color":"red"})
