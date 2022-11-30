import streamlit as st
from json import loads
from pandas import read_csv

st.markdown('''
# Exibidor de arquivos

## Suba um arquivo e vejamos o que acontece :smile::heart:
''')


arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'wav', 'csv', 'json']
)

st.text_input('Email', max_chars=10)
st.text_input('Senha', type='password')

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = read_csv(arquivo).transpose()
            st.dataframe(df)
            st.bar_chart(df)
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)
else:
    st.error('Ainda não tenho arquivo!')
