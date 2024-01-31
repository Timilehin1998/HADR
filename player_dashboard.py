import io
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import dash_mantine_components as dmc
from datetime import datetime
import dash
import matplotlib.colors as mcolors
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import os
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload 
import os
from collections import namedtuple
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import urllib.request, json
from urllib.request import urlopen 
import requests
import tempfile
from google.oauth2 import service_account




CLIENT_SECRET_FILE_URL = 'https://drive.google.com/file/d/1naCRnK6PPKxatPPc2nW0RPY69m-bKnSy/view?usp=drive_link'
CLIENT_SECRET_FILE_URL = 'https://drive.google.com/uc?id=' + CLIENT_SECRET_FILE_URL.split('/')[-2]

response = requests.get(CLIENT_SECRET_FILE_URL)

# Check if request was successful
if response.status_code == 200:
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the JSON content to the temporary file
        temp_file.write(response.text)
        CLIENT_SECRET_FILE = temp_file.name

    

API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

def Create_Service(client_secret_file, api_name, api_version, *scopes, prefix=''):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]

    # Load service account credentials from the JSON file
    credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=SCOPES)

    try:
        # Build the service using the service account credentials
        service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
        print(API_SERVICE_NAME, API_VERSION, 'service created successfully')
        return service
    except Exception as e:
        print(e)
        print(f'Failed to create service instance for {API_SERVICE_NAME}')
        return None











# Initialize the Dash app
#app = dash.Dash(__name__)


existing_data_url = 'https://drive.google.com/file/d/1T6iOOp5kD-hMVBmANRMGFCo3Gp2uTxqc/view?usp=sharing'
existing_data_url='https://drive.google.com/uc?id=' + existing_data_url.split('/')[-2]
existing_data = pd.read_csv(existing_data_url)


asset_df_url = 'https://drive.google.com/file/d/1riT7LUDNIsQP6zS1l4j96-mpGTK_yK2N/view?usp=drive_link'
asset_df_url='https://drive.google.com/uc?id=' + asset_df_url.split('/')[-2]
asset_df = pd.read_csv(asset_df_url)



my_list = []
#Budget = 600000000.0
def convert_to_millions(units):
    return '$' + str(round(units/1000000)) + ' Million'

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
# Define colors and styles
initial_options = [
                    {'label': '2', 'value': 2},
                    {'label': '4', 'value': 4},
                    {'label': '6', 'value': 6}
                ]
#existing_data = pd.read_csv('C:\\Users\\toderinde3\\Documents\\HADR_Project\\Year7\\DOE\\Baseline.csv')

current_directory = os.getcwd()

# Define the path to the background image within the local folder
background_image_path = "Python_Dashboard\\Pictures\\UH60rspic.png"  # Adjust the path as needed


# Combine the current directory with the image path
background_image_url = "C:/Users/toderinde3/OneDrive - Georgia Institute of Technology/HADR_Project/Year7/Python_Dashboard/Pictures/UH60rspic.png"
print(f"Full Path to Image: {background_image_url}")
def Header(name, app):
    title = html.H2(name, style={"margin-top": 5})
    logo = html.Img(
        src=app.get_asset_url("dash-logo.png"), style={"float": "right", "height": 50}
    )

    return dbc.Row([dbc.Col(title, md=9), dbc.Col(logo, md=3)])

LEFT_COLUMN = dbc.Jumbotron(
    [
        html.H4(children="Alternative asset combinations", className="display-5"),
        html.Hr(className="my-2"),
        html.H4(children="Acquisition", style={"marginTop": 30}, className="display-7"),
        #html.Hr(className="my-2"),
        

        html.Label("Select aerial cargo assets", style={"marginTop": 20}, className="lead"),
        dcc.Dropdown(
            id="cargo-acq-drop", clearable=False, style={"marginBottom": 10, "font-size": 12},
            options=[
            {'label': 'UH-60', 'value': 'UH-60'},
            {'label': 'V-280', 'value': 'V-280'},
            {'label': 'V-22', 'value': 'V-22'},
            {'label': 'MRH-90', 'value': 'MRH-90'},
            
        ],
        value=None,
        #label= "",
        ),

        html.Label("Number of assets", style={"marginTop": 20}, className="lead"),
    
        # Create radio buttons with options
       
        dcc.RadioItems(
            id='radio-button1',
            options=initial_options,
            value= 2,
            labelStyle={'display': 'inline-block', 'margin-right': '30px'}  # inline display with spacing
              
        ),


        html.Label("Select maritime cargo assets", style={"marginTop": 20}, className="lead"),
        dcc.Dropdown(
            id="maritime-acq-drop", clearable=False, style={"marginBottom": 10, "font-size": 12},
            options=[
            {'label': 'UH-60', 'value': 'UH-60'},
            {'label': 'V-280', 'value': 'V-280'},
            {'label': 'V-22', 'value': 'V-22'},
            {'label': 'MRH-90', 'value': 'MRH-90'},
            
        ],
        value=None,
        #label= "",
        ),


        html.Label("Number of assets", style={"marginTop": 20}, className="lead"),
    
        # Create radio buttons with options
       
        dcc.RadioItems(
            id='radio-button2',
            options=initial_options,
            value= 2,
           labelStyle={'display': 'inline-block', 'margin-right': '30px'}  # inline display with spacing
              
        ),


            

        
    ]
)




RIGHT_COLUMN = dbc.Jumbotron(
    [
    html.H4(children="Alternative asset combinations", className="display-5"),
    html.Hr(className="my-2"),
    html.H4(children="S & T Investment", style={"marginTop": 30}, className="display-7"),
    #html.Hr(className="my-2"),
    html.Label("Select aerial cargo assets", style={"marginTop": 10}, className="lead"),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(
                            id="cargo-st-drop", clearable=False, style={"marginBottom": 10, "font-size": 12},
                            options=[
            {'label': 'UH-60', 'value': 'UH-60'},
            {'label': 'V-280', 'value': 'V-280'},
            {'label': 'V-22', 'value': 'V-22'},
            {'label': 'MRH-90', 'value': 'MRH-90'},
            
                        ],
                        value='',
                        #label= "",
                        ),
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id="cargo-st-type-drop", clearable=False, style={"marginBottom": 10, "font-size": 12},
                            options=[
                                {"label": "Payload", "value": "A"},
                                {"label": "Range", "value": "B"},
                                {"label": "Speed", "value": "C"},
                                {"label": "Range and Payload", "value": "D"},
                                {"label": "Range and Speed", "value": "E"},
                                {"label": "Speed and Payload", "value": "F"},
                            ],
                            value="",
                        )
                    ),
                ],
                className="mt-4",
            ),

            html.Label("Number of assets", style={"marginTop": 10}, className="lead"),
    
        # Create radio buttons with options
       
            dcc.RadioItems(
                id='radio-button3',
                options=initial_options,
                value= 2,
                labelStyle={'display': 'inline-block', 'margin-right': '30px'}  # inline display with spacing
                
            ),

    

    html.Label("Select maritime cargo assets", style={"marginTop": 10}, className="lead"),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Dropdown(
                            id="maritime-st-drop", clearable=False, style={"marginBottom": 4, "font-size": 12},
                            options=[
                            {'label': 'UH-60', 'value': 'UH-60'},
                            {'label': 'V-280', 'value': 'V-280'},
                            {'label': 'V-22', 'value': 'V-22'},
                            {'label': 'MRH-90', 'value': 'MRH-90'},
                            
                        ],
                        value='',
                        #label= "",
                        ),
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id="maritime-st-type-drop", clearable=False, style={"marginBottom": 4, "font-size": 12},
                            options=[
                                {"label": "Payload", "value": "A"},
                                {"label": "Range", "value": "B"},
                                {"label": "Speed", "value": "C"},
                                {"label": "Range and Payload", "value": "D"},
                                {"label": "Range and Speed", "value": "E"},
                                {"label": "Speed and Payload", "value": "F"},
                            ],
                            value="",
                        )
                    ),
                ],
                className="mt-4",
            ),  
            html.Label("Number of assets", style={"marginTop": 10}, className="lead"),
    
            # Create radio buttons with options
        
            dcc.RadioItems(
                id='radio-button4',
                options=initial_options,
                value= 2,
                labelStyle={'display': 'inline-block', 'margin-right': '30px'}  # inline display with spacing
                
            ), 
    ]
)



base = [
    dbc.Card(
        [
            html.H2("Assets Specifications", className="card-title"),
            html.P(id='case-value1', className=""),
            html.Div(id='last-selected-dropdown', style={'display': 'none'}),
            
        ],
        body=True,
        color="light",
    ),
]

footer = [
    dbc.Card(
        [
            html.H2("Available Funds", className="card-title"),
            html.P(id='case-value2', className=""),  
            html.Div([dcc.Input(id='output-number', type='number', value=0)], style={'display': 'none'}),
        ],
        body=True,
        color="light",
    ),
]

NAVBAR = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand("Humanitarian Aid and Disaster Relief (HADR) Operations", className="ml-2")
                    ),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        )
    ],
    color="dark",
    dark=True,
    sticky="top",
)
BODY = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(LEFT_COLUMN, md=6, align="left"),
                dbc.Col(RIGHT_COLUMN, md=6, align="right"),

            ],
            style={"marginTop": 30},
        ),

        html.Hr(),
        dbc.Row([
            dbc.Col([dbc.Col(base) for card in base], style={'margin-top': '5px', 'font-size': '10px'}, md=8) ,
        
            dbc.Col([dbc.Col(footer) for card in footer], style={'margin-top': '5px', 'font-size': '10px'}) ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                html.Button("Populate Case", id='populate-button', n_clicks=0),
                md=4,
                style={'text-align': 'right'},align="right"
                
            ),
            dbc.Col(
                html.Button('Clear Selections', id='clear-button', n_clicks=0),
                md=4,
                style={'text-align': 'right'},align="right"
            ),
            html.Div(id='output-container'),

            dbc.Col(
                html.H2( id='simulation-output'),
                md=4,
                style={'text-align': 'right'},align="right"
            ),
        ]),

        dbc.Row([
            dbc.Col(
                dash_table.DataTable(id='data-table',
                                     selected_rows=[],
        style_table={'overflowX': 'auto'}),
                md=12,
                
            )
        ]),


    ],
    className="mt-12",
)




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = html.Div(children=[NAVBAR,BODY])

# Callback to handle disabling/enabling dropdowns based on selections
@app.callback(
    [Output('cargo-st-drop', 'disabled'),
     Output('cargo-st-type-drop', 'disabled'),
     Output('radio-button3', 'options')],
    [Input('cargo-acq-drop', 'value'),
     Input('radio-button3', 'options')]
)
def disable_dropdowns_3_to_4(selected_value_dropdown1, options):
    if selected_value_dropdown1:
        for option in options:
            option['disabled'] = True
        return True, True, options
    return False, False, options

# Callback to handle disabling/enabling dropdowns based on selections
@app.callback(
    [Output('cargo-acq-drop', 'disabled'),
     Output('radio-button1','options')],
    [Input('cargo-st-drop', 'value'),
     Input('cargo-st-type-drop','value'),
     Input('radio-button1','options')]
)
def disable_dropdowns_1(selected_value_dropdown1,selected_value_dropdown2, options):
    if selected_value_dropdown1 or selected_value_dropdown2:
        for option in options:
            option['disabled'] = True
        return True, options
    return False, options

@app.callback(
    [Output('maritime-st-drop', 'disabled'),
     Output('maritime-st-type-drop', 'disabled'),
     Output('radio-button4','options')],
    [Input('maritime-acq-drop', 'value'),
     Input('radio-button4','options')]
)
def disable_dropdowns_5_to_6(selected_value_dropdown1, options):
    if selected_value_dropdown1:
        for option in options:
            option['disabled'] = True
        return True, True, options
    return False, False, options

@app.callback(
    [Output('maritime-acq-drop', 'disabled'),
     Output('radio-button2', 'options')],
    [Input('maritime-st-drop', 'value'),
     Input('maritime-st-type-drop','value'),
     Input('radio-button2', 'options')]
)
def disable_dropdowns_2(selected_value_dropdown1,selected_value_dropdown2, options):
    if selected_value_dropdown1 or selected_value_dropdown2:
        for option in options:
            option['disabled'] = True
        return True, options
    return False, options



# Callback to clear selections and enable all dropdowns on button click
@app.callback(
    [Output('cargo-acq-drop', 'value'),
     Output('maritime-acq-drop', 'value'),
     Output('cargo-st-drop', 'value'),
     Output('cargo-st-type-drop', 'value'),
     Output('maritime-st-drop', 'value'),
     Output('maritime-st-type-drop', 'value'),
     Output('radio-button3', 'options', allow_duplicate=True),
     Output('radio-button1', 'options', allow_duplicate=True),
     Output('radio-button4', 'options', allow_duplicate=True),
     Output('radio-button2', 'options', allow_duplicate=True)],
    [Input('clear-button', 'n_clicks'),
     ],
     prevent_initial_call=True
)
def clear_selections(n_clicks):
    global my_list
    ctx = dash.callback_context
    if ctx.triggered_id == 'clear-button' and n_clicks is not None:
        my_list=[]
        #print("clear_trigger is",ctx.triggered_id)
        for option in initial_options:
            option['disabled'] = False
        return None,  None, None, None, None, None, initial_options.copy(), initial_options.copy(), initial_options.copy(), initial_options.copy()
    return dash.no_update

@app.callback(
    [Output('case-value1', 'children'),
     Output('last-selected-dropdown', 'children'),
     Output('case-value2', 'children'),
     Output('output-number', 'value')],
    [Input('cargo-acq-drop', 'value'),
     Input('maritime-acq-drop', 'value'),
     Input('cargo-st-drop', 'value'),
     Input('cargo-st-type-drop', 'value'),
     Input('maritime-st-drop', 'value'),
     Input('maritime-st-type-drop', 'value'),
     Input('radio-button1', 'value'),
     Input('radio-button2', 'value'),
     Input('radio-button3', 'value'),
     Input('radio-button4', 'value'),
     ],
     [State('last-selected-dropdown', 'children')]
    
)


def update_graph(cargo_acq, maritime_acq, cargo_st, cargo_st_type, maritime_st, maritime_st_type, radio1, radio2, radio3, radio4, last_selected_dropdown):
    Budget = 600000000.0
    # Get the ID of the component that triggered the callback
    
    triggered_id = dash.callback_context.triggered_id
    #last_saved_dropdown_value = triggered_id
    '''
    if (dash.callback_context.triggered_id == 'cargo-acq-drop' or dash.callback_context.triggered_id == 'maritime-acq-drop' or dash.callback_context.triggered_id == 'cargo-st-drop' or dash.callback_context.triggered_id == 'cargo-st-type-drop'or dash.callback_context.triggered_id == 'maritime-st-drop' or dash.callback_context.triggered_id == 'maritime-st-type-drop'):
        triggered_id = dash.callback_context.triggered_id
    if triggered_id is None:
        triggered_id = last_saved_dropdown_value
    '''
    

# Initialize the variable to hold the last non-None item
    last_selected_dropdown = None

# Iterate through the list


    # Determine the last selected dropdown based on the triggering component

    if triggered_id=='cargo-acq-drop' and cargo_acq:
        last_selected_dropdown = 'cargo-acq-drop'
    elif triggered_id=='maritime-acq-drop' and maritime_acq:
        last_selected_dropdown = 'maritime-acq-drop'
    elif triggered_id=='cargo-st-drop' and cargo_st_type:
        last_selected_dropdown = 'cargo-st-drop'
    elif triggered_id=='cargo-st-type-drop' and cargo_st:
        last_selected_dropdown = 'cargo-st-type-drop'
    elif triggered_id=='maritime-st-drop' and maritime_st_type:
        last_selected_dropdown = 'maritime-st-drop'
    elif triggered_id=='maritime-st-type-drop' and maritime_st:
        last_selected_dropdown = 'maritime-st-type-drop'
    else:
        last_selected_dropdown=None

    my_list.append(last_selected_dropdown)
    for item in my_list:
        if item is not None:
            last_selected_dropdown = item


    #print("trigger_id is",triggered_id)
    #print("my list is ",my_list)
    #print("last_selected_drop is",last_selected_dropdown)
    


    if last_selected_dropdown=='cargo-acq-drop':

        output_text = html.Div(style={
        'background-image': f'url("{background_image_url}")',
        'background-size': 'cover',
        'background-position': 'center',
        'padding': '20px',  # Adjust padding as needed
        'color': 'black',   # Text color
    },
        children=[
            html.H6([
                html.Ul([
                    html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_acq]['Asset'].values[0]}"),
                    html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==cargo_acq]['Cruise_speed'].values[0]} knots"),
                    html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_acq]['Max_ROC'].values[0]} ft/min"),
                    html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_acq]['Service_ceiling'].values[0]} ft"),
                    html.Li(f"Range: {asset_df[asset_df['Asset']==cargo_acq]['Range'].values[0]} nm"),
                    html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==cargo_acq]['MTOGW'].values[0]} lb"),
                    html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_acq]['Max_External_Load'].values[0]} lb"),
                    html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])}"),
                    html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_acq]['Operational_cost'].values[0]} USD")
                ])
            ]),
            # Add other components or text as needed
        ]
    )

        if (cargo_acq and maritime_acq):

            Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
        elif (cargo_acq and maritime_st and maritime_st_type):
            if maritime_st_type == 'A':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
            if maritime_st_type == 'B':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
            if maritime_st_type == 'C':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
            if maritime_st_type == 'D':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
            if maritime_st_type == 'E':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
            if maritime_st_type == 'F':
                Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
        else:
            Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
        color = 'red' if Budget < 0 else 'green'

        #print("trigger_id is",dash.callback_context.triggered_id)
        return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
    
    elif last_selected_dropdown=='maritime-acq-drop':
        

        output_text = [html.H6([
                        html.Ul([
                            html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_acq]['Asset'].values[0]}"),
                            html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==maritime_acq]['Cruise_speed'].values[0]} knots"),
                            html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_acq]['Max_ROC'].values[0]} ft/min"),
                            html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_acq]['Service_ceiling'].values[0]} ft"),
                            html.Li(f"Range: {asset_df[asset_df['Asset']==maritime_acq]['Range'].values[0]} nm"),
                            html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==maritime_acq]['MTOGW'].values[0]} lb"),
                            html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_acq]['Max_External_Load'].values[0]} lb"),
                            html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])}"),
                            html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_acq]['Operational_cost'].values[0]} USD")
                        ])
        ])]
        if (maritime_acq and cargo_acq):

            Budget = Budget - radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0]) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
        elif (maritime_acq and cargo_st and cargo_st_type):
            if cargo_st_type == 'A':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
            if cargo_st_type == 'B':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
            if cargo_st_type == 'C':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
            if cargo_st_type == 'D':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
            if cargo_st_type == 'E':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
            if cargo_st_type == 'F':
                Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0]) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
        else:
            Budget = Budget - radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])


        color = 'red' if Budget < 0 else 'green'

        #print("trigger_id is",dash.callback_context.triggered_id)
        return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
    
    
    elif last_selected_dropdown == 'cargo-st-drop' or last_selected_dropdown == 'cargo-st-type-drop':
        if cargo_st_type == 'A':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {asset_df[asset_df['Asset']==cargo_st]['Range'].values[0]} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.2)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.2) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
            
        
        elif cargo_st_type =='B':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==cargo_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.3)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.3) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif cargo_st_type =='C':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {(asset_df[asset_df['Asset']==cargo_st]['Range'].values[0])} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.1)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.1) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
            
        
        elif cargo_st_type =='D':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==cargo_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.4)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.4) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif cargo_st_type =='E':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==cargo_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.5)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]
            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.5) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget

        
        elif cargo_st_type =='F':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==cargo_st]['Asset'].values[0]}-{cargo_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==cargo_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==cargo_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==cargo_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {(asset_df[asset_df['Asset']==cargo_st]['Range'].values[0])} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==cargo_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==cargo_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] * 1.6)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==cargo_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (cargo_st and cargo_st_type and maritime_acq):
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0] *1.6) -radio2*(asset_df[asset_df['Asset']==maritime_acq]['Acquisition_cost'].values[0])
            elif (cargo_st and cargo_st_type and maritime_st and maritime_st_type):
                if maritime_st_type == 'A':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)
                if maritime_st_type == 'B':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)
                if maritime_st_type == 'C':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)
                if maritime_st_type == 'D':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)
                if maritime_st_type == 'E':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)
                if maritime_st_type == 'F':
                    Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6) -radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget

        
    elif last_selected_dropdown == 'maritime-st-drop' or last_selected_dropdown == 'maritime-st-type-drop':    
        if maritime_st_type == 'A':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {asset_df[asset_df['Asset']==maritime_st]['Range'].values[0]} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.2)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.2) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.2)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        
        elif maritime_st_type =='B':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==maritime_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.3)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.3) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.3)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif maritime_st_type =='C':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {(asset_df[asset_df['Asset']==maritime_st]['Range'].values[0])} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.1)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.1) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.1)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif maritime_st_type =='D':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==maritime_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.4)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.4) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.4)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif maritime_st_type =='E':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {round(asset_df[asset_df['Asset']==maritime_st]['Range'].values[0]*1.15)} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.5)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.5) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.5)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
        
        elif maritime_st_type =='F':
            output_text = [html.H6([
                            html.Ul([
                                html.Li(f"Asset Type: {asset_df[asset_df['Asset']==maritime_st]['Asset'].values[0]}-{maritime_st_type}"),
                                html.Li(f"Cruise Speed: {round(asset_df[asset_df['Asset']==maritime_st]['Cruise_speed'].values[0]*1.15)} knots"),
                                html.Li(f"Maximum Rate of Climb: {asset_df[asset_df['Asset']==maritime_st]['Max_ROC'].values[0]} ft/min"),
                                html.Li(f"Service Ceiling: {asset_df[asset_df['Asset']==maritime_st]['Service_ceiling'].values[0]} ft"),
                                html.Li(f"Range: {(asset_df[asset_df['Asset']==maritime_st]['Range'].values[0])} nm"),
                                html.Li(f"Maximum Takeoff Gross Weight: {round(asset_df[asset_df['Asset']==maritime_st]['MTOGW'].values[0]*1.15)} lb"),
                                html.Li(f"Maximum External Load: {asset_df[asset_df['Asset']==maritime_st]['Max_External_Load'].values[0]} lb"),
                                html.Li(f"Acquisition Cost: {convert_to_millions(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] * 1.6)}"),
                                html.Li(f"Operational Cost (per flight hour): {asset_df[asset_df['Asset']==maritime_st]['Operational_cost'].values[0]} USD")
                            ])
            ])]

            if (maritime_st and maritime_st_type and cargo_acq):
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0] *1.6) -radio1*(asset_df[asset_df['Asset']==cargo_acq]['Acquisition_cost'].values[0])
            elif (maritime_st and maritime_st_type and cargo_st and cargo_st_type):
                if cargo_st_type == 'A':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.2)
                if cargo_st_type == 'B':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.3)
                if cargo_st_type == 'C':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.1)
                if cargo_st_type == 'D':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.4)
                if cargo_st_type == 'E':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.5)
                if cargo_st_type == 'F':
                    Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6) -radio3*(asset_df[asset_df['Asset']==cargo_st]['Acquisition_cost'].values[0]*1.6)
            else:
                Budget = Budget - radio4*(asset_df[asset_df['Asset']==maritime_st]['Acquisition_cost'].values[0]*1.6)

            color = 'red' if Budget < 0 else 'green'

            #print("trigger_id is",dash.callback_context.triggered_id)
            return output_text, last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
    else:
            color = 'red' if Budget < 0 else 'green'


            return html.P("No selection."), last_selected_dropdown, html.H6(f"{convert_to_millions(Budget)}", style={'color': color}), Budget
    



           

@app.callback(
    Output('data-table', 'data'),
    [Input('populate-button', 'n_clicks'),Input('output-number', 'value')],
    [State('cargo-acq-drop', 'value'),
    State('maritime-acq-drop', 'value'),
    State('cargo-st-drop', 'value'),
    State('cargo-st-type-drop', 'value'),
    State('maritime-st-drop', 'value'),
    State('maritime-st-type-drop', 'value'),
    State('radio-button1', 'value'),
    State('radio-button2', 'value'),
    State('radio-button3', 'value'),
    State('radio-button4', 'value')]
)

def update_data_table(n_clicks, input_value, cargo_acq, maritime_acq, cargo_st, cargo_st_type, maritime_st, maritime_st_type,radio1,radio2,radio3,radio4):
    # Create a DataFrame with the selected values
    global existing_data
    #existing_data = pd.read_csv('C:\\Users\\toderinde3\\Documents\\HADR_Project\\Year7\\DOE\\Baseline.csv')
    ctx = dash.callback_context
    if ctx.triggered_id == 'populate-button' and n_clicks is not None: 
        if ((cargo_st == None or cargo_st == '') and (maritime_acq == None or maritime_acq == '') and (cargo_st_type == None or cargo_st_type == '') and cargo_acq and maritime_st and maritime_st_type):
            data = {'case_number':[existing_data.shape[0]],
                    'rc_cargo_num':[radio1],
                    'rc_cargo_type': [cargo_acq],
                    'maritime_rc_cargo_num':[radio4],
                'maritime_rc_cargo_type': [maritime_st+'-'+maritime_st_type],}
            new_data = pd.DataFrame(data)
            #new_data = existing_data.append(df, ignore_index=True)
        elif ((cargo_acq == None or cargo_acq == '') and (maritime_acq == None or maritime_acq == '') and cargo_st and cargo_st_type and maritime_st and maritime_st_type):
            data = {'case_number':[existing_data.shape[0]],
                    'rc_cargo_num':[radio3],
                    'rc_cargo_type': [cargo_st+'-'+cargo_st_type],
                    'maritime_rc_cargo_num':[radio4],
                'maritime_rc_cargo_type': [maritime_st+'-'+maritime_st_type]}
            new_data = pd.DataFrame(data)
        elif ((cargo_st == None or cargo_st == '') and (maritime_st== None or maritime_st== '')and (cargo_st_type == None or cargo_st_type == '')and (maritime_st_type == None or maritime_st_type == '') and cargo_acq and maritime_acq):
                  data = {'case_number':[existing_data.shape[0]],
                    'rc_cargo_num':[radio1],
                    'rc_cargo_type': [cargo_acq],
                    'maritime_rc_cargo_num':[radio2],
                'maritime_rc_cargo_type': [maritime_acq]}
                  new_data = pd.DataFrame(data)
        elif ((cargo_acq == None or cargo_acq == '') and (maritime_st== None or maritime_st== '')and (maritime_st_type == None or maritime_st_type == '') and cargo_st and cargo_st_type and maritime_acq):
                  data = {'case_number':[existing_data.shape[0]],
                    'rc_cargo_num':[radio3],
                    'rc_cargo_type': [cargo_st+'-'+cargo_st_type],
                    'maritime_rc_cargo_num':[radio2],
                'maritime_rc_cargo_type': [maritime_acq]}
                  new_data = pd.DataFrame(data)
                  #new_data = existing_data.append(df, ignore_index=True)
        #existing_data = existing_data.append(new_data, ignore_index=True)
        else:
            new_data = []
        
        if input_value>=0 and len(new_data)>0:
            
            #try:

         
        
        

            # Authenticate with Google Drive API
            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            csv_content = new_data.to_csv(index=False)
            
            # Upload CSV to Google Drive
            file_metadata = {
                'name': 'player_1',
                'parents': ['1TjmMTkUM-DeKqUILko9JTBEpgNxDAZKv'],  # Parent folder ID
                'mimeType': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            }
        
            media = MediaIoBaseUpload(io.BytesIO(csv_content.encode('utf-8')), mimetype='text/csv', resumable=True)
            
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
           
            
            # Return the DataFrame records if the upload is successful
            return new_data.to_dict('records')
            #except Exception as e:
                #return f'Error: {str(e)}'
            #new_data.to_csv('C:\\Users\\toderinde3\\OneDrive - Georgia Institute of Technology\\HADR_Project\\Year7\\DOE\\player_1_cases.csv', index=False)
            #return new_data.to_dict('records')
        else:
        # If the button is not clicked yet, return an empty data dict
            return []
    







if __name__ == "__main__":
    app.run_server(debug=True)



