
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.NavItem(dbc.NavLink("Service Request", href="/requests")),
        dbc.DropdownMenu(
            children=[
                # dbc.DropdownMenuItem("More", header=True),
                dbc.DropdownMenuItem("Dataset Prep", href="/dataset"),
                dbc.DropdownMenuItem("Log out", href="/logout"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Demo App",
    brand_href="#",
    color="primary",
    dark=True,
)
