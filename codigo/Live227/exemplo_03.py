import streamlit as st
from streamlit.components import v1 as components
from spacy import load, displacy

nlp = load('pt_core_news_lg')

bar = st.sidebar

escolha = bar.selectbox(
    'Escolha uma categoria',
    ['Entidades', 'Gramática']
)

text = st.text_area('Bote um textão aqui!')

doc = nlp(text)


if text and escolha == 'Entidades':
    data = displacy.render(doc, style='ent')

    with st.expander('Dados do spaCy'):
        components.html(
            data, scrolling=True, height=300
        )

    a, b = st.columns(2)
    for e in doc.ents:
        a.info(e)
        b.warning(e.label_)


if text and escolha == 'Gramática':
    filtro = bar.multiselect(
        'Filtro',
        ['VERB', 'PROPN', 'ADV', 'AUX'],
        default=['VERB', 'PROPN']
    )
    with st.expander('Dados do spaCy'):
        st.json(doc.to_json())

    container = st.container()
    a, b, c = container.columns(3)

    a.subheader('Token')
    b.subheader('Tag')
    c.subheader('Morph')

    for t in doc:
        if t.tag_ in filtro:
            container = st.container()
            a, b, c = container.columns(3)
            a.info(t)
            b.warning(t.tag_)
            c.error(t.morph)
