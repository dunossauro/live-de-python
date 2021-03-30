from dash import Dash
from dash_html_components import Div, P, Br
from dash_core_components import Input as DCCInput
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = Div(
    children=[
        DCCInput(id='meu_input1', value='batatinha frita'),
        Br(),
        DCCInput(id='meu_input2', value='Quantas saias a barata tem?'),
        P(id='output1'),
        P(id='output2')
    ]
)


@app.callback(
    [
        Output('output1', 'children'),
        Output('output2', 'children')
    ],
    [
        Input('meu_input1', 'value'),
        Input('meu_input2', 'value'),
    ]
)
def meu_callback(meu_input1, meu_input2):
    return meu_input1, meu_input2


app.run_server()
