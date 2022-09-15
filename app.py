import dash
from dash import Dash, dcc, html

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.Nav(
        html.Div(
            html.Ul([
                html.Li(dcc.Link(
                    f"{page['name']}", href=page["relative_path"], className="nav-link active"
                ), className="nav-item"
            )
            for page in dash.page_registry.values()
            ], className="navbar-nav me-auto mb-2 mb-lg-0"), className="container-fluid"
        ), className="navbar navbar-expand-lg bg-light"
    ),
	dash.page_container
])


if __name__ == '__main__':
    app.run_server(debug=True)
