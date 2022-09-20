import dash
import dash_dangerously_set_inner_html
from dash import Dash, dcc, html
from pathlib import Path
from html import unescape

app = Dash(__name__, use_pages=True, assets_url_path="/assets")

here = Path(__file__).parent
templates = (here / "./pages/templates").resolve()
header = (templates/"header.html").read_text()
footer = (templates/"footer.html").read_text()
navbar = (templates/"navbar.html").read_text()
navlink = (templates/"navlink.html").read_text()
link = ''
for page in dash.page_registry.values():
    link = link + navlink
    link = link.replace("href_value", page["relative_path"])
    link = link.replace("name_value", page["name"])


navbar = navbar.replace("links_value", link)
app.layout = html.Div([
    html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML(unescape(header))]),
    html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML(unescape(navbar))]),
    html.Div(dash.page_container, style={"min-height": 300}, className="grid-container-widescreen"),
    html.Div([dash_dangerously_set_inner_html.DangerouslySetInnerHTML(unescape(footer))]),
])

if __name__ == "__main__":
    app.run_server(debug=True)
